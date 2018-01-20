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

In the template you can use word-by-word division, as, for example, here:

**picture**

Types of all layers:

|           title          |      layer type      |
|:------------------------:|:--------------------:|
| A_Transcription-txt-andi | -                    |
| A_Morph-txt-andi         | Symbolic Subdivision |
| A_Lemma-txt-andi         | Symbolic Association |
| A_Gloss-txt-en           | Symbolic Association |
| A_POS-txt-en             | Symbolic Association |
| A_Translation-gls-ru     | Symbolic Association |
| A_Participant-note-en    | Symbolic Association |



## Metadata.
The list of possible fields in the metadata table lies in meta_template.csv. Bold in those columns that should be required. The metadata file must be in the .csv format and have the following appearance (each line is one speaker in the file):

|     file_title     | speaker_id | ... | ... | ... |
|:------------------:|:----------:|:---:|:---:|:---:|
| andi_pirozki_1.eaf | A          |     |     |     |
| andi_pirozki_1.eaf | B          |     |     |     |
| andi_pirozki_2.eaf | A          |     |     |     |
| andi_pirozki_2.eaf | B          |     |     |     |
| andi_pirozki_2.eaf | C          |     |     |     |

## Glosses.

A file with glosses is a table (.csv format), in which first there is what is in the markup, and in the next column it is written which large category this gloss refers to. For example:

| voc   | case   |
|-------|--------|
| adnum | case   |
| m     | gender |
| f     | gender |
| n     | gender |
| mf    | gender |
| tran  | vType  |
| intr  | vType  |
| pf    | aspect |
