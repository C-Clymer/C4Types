####################################################################
import sys
import os
import pysam as pys
####################################################################
'''
This program will search for specific reads in a fasta file to determine if
they line up with other HG versions
'''

def main():
    readNames=('ST-E00192:75:H2L7GCCXX:3:2213:16854:22458','ST-E00192:75:H2L7GCCXX:3:2214:29267:21913','ST-E00192:75:H2L7GCCXX:3:1203:9069:16252','ST-E00192:75:H2L7GCCXX:3:2123:32394:16674', 'ST-E00192:75:H2L7GCCXX:3:1119:32759:14037','ST-E00192:75:H2L7GCCXX:3:2118:25421:24708','ST-E00192:75:H2L7GCCXX:3:1221:26354:66233','ST-E00192:75:H2L7GCCXX:3:1221:27014:66286','ST-E00192:75:H2L7GCCXX:3:2222:12906:68079','ST-E00192:75:H2L7GCCXX:3:2222:12906:68079','ST-E00192:75:H2L7GCCXX:3:2213:16854:22458','ST-E00192:75:H2L7GCCXX:3:2214:29267:21913')
    #check for arguments by calling parseArgs
    args = parseArgs(sys.argv)
    #if there are no arguments then close program
    if args == ():
        return
    #set args to variables for use
    readName, inputFile = args
    #set samfile
    samfile = pys.AlignmentFile(inputFile, "rb")
    output=''
    count = 0
    for read in samfile.fetch(until_eof=True):
        count+=1
        if count%100000 == 0:
            print(count)
        if read.query_name.rstrip() in readNames:
            output+=str(read.query_name.rstrip()) + ' vs ' + readName + '\n'
            output+=str(read.cigarstring) + '\t'
            output+=str(read.reference_name) + '\t'
            output+=str(read.reference_start) + '\t'
            output+=str(read.reference_end) + '\n'
    #close samfile
    samfile.close()
    print(output)
    return


'''
Check arguments passed by user and returns arguments.
'''
def parseArgs(args):
    #check for commandline arguments, change compare value to be 1 more than
    #amount you are expecting, if it is less than expected then
    #print out the expected input
    if len(args) != 3:
        print("Usage: read_name input.bam/sam")
        return ()

    #return all arguments split up into big tuple
    return (str(args[1]), str(args[2].rstrip()))
####################################################################
#call main function to start with
if __name__ == "__main__":
    main()
