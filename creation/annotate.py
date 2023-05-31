# =============================================================================
# ScientISST MOVE Dataset
# Creation Scripts
#
# Script: annotate.py
# Description: Annotate all '.biosignal' files with the events marked on Empatica E4.
#
# Author: João A. Saraiva
# ©2023 ScientISST, Lisboa, Portugal
# =============================================================================


from os.path import join

from ltbio.biosignals import Event
from ltbio.biosignals.modalities import *

# =============================================================================
# Change below

common_path = ""  # FIXME
code = "AP3H"  # FIXME
date = "13_07_2022"  # FIXME

# =============================================================================
# Do not change below

ecg = ECG.load(join(common_path, code, date, 'COMPACT', 'ecg.biosignal'))
eda = EDA.load(join(common_path, code, date, 'COMPACT', 'eda.biosignal'))
temp = TEMP.load(join(common_path, code, date, 'COMPACT', 'temp.biosignal'))
acc_chest = ACC.load(join(common_path, code, date, 'COMPACT', 'acc_chest.biosignal'))
acc_e4 = ACC.load(join(common_path, code, date, 'COMPACT', 'acc_e4.biosignal'))
emg = EMG.load(join(common_path, code, date, 'COMPACT', 'emg.biosignal'))
ppg = PPG.load(join(common_path, code, date, 'COMPACT', 'ppg.biosignal'))
resp = RESP.load(join(common_path, code, date, 'COMPACT', 'resp.biosignal'))

# FIXME all these event corrections
temp.events[0].offset = resp.domain[1].end_datetime  # event 1
temp.events[1].offset = resp.domain[2].end_datetime  # event 2
temp.events[2].offset = resp.domain[3].end_datetime  # event 3
temp.events[3].offset = temp.events[4].onset   # event 4
temp.events[4].offset = resp.final_datetime  # event 5
temp.set_event_name('event1', 'lift')
temp.set_event_name('event2', 'greetings')
temp.set_event_name('event3', 'gesticulate')
temp.set_event_name('event4', 'run')
temp.set_event_name('event5', 'walk_after')

temp.associate(Event('stairs_down_and_walk_before', resp.domain[4].start_datetime, resp.domain[4].end_datetime))
acc_e4.associate(temp.events)

resp.associate(temp.events)
baseline = Event('baseline', resp.domain[0].start_datetime, resp.domain[0].end_datetime)
resp.associate(baseline)

# Copy events
eda.associate(resp.events)
emg.associate(resp.events)
ppg.associate(resp.events)
ecg.associate(resp.events)
acc_chest.associate(resp.events)

# Save
save_common_path = join(common_path, code, date, 'COMPACT')
ecg.save(join(save_common_path, 'ecg.biosignal'))
eda.save(join(save_common_path, 'eda.biosignal'))
emg.save(join(save_common_path, 'emg.biosignal'))
resp.save(join(save_common_path, 'resp.biosignal'))
temp.save(join(save_common_path, 'temp.biosignal'))
ppg.save(join(save_common_path, 'ppg.biosignal'))
acc_e4.save(join(save_common_path, 'acc_e4.biosignal'))
acc_chest.save(join(save_common_path, 'acc_chest.biosignal'))
