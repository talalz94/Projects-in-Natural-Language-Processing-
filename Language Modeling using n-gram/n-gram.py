



from random import choices

train = False


#Loads the processed corpus which was processed earlier by 'text processing.py'
def loadCorpus ():

    with open('corpusProcessed.txt', "r") as f:
        corpus = list(filter(None, f.read().splitlines()))

    return corpus

#Calculates frequency of each word in the entire corpus
def wordFreq():
    import re

    dic = {}

    for sentence in loadCorpus():
        for word in re.split('\s', sentence): # split with whitespace
            try:
                dic[word] += 1
            except KeyError:
                dic[word] = 1

    return dic


# Calculates the n-gram for the corpus. n can be 1 or 2 or 3 etc
def ngrams(n):

    ngram = {}
    
    for i in loadCorpus():

        words = i.split()

        while len(words) >= n:
            
            key = ' '.join(words[:n])

            if key in ngram:

                ngram[key] += 1

            else:
                ngram[key] = 1

            del words[0]

    return ngram           

#Calculates the number of words in corpus            
def noOfWords():

    c = 0
    for i in loadCorpus():
        c = c + len(i.split())

    c = c - len(loadCorpus())*2 # removing start and end tokens

    return c


#The main unigram function trains the corpus on unigram model 
def unigramTrain():


    
    global train, wordListUnigram, pListUnigram
    
    l = len(loadCorpus())
    dataDic = ngrams(1)
    pDic = {}                # will contain words along with their probability of occurence
    c = noOfWords()
    
    for i in dataDic:

        if i != '<s>' and i!= '<s/>':           #Calculating the probability for all the words
            pDic[i] = dataDic[i]/c


    wordListUnigram = list(pDic.keys())
    pListUnigram = list(pDic.values())
    
    train = True


#Generates a word based on the unigram model
def generateUnigram():

    if not (train):
        
        unigramTrain()
        print('Model trained! \n')

    

    x = int(input('Enter number of words you want to generate: '))
    print('\n')
    

    for i in range(x):

        print(choices(wordListUnigram ,pListUnigram)[0])    #outputs the word based on its probability

            

#The main bigram function trains the corpus on bigram model, no need to run this
def bigramTrain(text):
    
    global train, wordListBigram, pListBigram

    c = 0
    l = len(loadCorpus())
    dataDic = ngrams(2)
    
    biDic = {}                # will contain words along with their probability of occurence
    pDicBi = {}
    
    
    for i in dataDic:
        if i.split(' ')[0] == text:
            c = c + dataDic[i]
            biDic[i] = dataDic[i]

    for i in biDic:

        pDicBi[i] = biDic[i] / c           #calculating the maximum likelihood estimate by Count(wi-1,wi)/Count(wi-1)
        
    wordListBigram = list(pDicBi.keys())
    pListBigram = list(pDicBi.values())

    return (choices(wordListBigram ,pListBigram)[0]).split(' ')[1]  #outputs the word based on its probability
    

# Run this function to run the generate words using bigram
def generateBigram():

    text = ''
    while text not in ngrams(1).keys():
        
        text = input('Enter a valid starting word from the corpus: ')

    print('\n')

    x = int(input('Enter the number of words you want to generate: '))

    for i in range(x):

        a = bigramTrain(text)
        if a == '<s/>':                                     # To make the text continous, end of sentence will mean the next token is start to sentence.
            a = '<s>'
        print (a)
        text = a
    
      
    

    
 
    
            

            

            

        
