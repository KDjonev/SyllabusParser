import os
import re

import PdfImporter
import TxtImporter
import DateEventExtractor
import GoogleCalendarWrapper

# For now, only .txt is supported, use https://pdftotext.com/ to get the txt files.
def GetText(file):
    filename, fileExtension = os.path.splitext(file)
    if fileExtension == '.txt':
        data = TxtImporter.GetData(file)
    elif fileExtension == '.pdf':
        data = PdfImporter.GetData(file)
    return data


# Moatly for testing and debugging.
def ProcessDateEvents(dateEventPairs):
    for date, event in dateEventPairs:
        print(date, event)


def ParseSyllabus(clas, file):
    # Import the file and get the text data:
    data = GetText(file)
    # Events and dates associated with those dates.
    # eventsOfInterest = ['due', 'exam', 'quiz' 'midterm', 'final', 'no class']
    eventsOfInterest = ['due', 'exam', 'no class', 'project presentation']
    dateEventPairs = DateEventExtractor.GetDateEventPairs(data, eventsOfInterest)
    # Upload these to Google Callender
    ProcessDateEvents(dateEventPairs)
    #GoogleCalendarWrapper.AddEvent(clas, dateEventPairs)


def main():
    # Import the file and get the text data:
    ParseSyllabus('CS272', '../Syllabuses/Cs272F18.txt')
    print("*******************************************")
    ParseSyllabus('CS291i', '../Syllabuses/Cs291iF18.txt')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/agneta87382fall2018.pdf')
    print("*******************************************")
    ParseSyllabus('', '../Syllabuses/laberge84176fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/laberge84169fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/blm271128fall2018.pdf')
    print("*******************************************")
    ParseSyllabus('', '../Syllabuses/finou84484fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/mespey68657fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/apg70337fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/childer70372fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/mbrosse82972fall2018.pdf')
    print("*******************************************")
    ParseSyllabus('', '../Syllabuses/mespey68657fall2018.pdf')
    print("*******************************************")
    ParseSyllabus('', '../Syllabuses/lorip78933fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/edmondb81075fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/chochri82699fall2018.pdf')
    #print("*******************************************")
    #ParseSyllabus('', '../Syllabuses/vcondon73151fall2018.pdf')


if __name__ == "__main__":
    main()