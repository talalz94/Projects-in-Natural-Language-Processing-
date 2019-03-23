#12416449

import pandas as pd
from collections import OrderedDict


myFile = 'textfile.txt'   
    


#This function takes a text file and a transition table as input
# Example " search('textfile.txt', df ) "

def search(file, table):

    #Dividing each line into a seperate list element
    with open(file, "r") as f:
        names = list(filter(None, f.read().splitlines()))

    
    state = 0
    line = 0 
    for j in names:

        line += 1
        for i in range (len(j)):

            #first check if alphabet exists in the pattern

            if (j[i] in list(df.columns)):
                


            #check if the some state exists for that alphabet
            #and then update the state
                if (pd.isnull(df.loc[state,j[i]]) == False):
                    state = df.loc[state,j[i]]

                # if the final state is reached, string has been found and state is reset
                if state == patternlen:
                    
                    print('Name found at Line: ' + str(line))
                    state = 0

            else:
                state = 0

        
  

    
# transition table for any given string, using pandas dataframe
# Example " transitionTable('sana') "
def transitionTable(pattern):

    global patternlen
    patternlen = len(pattern)
    
    df = pd.DataFrame()

    # Removing dupilcates
    alphabets = list(OrderedDict.fromkeys(pattern))
    alphabets.insert(0, "State")
    tableCols = alphabets
    df = pd.DataFrame(columns = tableCols)

    #Populating rows with the number of states
    states = list(range(len(pattern) + 1))
    df['State'] = states
    df.set_index('State', inplace=True)

    #Populating transition table according to the NFA of the pattern
    for i in range(len(pattern)):
        
        df.loc[i,pattern[i]] = i+1
  
    return df
        
    

