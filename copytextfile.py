'''
Created on Feb 7, 2012

@author: Meredith
Command Line Arguments
'''
#command line arguments
import sys

def copy_text_file(src, dst):
    try:
        input_file = open(src, "r")
    except IOError as error:
        print("I/O error(" + str(error.error) + "): " + src + ", " + error.strerror + ".")
        sys.exit(1)
    try:
        output_file = open(dst, "w")
    except IOError as error:
        print("I/O error(" + str(error.error) + "): " + dst + ", " + error.strerror + ".")
        sys.exit(1)
    input_file = open(src, "r")#r for read
    output_file = open(dst, "w")#w for write
    for line in input_file:
        output_file.write(line)
        input_file.close()
        output_file.close()
    
def main():
    '''argv[]--- made list
    copytextfile.py, a.txt, b.txt are arguments in the list
    '''
    if len(sys.argv) != 3:
        print("Usage: python " + sys.argv[0] + "[source file] ")
        sys.exit(1)
    copy_text_file(sys.argv[1], sys.argv[2])
    pass

if __name__ =='__main__':
    main() 