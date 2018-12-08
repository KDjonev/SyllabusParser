from sklearn.feature_extraction.text import CountVectorizer
import random

def textToVector(text, vectorizer):
    text = text.lower()
    text = text.strip()
    # encode document
    vector = vectorizer.transform([text])
    # summarize encoded vector
    return (vector.toarray())


def ReadFile(file):
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


# Read Line by Line, vectorize
# randomize lines

def main():
    allWords = " ".join(ReadFile('Words.txt'))
    lines = ReadFile('truthX.txt')
    vectorizer = CountVectorizer()
    # tokenize and build vocab
    vectorizer.fit([allWords, " ".join(lines)])

    vectors = []
    for line in lines:
        vectors.append((textToVector(line, vectorizer=vectorizer)).tolist()[0])

    lables = ReadFile('truthY.txt')
    for i in range(len(lables)):
        randomNumber = random.randint(0, len(lables) - 1);

        xTmp = vectors[i]
        vectors[i] = vectors[randomNumber]
        vectors[randomNumber] = xTmp

        yTmp = lables[i]
        lables[i] = lables[randomNumber]
        lables[randomNumber] = yTmp

    fileX = open("truthX.csv", "w")
    fileY = open("truthY.csv", "w")
    for vector, lable in zip(vectors, lables):
        fileY.write(lable)
        for x in vector:
            fileX.write(str(x))
            fileX.write(',')
        fileY.write('\n')
        fileX.write('\n')





if __name__ == "__main__":
    main()