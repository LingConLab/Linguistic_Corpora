
# coding: utf-8

# In[10]:


from lxml import etree
import xml.etree.ElementTree as ET
import os
import pandas as pd 


# * правильно ли названы все слои (**done** *только если слоев столько же, сколько в шаблоне --- ето исправим попозже*)
# * совпадают ли спикеры со спикерами в мете для данного файла **done**
# * все ли файлы, указанные в метаданных, есть среди наших данных? **done** + больше или меньше **done**
# * все ли глоссы указаны в файле с глоссами?
# * правильная ли иерархия в элановском файле? (**done** *только если слоев столько же, сколько в шаблоне --- ето исправим попозже*)
# * правильные ли типы слоев? (**done** *только если слоев столько же, сколько в шаблоне --- ето исправим попозже*)
# * все ли поля в метаданных указаны правильно?
# 
# если аудио корпус:
# * есть ли звуковые данные для всех файлов?
# * входит ли длительность всей разметки в длительность звукового файла?

# In[11]:


#download meta data
meta = pd.read_csv('meta.csv')


# In[12]:


#download template data
template = pd.read_csv('tier_template.csv')


# In[13]:


def get_eafData(root):
    res = []
    for child in root:
        if child.tag == 'TIER':
            tier_name = child.attrib.get("TIER_ID")
            print 
            tier_arr = tier_name.split('-')
            i = 0
            for el in tier_arr[0].split('_'):
                tier_arr.insert(i, el)
                i += 1
            tier_arr.remove(tier_arr[2])
            tier_arr.append(child.attrib.get("LINGUISTIC_TYPE_REF"))
            parent = child.attrib.get("PARENT_REF")
            if parent != None:
                tier_arr.append(parent.split('-')[0].split('_')[1])
            else:
                tier_arr.append('None')
            res.append(tier_arr)
    return res


# In[14]:


# how many speakers in the file
def n_speakers(data):
    n_speakers = len(data)/6
    if n_speakers == 1:
        return [[0,6]]
    if n_speakers == 2:
        return [[0,6], [6,12]]
    if n_speakers == 3:
        return [[0,6], [6,12], [12,18]]


# In[15]:


# check the names of the layers
def is_names(eaf_df):
    for index in n_speakers(eaf_df):
        i, j = index
        speaker = [i for i in set(eaf_df[i:j:]['speaker'])]
        if sorted((eaf_df.tier_name[i:j:]+'-'+eaf_df.flex_type[i:j:]).tolist()) != sorted((template.tier_name +'-'+ template.flex_type).tolist()):
            raise Exception("The tier names in the elan file (for speaker " + ''.join(speaker) + ") does not match the tier names in the template (tier_name and flex_type fields).")


# In[16]:


# check the types of the layers
def is_types(eaf_df):
    for index in n_speakers(eaf_df):
        i, j = index
        speaker = [i for i in set(eaf_df[i:j:]['speaker'])]
        if sorted((eaf_df.tier_name[i:j:]+'-'+eaf_df.tier_type[i:j:]).tolist()) != sorted((template.tier_name +'-'+ template.tier_type).tolist()):
            raise Exception("The tier types in the elan file (for speaker " + ''.join(speaker) + ") does not match the tier types in the template (tier_type field).")


# In[17]:


# checking the hierarchy of tiers
def is_hierarchy(eaf_df):
    for index in n_speakers(eaf_df):
        i, j = index
        speaker = [i for i in set(eaf_df[i:j:]['speaker'])]
        if sorted((eaf_df.tier_name[i:j:]+'-'+eaf_df.parent_tier[i:j:]).tolist()) != sorted((template.tier_name +'-'+ template.parent_tier).tolist()):
            raise Exception("tiers hierarchy in the elan file (for speaker " + ''.join(speaker) + ") does not match the tiers hierarchy in the template (parent_tier field).")


# In[33]:


# looking for all elan and wav files in data folder
def wavs_eafs():
    file_names = os.listdir('./data')
    eafs = []
    wavs = []
    for file in file_names:
        if '.eaf' in file:
            eafs.append(file)
        if '.wav' in file:
            wavs.append(file)
    return eafs, wavs


# In[19]:


# checking .eaf file names and file names in the meta.csv
def is_file_title(eafs):
    if len(set(meta.file_title.tolist())) < len(eafs):
        raise Exception("You did not specify all the .eaf files in the meta.csv.")
    if len(set(meta.file_title.tolist())) > len(eafs):
        raise Exception("You have fewer files than you specified in the meta.csv.")
    if sorted(set(meta.file_title.tolist())) != sorted(eafs):
        raise Exception("The names of the .eaf files do not match the file names in the meta.csv.")


# In[20]:


# checking names of the speakers in eaf files and in the mata.csv
def is_speaker_id(eaf_df, filename):
    meta_spiakers = (meta['speaker_id'].loc[meta['file_title'] == filename]).tolist()
    eaf_speakers = [i for i in set(eaf_df['speaker'])]
    if  sorted(meta_spiakers) != sorted(eaf_speakers):
        raise Exception("The names of the speakers in the " + filename + " and in the metadata do not match.")


# In[31]:


def main():
    for eaf in eafs:
        tree = ET.parse('./data/' + eaf)
        root = tree.getroot()
        eaf_df = pd.DataFrame(get_eafData(root), columns=['speaker', 'tier_name', 'flex_type', 'lang', 'tier_type', 'parent_tier'])
        is_speaker_id(eaf_df, eaf)
        is_file_title(eafs)
        is_hierarchy(eaf_df)
        is_types(eaf_df)
        is_names(eaf_df)


# In[32]:


eafs, wavs = wavs_eafs()
main()

