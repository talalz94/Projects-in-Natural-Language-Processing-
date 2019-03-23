# The text files in the corpus first have to be segmented
# for that i will first extract all the sentences from all
# the text files provided, depending on the format of the
# text data that is in those files respectively.

dataset = []
p = []
l = []
dataset2 = []
m = []

import os


def get_iterator_all_files(dir_path):
    for (dirpath, dirnames, filenames) in os.walk(dir_path):
        for f in filenames:
            print (f)


import glob, re

def procesesData():
    global f, dataset, p, dataset2, l, m
    for filename in glob.glob(r'C:\Users\Talal\Desktop\Talal\8TH SEMESTER\NLP\NLP Assignment 2\corpus\convo1/*.txt'):
        #file = open(filename, "r") 
        lines = open(filename).readlines()
        dataset.append(lines)

    for i in dataset:
        for j in i:
            if ':' in j:
                #print(c)
                sentence = ((j.split(":")[1]).strip()).lower()
                p.append(sentence)


    # Conversations of different format
    for filename in glob.glob(r'C:\Users\Talal\Desktop\Talal\8TH SEMESTER\NLP\NLP Assignment 2\corpus\convo8/*.txt'):
        #file = open(filename, "r") 
        lines = open(filename, encoding="utf8").readlines()
        dataset2.append(lines)
        dataset2 = [[w.replace("Â\xa0", " ") for w in words] for words in dataset2]  #removing non-ascii characters

    for i in dataset2:
        i = i[7:]
        for j in i:
            
            sentence = (j.strip()).lower()
            #re.sub('\s+',' ',j)
            l.append(sentence)
            m = list(filter(None, l))


    
def loadData():

    from nltk.tokenize import sent_tokenize

    sentenceList = []
    with open('corpusRaw.txt', "r") as f:
        corpus = list(filter(None, f.read().splitlines()))

        
    #segementing sentences

    for i in corpus:
        sentences = sent_tokenize(i)

        for i in sentences:
            if len(i) > 9:

                i = "<s> " + i
                if i[-1] == '.' or i[-1] == '!' or i[-1] == '?':
                    i = i[:-1]   
                i  = i + ' <s/>'

                if ',' in i:

                    i = i.replace(',', '')

                if '.' in i:
                    while '.' in i:
                        
                        i = i.replace('.', '')
                if '  ' in i:
                    while '  ' in i:
                        i = i.replace('  ', ' ')
                        
                sentenceList.append(i)

    

    return sentenceList
        
        
    
        
    
