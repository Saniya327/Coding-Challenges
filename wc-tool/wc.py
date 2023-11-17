import getopt
import io
import os
import sys

def main(argv):
    
    opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    if(len(argv) == 2):
        ifile=argv[1]
        print(get_bytes(ifile))
        print(get_lines(ifile))
        print(get_words(ifile))
        return 0
    opt = str(argv[1])
    ifile = argv[2]
   
    if opt == '-c': #bytes
        print(get_bytes(ifile)) 
    elif opt == "-l": #lines
        print(get_lines(ifile)) 
    elif opt == "-w": #words
        print(get_words(ifile)) 
    elif opt =="-m": #chars
        print(get_chars(ifile)) 
    else: 
        return 0


def get_bytes(filename):
    return (os.path.getsize(filename))

def get_words(filename):
    f = open(filename, "r")
    lines = f.readlines()
    count = 0
    for line in lines:
      words = line.split()
      count += len(words)
    return count

def get_lines(filename):
    f = open(filename, "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        count=count+1
    return count

def get_chars(filename):
    f = io.open(filename, "rb")
    lines = f.read()
    count = len(lines.decode('utf-8'))
    return count


if __name__=="__main__": 
    main(sys.argv) 


#print(get_bytes("test.txt")) #342190
#print(get_lines("test.txt")) #7145
#print(get_words("test.txt")) #58164
#print(get_chars("test.txt")) #339,292

