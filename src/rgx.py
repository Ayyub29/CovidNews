import nltk
import os
import re
import util
import sys

def searchWithRegex(Pattern,File):
    Ada = True
    listOfFound = re.findall(Pattern,File)
    if (len(listOfFound) < 1):
        Ada = False
    return Ada

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
    ada = searchWithRegex(pat,kalimat)
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