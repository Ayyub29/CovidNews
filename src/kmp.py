import os
import nltk
import re
import sys
import util

def searchWithKMP(Pattern, File):

    #Instansiasi Variabel
    PatternLength = len(Pattern) 
    FileLength = len(File)
    cntPattern = 0
    cntFile = 0
    Ada = False

    Prefix = [0]*PatternLength

    borderFunction(Pattern, Prefix)
    while ( cntFile < FileLength ):
        if (Pattern[cntPattern] == File[cntFile] ):
            cntFile += 1
            cntPattern += 1
        if ( cntPattern == PatternLength ):
            Ada = True
            cntPattern = Prefix[cntPattern-1]
        elif cntFile < FileLength and Pattern[cntPattern] != File[cntFile]: 
            if cntPattern != 0: 
                cntPattern = Prefix[cntPattern-1] 
            else: 
                cntFile += 1
    return Ada


def borderFunction(Pattern, Prefix):
    # Fungsi yang mengembalikan nilai border Function dari suatu Pattern
    # Masukan : String Pattern
    # Keluaran : List of Integer yang berisi 
    PatternLength = len(Pattern) 
    cntPrefix = 0
    Prefix[0]
    cntSuffix = 1
    while ( cntSuffix < PatternLength):
        if (Pattern[cntSuffix] == Pattern[cntPrefix]):
            cntPrefix +=1
            Prefix[cntSuffix] = cntPrefix
            cntSuffix += 1
        else:
            Prefix[cntSuffix] = 0
            cntSuffix += 1

name = sys.argv[1]

fileName = '../test/' #Untuk Ubuntu
fileName2 = '..\\test\\' #Untuk Windows

try:
    fileName += name
    txtFile = open(fileName) #Untuk Ubuntu
except:
    fileName2 += name
    txtFile = open(fileName2) #Untuk Windows
txt = txtFile.read().replace("\n", " ")

pat = sys.argv[2]

ada = False
sent_text = nltk.sent_tokenize(txt)

for sentence in sent_text:
    kalimat = str(sentence)
    ada = searchWithKMP(pat,kalimat)
    if (ada):
        print("Kalimat yang mengandung keyword : ")
        print()
        print(kalimat)
        print()
        print("jumlah : " + str(util.getNearestNumbers(pat,kalimat)))
        waktu = str(util.getRealDates(kalimat))
        if waktu != '-1':
            print("waktu: " + str(util.getRealDates(kalimat)))
        else:
            print("waktu: " + str(sent_text[2]))


        