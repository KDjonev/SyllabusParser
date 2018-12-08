import csv
from math import log


def RunVotedPerceptron(Xtrain_file, Ytrain_file, test_data_file, pred_file):
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
    predictions = VotedPerceptron(xData, yData, testXData)

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
        for i in range(0, len(yData)):
            if yData[i][0] == 0.0:
                yData[i][0] = -1.0
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


def VotedPerceptron(xData, yData, testXData):

    k = 1
    c = [0] * (len(xData) + 5)
    w = []
    w.append([0] * len(xData[-1]))
    w.append([0] * len(xData[-1]))
    t = 0
    T = 20
    while t <= T:
        for yi, xi in zip(yData, xData):
            XdotW = sum([i*j for (i, j) in zip(xi, w[k])])
            if yi[0] * XdotW <= 0:
                yixi = [x * yi[0] for x in xi]
                w.append([0] * len(xData[-1]))
                w[k+1] = [sum(x) for x in zip(w[k], yixi)]
                c[k+1] = 1
                k = k + 1
            else:
                c[k] = c[k] + 1
            t = t + 1

    predictions = []
    for test in testXData:
        y = 0
        for smallK in range(1, k):
            XdotW = sum([i*j for (i, j) in zip(test, w[smallK])])
            signbit = 1
            if XdotW < 0.0:
                signbit = -1
            y = y + c[smallK] * signbit
        if y >= 0:
            predictions.append(['1'])
        else:
            predictions.append(['0'])

    return predictions


def main():
    RunVotedPerceptron('Xtrain90.csv', 'Ytrain90.csv', 'Xtest.csv', 'Results.csv')


if __name__ == "__main__":
    main()
