from FileSorter import FileSorter
from re import match
import sys

def parseArgs():
    if len(list(filter(lambda arg: match('^(?!\-)', arg), sys.argv))) < 2:
        print('Please input the directory to sort')
    else:
        fs = FileSorter(sys.argv[1])
        fs.sortDirectory()

if __name__ == '__main__':
    parseArgs()