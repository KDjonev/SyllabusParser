import csv
import random
import math


def RunRegression(Xtrain_file, Ytrain_file, test_data_file, pred_file):
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
    predictions = Regression(xData, yData, testXData)

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


def GetRandomXRow(xData):
    return random.randint(0, len(xData) - 1)


def LogisticFunction(xDataRow, wVector):

    XdotW = sum([i*j for (i, j) in zip(xDataRow, wVector)])
    return 1 / (1 + math.pow(math.e, -1 * XdotW))


def DoLcl(yData, p):
    Lcl = 0
    for y in yData:
        Lcl = Lcl + (y[0]*math.log(p) + (1-y[0])*math.log(1-p))
    return Lcl


def Regression(xData, yData, testXData):

    Converged = False
    lam = 0.01
    alpha = 0.01
    learningRateDecay = 0.99
    threshold = 0.0001
    w = [0] * len(xData[0])
    prevLclMinusL2Norm = 0
    while not Converged:
        randomNumbuh = GetRandomXRow(xData)
        x = xData[randomNumbuh]
        y = yData[randomNumbuh][0]
        p = LogisticFunction(x, w)
        w = [w_i + alpha * ((y - p)*x_i - 2*lam*w_i) for (w_i, x_i) in zip(w, x)]

        Lcl = DoLcl(yData, p)
        L2Norm = (sum([i*i for i in w]))
        LclMinusL2Norm = Lcl - lam*L2Norm
        Diff = LclMinusL2Norm - prevLclMinusL2Norm
        prevLclMinusL2Norm = LclMinusL2Norm
        alpha = alpha * learningRateDecay
        if abs(Diff) < threshold:
            Converged = True


    predictions = []
    for test in testXData:
        p = LogisticFunction(test, w)
        result = int(p > 0.5)
        if result == 1:
            predictions.append(['1'])
        else:
            predictions.append(['0'])

    return predictions


def main():
    RunRegression('Xtrain80PercentBro.csv', 'Ytrain80PercentBro.csv', 'Xtest20PercentBro.csv', 'Results.csv')


if __name__ == "__main__":
    main()
