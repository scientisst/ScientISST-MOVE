# Creation of ScientISST MOVE

In this directory, the script used to prepare the dataset are shared.

## After each Session

The following scripts were run in this order:

1. `create_biosignals.py` | Creates `.biosignal`files from the raw ScientISST and Empatica E4 files.  This file was different for all sessions, so an example is here shown.
2. `anonymize.py` | Anonymizes `.biosignal` files.
3. `annotate.py` | Annotates `.biosignal` files events and other metadata. This file was different for all sessions, so an example is here shown.

## Preparation for public sharing

The following scripts were run in this order:

1. `redo_biosignals.py` | Standardizes channel names, event names, and other metadata.
2. `to_csv.py` | Converts `.biosignal` files to `.csv` files.

____
© 2023 LTBio, ScientISST, Lisboa
