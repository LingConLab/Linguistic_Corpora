# validator.py
Before converting your data into a *tsacorpus* format, you need to make sure that you did everything correctly using the layout template.

To do this, use the program validator.py. For the validator it is necessary to put all files (.eaf and .wav) in a folder "data" and in the same directory where this folder lies, to put meta.csv, a template.csv and gloss.csv.

## Functions implemented in the validator
* are all layers properly named? **done** \
Works only if the layers are the same number as in the template --- this will be repaired later 
* Do the speakers match with the speakers in the metadata for the particular file? **done**
* Are all the files specified in the metadata included among the "data" folder? **done** 
  * If the folder contains more or less files than the metadata, the program indicates this. **done**
* Are all glosses specified in the file with glosses?
* Is the hierarchy correct in the Elan file? **done** \
Works only if the layers are the same number as in the template --- this will be repaired later 
* are the types of layers correct? **done** \
Works only if the layers are the same number as in the template --- this will be repaired later 
* Are all fields in the metadata specified correctly?
* Is the same number of audio files and elan files?
* Is the duration of all markup is included in the length of the sound file?
