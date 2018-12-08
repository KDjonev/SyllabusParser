import subprocess

def GetData(file):
    args = ['pdftotext', '-layout', '-q', file, '-']
    data = subprocess.check_output(args, shell=True, universal_newlines=True)
    return data
