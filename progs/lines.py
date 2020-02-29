import os
def getFirst(filename, mode):
    with open(filename , mode) as file:
        if os.path.isfile(filename):
            return file.readline()
        else:
            return None

getFirst('Test.txt','r' )