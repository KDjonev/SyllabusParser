import datefinder
import re

#import nltk
#from nltk.tokenize import word_tokenize
#from nltk.tag import pos_tag
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def isEventOfInterest(string, eventsOfInterest):
    return any(substring in string for substring in eventsOfInterest)


def GetDateEventPairs(data, eventsOfInterest):
    events = []
    for line in data.splitlines():
        if isEventOfInterest(line.lower(), eventsOfInterest):
            # The following string got matched as a date:
            # 'injuries/conditions may require accommodations due to barriers in the structure of'
            # apperently injuries/conditions is interpreted as a date.
            matches = datefinder.find_dates(line)
            dates = []
            for match in matches:
                dates.append(match)
            if len(dates) > 0:
                date = dates[0]
                event = re.sub('\s+', ' ', line).strip()
                #line = nltk.word_tokenize(line)
                #line = nltk.pos_tag(line)
                events.append((dates[0], event))
    return events


def main():
    matches = datefinder.find_dates('injuries/conditions may require accommodations due to barriers in the structure of')
    for match in matches:
        print (match)


if __name__ == "__main__":
    main()