# 1. Template for marking elan files.
## Tiers names.
Each Elan file have to contain the following tiers:

| NB! |          Tier in ELAN          |                          Comments                         |
|:---:|:------------------------------:|:---------------------------------------------------------:|
|  !  | Speaker_Transcription-txt-andi | text                                                      |
|     | Speaker_Lemma-txt-andi         | lemmas                                                    |
|     | Speaker_POS-txt-en             | Info associated with the lexical item e.g. Part of speech |
|  !  | Speaker_Morph-txt-en           | division into morphemes                                   |
|  !  | Speaker_Gloss-txt-en           | English glosses                                           |
|  !  | Speaker_Translation-gls-...    | free translation into ... language                        |
|     | Speaker_Gloss-txt-...          | glosses in ... language                                   |
|     | Speaker_Translation-gls-...    | free translation into ... language                        |
|     | Speaker_Participant-note-...   | comments on ... language                                  |

The name of each layer has a clear structure: \
The name of the speaker and the name of the layer are separated by a lower underscore, all other fields by a hyphen. You can only change the speaker's name and ISO language code.
[speaker_name of the layer]-[layer type]-[code of the writing system]

What are the [layer type]:
* txt - the main line of transcription (Baseline)
* gls - for the sentence, this type means free translation
* lit - literal translation
* note - notes

[code of the writing system] --- ISO code (can be found here: https://www.ethnologue.com/browse)


NB! There can be several layers in the markup with the same name, but different languages. For example, if you have a translation into two languages (for example, Russian and English), the names of the layers will look like this:
* Speaker_Translation-gls-en
* Speaker_Translation-gls-en

## Hierarchy of layers.
The **Transcription** layer does not depend on any layers. The layers **Morph**, **Translation** and **Participant** depend on **Transcription**. The **Gloss** layer depends on the **Morph** layer. If you have a speaker *A* and the source language is *Andi (andi)*, the markup will look like this:

**picture**

As a separator, only spaces are used, but they should not be used anywhere in the layer. Separator for the gloss is a hyphen, everything else needs to be separated by something else (for example, Baba_Yaga).
