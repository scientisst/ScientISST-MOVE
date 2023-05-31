# =============================================================================
# ScientISST MOVE Dataset
# Creation Scripts
#
# Script: anonymize.py
# Description: Anonymizes all '.biosignal' files.
#
# Author: João A. Saraiva
# ©2023 ScientISST, Lisboa, Portugal
# =============================================================================


from datetime import datetime
from os.path import join, isfile

from ltbio.biosignals import Biosignal


# =============================================================================
# Change below

common_path = ""  # FIXME
code = "AP3H"  # FIXME
date = "13_07_2022"  # FIXME


# =============================================================================
# Do not change below

all_biosignals = {}
for modality in ('ecg', 'temp', 'acc_chest', 'acc_e4', 'eda', 'emg', 'ppg', 'resp'):
    path = join(common_path, code, date, 'COMPACT', modality + '.biosignal')
    if isfile(path):
        x = Biosignal.load(path)
        all_biosignals[modality] = x

# A. Shift dates
earliest_date = min([x.initial_datetime for x in all_biosignals.values()])
delta = earliest_date - datetime(2000, 1, 1, 0, 0, 0)
for x in all_biosignals.values():
    x.timeshift(-delta)

# B. Delete Patient Name
for x in all_biosignals.values():
    x._Biosignal__patient._Patient__name = None

# Save
for modality, x in all_biosignals.items():
    x.save(path)
