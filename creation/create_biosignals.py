# =============================================================================
# ScientISST MOVE Dataset
# Creation Scripts
#
# Script: create_biosignals.py
# Description: Create '.biosignal' files from the raw ScientISST and Empatica E4 files.
#
# Author: João A. Saraiva
# ©2023 ScientISST, Lisboa, Portugal
# =============================================================================


from os import mkdir
from os.path import join, isdir

from ltbio.clinical.conditions import COVID19
from ltbio.biosignals.sources import E4
from ltbio.biosignals.modalities import *
from ltbio.biosignals.sources import Sense
from ltbio.clinical.BodyLocation import BodyLocation
from ltbio.clinical.Patient import Patient, Sex


# =============================================================================
# Change below

common_path = ""  # FIXME
code = "AP3H"  # FIXME
date = "13_07_2022"  # FIXME
patient = Patient(code, age=25, sex=Sex.F, conditions=(COVID19(0.5), ))  # FIXME
patient.add_note('There is family history of cardiac disease, although the subject did not know what the diagnosis was.')
patient.add_note('2 coffees on the acquisition day. Last full meal 6h a go.')


# =============================================================================
# Do not change below

# Arm
path = join(common_path, code, date, 'arm')
source = Sense('run_arm')
eda_arm = EDA(path, source, patient, BodyLocation.WRIST_L, name='L-Wrist EDA with Gel Electrodes')
emg_arm = EMG(path, source, patient, BodyLocation.BICEP_L, name='L-Bicep EMG with Gel Electrodes')
ppg_arm = PPG(path, source, patient, BodyLocation.INDEX_L, name='L-Index PPG')

# Chest
path = join(common_path, code, date, 'chest')
source = Sense('run_chest')
ecg_chest = ECG(path, source, patient, BodyLocation.CHEST, name='Chest-Abdomen ECG')
acc_chest = ACC(path, source, patient, BodyLocation.CHEST, name='Chest-Abdomen ACC')
resp_chest = RESP(path, source, patient, BodyLocation.CHEST, name='Chest-Abdomen RESP Band')

# Wrist
path = join(common_path, code, date, 'wrist')
source = E4
acc_e4 = ACC(path, source, patient, BodyLocation.WRIST_L, name='L-Wrist ACC from E4')
acc_e4.delete_events()
ppg_e4 = PPG(path, source, patient, BodyLocation.WRIST_L, name='L-Wrist PPG from E4')
ppg_e4.delete_events()
eda_e4 = EDA(path, source, patient, BodyLocation.WRIST_L, name='L-Wrist EDA from E4')
eda_e4.delete_events()
temp_e4 = TEMP(path, source, patient, BodyLocation.WRIST_L, name='L-Wrist TEMP from E4')

# Join biosignals
ecg = ecg_chest
eda = eda_arm & eda_e4
emg = emg_arm
temp = temp_e4
ppg = ppg_e4 & ppg_arm
resp = resp_chest

# Change some channel names
eda.set_channel_name('eda', 'E4')
ppg.set_channel_name('bvp', BodyLocation.WRIST_L)

# Last check
print(ecg)
print(eda)
print(emg)
print(resp)
print(temp)
print(ppg)
print(acc_e4)
print(acc_chest)

# Save
save_common_path = join(common_path, code, date, 'COMPACT')
if not isdir(save_common_path):
    mkdir(save_common_path)
ecg.save(join(save_common_path, 'ecg.biosignal'))
eda.save(join(save_common_path, 'eda.biosignal'))
emg.save(join(save_common_path, 'emg.biosignal'))
resp.save(join(save_common_path, 'resp.biosignal'))
temp.save(join(save_common_path, 'temp.biosignal'))
ppg.save(join(save_common_path, 'ppg.biosignal'))
acc_e4.save(join(save_common_path, 'acc_e4.biosignal'))
acc_chest.save(join(save_common_path, 'acc_chest.biosignal'))
