def GetData(file):
    with open(file, 'r', encoding="utf8", errors='ignore') as myfile:
        data = myfile.read()
    return data