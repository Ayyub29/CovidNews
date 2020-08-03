import os
import nltk
import re
import util
import sys

def searchWithBM(Pattern, File): 
    PatternLength = len(Pattern) 
    FileLength = len(File) 
    Ada = False

    badChar = patternRecognizer(Pattern, PatternLength)  
  
    itrFile = 0
    while(itrFile <= FileLength - PatternLength): 
        itrPattern = PatternLength-1
        while itrPattern >= 0 and Pattern[itrPattern] == File[itrFile + itrPattern]: 
            itrPattern -= 1
        if itrPattern < 0: 
            Ada = True
            if itrFile + PatternLength < FileLength:
                itrFile += (PatternLength - badChar[ord(File[itrFile + PatternLength])])
            else:
                itrFile += 1
        else: 
            itrFile += max(1, itrPattern - badChar[ord(File[itrFile + itrPattern])])
    return Ada 

def patternRecognizer(Pattern, PatternLength): 
    badChar = [-1]*256
  
    for i in range(PatternLength): 
        badChar[ord(Pattern[i])] = i; 
  
    return badChar 

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
    ada = searchWithBM(pat,kalimat)
    if (ada):
        print("Kalimat yang mengandung keyword : ")
        print("\n")
        print(kalimat)
        print("\n")
        print("jumlah : " + str(util.getNearestNumbers(pat,kalimat)))
        print("\n")
        waktu = str(util.getRealDates(kalimat))
        if waktu != '-1':
            print("waktu: " + str(util.getRealDates(kalimat)))
        else:
            print("waktu: " + str(sent_text[2]))
