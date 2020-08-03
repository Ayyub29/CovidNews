import os
import nltk
import re
import sys

def getNearestNumbers(Pattern, Kalimat): 
    expression = r"(?i)(?:\b)"+ Pattern +"(?:\D{0,100})([0-9][0-9,\.]*)[^.,]|([0-9][0-9,\.]*)[^.,](?:\D{0,100})" + Pattern
    listOfAllNumbers = re.findall(expression,Kalimat)
    number = '-1'
    for listOfNumbers in listOfAllNumbers:
        for numbers in listOfNumbers:
            if (numbers != ''):
                number = numbers
    #print(listOfAllNumbers)
    return number

def getAllDates(str):
    expression = r"(?i)(?:\b\D{0,100})((((Kini|Sebelum(nya)?|Hari\s(ini|depan)?|Minggu\s(ini|depan)?|Besok|Lusa|Kemarin|Setelah(nya)?)?((satu|dua|tiga|empat)?(\s)?(se)?hari\s|(se)?pekan\s|(se)?musim))?(\s)?(Sen(in)?|Sel(asa)?|Rab(u)?|Ka(mis)?|Ju(mat)?|Sab(tu)?|Min(ggu)?)?(\s)?(\s|-|,|/|\()?(\s)?((tanggal\s|tgl\s)(\s)(\d{1,2}))?(\s)?((\d{1,2})?(\s|-|,|\/)?(\s)?((\d{1,2}|Jan(uari)?|Feb(ruari)?|Mar(et)?|Apr(il)?|Mei|Jun(i)?|Jul(i)?|Agu(stus)?|Sep(tember)?|Okt(ober)?|Nov(ember)?|Des(ember)?)(\s)?(\s|-|,|\/)?(\d{2,4})?)?(\s)?((tahun\s)(\d{2,4}))?)?(\s)?(\s|-|,|/|\))?(\s)?((pukul)(\s)?(\d{2})?(:|\.)?(\s)?(\d{2})?(:)?(\s)?(\d{2})?(\s)?(WIB|WITA|WIT)?)?(\s)?(pagi|siang|sore|malam)?)(\s)?(Depan|Lalu|Kemarin)?)"
    array = re.findall(expression,str)
    return array

def getSentence(Pattern,Kalimat):
    expression = r"(?i)(?:\b)"+ Pattern +"(\D{0,100})([0-9][0-9,]*)[^.,]|([0-9][0-9,]*)[^.,](?:\D{0,100})" + Pattern
    kata = re.search(expression,Kalimat)
    return kata[0]

def getLongestDates(lists):
    max = 0
    kata = "bacod"
    for list in lists:
        for word in list:
            if (len(word) >= max):
                kata = word
                max = len(word)
    return kata

def getRealDates(str):
    listAllDates = getAllDates(str)
    RealDates = getLongestDates(listAllDates)
    listOfDatesFound = re.findall("\D+",RealDates)
    if (len(listOfDatesFound) == 1 and listOfDatesFound[0] == ' ') or (len(listOfDatesFound) < 1):
        RealDates = -1
    if RealDates == "bacod":
        RealDates = -1
    return RealDates
