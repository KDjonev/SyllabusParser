import csv
from math import log


def RunNaiveBayes(Xtrain_file, Ytrain_file, test_data_file, pred_file):
    '''The function to run your ML algorithm on given datasets, generate the predictions and save them into the provided file path

    Parameters
    ----------
    Xtrain_file: string
        the path to Xtrain csv file
    Ytrain_file: string
        the path to Ytrain csv file
    test_data_file: string
        the path to test data csv file
    pred_file: string
        the prediction file to be saved by your code. You have to save your predictions into this file path following the same format of Ytrain_file
    '''

    # read data from Xtrain_file, Ytrain_file and test_data_file
    xData, yData, testXData = readTrainingData(Xtrain_file, Ytrain_file, test_data_file)

    # your algorithm
    predictions = NaiveBayes(xData, yData, testXData)

    # save your predictions into the file pred_file
    savePredictions(pred_file, predictions)


def readTrainingData(Xtrain_file, Ytrain_file, test_data_file):

    with open(Xtrain_file, 'rb') as f:
        reader = csv.reader(f)
        xData = list(reader)
        for i in range(len(xData)):
            xData[i] = [float(x) for x in xData[i]]
    with open(Ytrain_file, 'rb') as f:
        reader = csv.reader(f)
        yData = list(reader)
        for i in range(len(yData)):
            yData[i] = [float(x) for x in yData[i]]
    with open(test_data_file, 'rb') as f:
        reader = csv.reader(f)
        testXData = list(reader)
        for i in range(len(testXData)):
            testXData[i] = [float(x) for x in testXData[i]]
    return xData, yData, testXData


def savePredictions(pred_file, predictions):
    with open(pred_file,'wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(predictions)


def NaiveBayes(xData, yData, testXData):

    # Bullet point 1
    TrueTrainingCount = 0.0
    FalseTrainingCount = 0.0

    for label in yData:
        if label[0] == 1.0:
            TrueTrainingCount = TrueTrainingCount + 1.0
        else:
            FalseTrainingCount = FalseTrainingCount + 1.0
    # Bullet point 2
    TotalTrainingCount = TrueTrainingCount + FalseTrainingCount
    # Bullet point 3
    TokenInTrueDocument = [0] * len(xData[-1])
    TokenInFalseDocument = [0] * len(xData[-1])

    for TokenVector, Label in zip(xData, yData):
        if Label[0] == 1.0:
            for i in range(0, len(xData[-1])):
                TokenInTrueDocument[i] = TokenInTrueDocument[i] + TokenVector[i]
        else:
            for i in range(0, len(xData[-1])):
                TokenInFalseDocument[i] = TokenInFalseDocument[i] + TokenVector[i]

    # AddOne Smoothing
    TokenInTrueDocument = [x+1 for x in TokenInTrueDocument]
    TokenInFalseDocument = [x+1 for x in TokenInFalseDocument]

    # Bullet point 4
    TotalTokenInTrueDocument = sum(TokenInTrueDocument)
    TotalTokenInFalseDocument = sum(TokenInFalseDocument)

    predictions = []

    for testData in testXData:
        totalSumTrue = 0.0
        for i in range(0, len(testData)):
            if testData[i] > 0:
                totalSumTrue = totalSumTrue + log(TokenInTrueDocument[i] / TotalTokenInTrueDocument)
        totalSumTrue = totalSumTrue + log(TrueTrainingCount/TotalTrainingCount)

        totalSumFalse = 0.0
        for i in range(0, len(testData)):
            if testData[i] > 0:
                totalSumFalse = totalSumFalse + log(TokenInFalseDocument[i] / TotalTokenInFalseDocument)
        totalSumFalse = totalSumFalse + log(FalseTrainingCount/TotalTrainingCount)

        if totalSumTrue > totalSumFalse:
            predictions.append(['1'])
        else:
            predictions.append(['0'])

    return predictions


def main():
    RunNaiveBayes('Xtrain90.csv', 'Ytrain90.csv', 'Xtest.csv', 'Results.csv')


if __name__ == "__main__":
    main()
