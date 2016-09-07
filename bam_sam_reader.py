####################################################################
import sys
import os
import pysam as pys
####################################################################
'''
This script will scan an entire SAM file looking for reads
in the specified regions.

It then prints out a total count along with information on each read
'''

def main():

    #check for arguments by calling parseArgs
    args = parseArgs(sys.argv)
    #if there are no arguments then close program
    if args == ():
        return
    #set args to variables for use
    startPos, endPos, inputFile = args
    #set samfile
    samfile = pys.AlignmentFile(inputFile, "rb")


    totalReadsInRegion=0    #hold total reads count
    totalSplitReads=0       #hold total split reads count
    totalIntactReads=0      #hold total intact reads count
    totalOtherReads=0       #other

    output = ''
    #step through the indexed sam/bam file to get each read
    #that fits into the region
    for read in samfile.fetch('chr6', startPos, endPos):

        #increment the total count
        totalReadsInRegion+=1
        #determine is cigar is None, if it is then add to other count and go to next loop
        if read.cigarstring == None:
            totalOtherReads+=1
            print("None")
            continue
        #break current cigar into a set for fast access
        temp=set(read.cigarstring)
        #check if CIGAR contains all 4 types of mutations, if it does its likely it isnt mapped well
        if ('M' in temp and 'D' in temp and 'I' in temp and ('S' in temp or 'H' in temp)):
            totalOtherReads+=1
            print("All four")
        #if it contains S, it is a split
        elif ('S' in temp or 'H' in temp):
            totalSplitReads+=1
            output += ('\n' + read.cigarstring + '\t' + str(read.reference_start) + '\t' + str((read.reference_end)-1))
        #otherwise it is intact
        else:
            totalIntactReads+=1

    #output results
    print("Total reads:" + '\t' + str(totalReadsInRegion))
    print("Total intact:" + '\t' + str(totalIntactReads))
    print("Total split:" + '\t' + str(totalSplitReads))
    print("Total other:" + '\t' + str(totalOtherReads))
    print(output)

    #close samfile
    samfile.close()

    return


'''
Check arguments passed by user and returns arguments.
'''
def parseArgs(args):
    #check for commandline arguments, change compare value to be 1 more than
    #amount you are expecting, if it is less than expected then
    #print out the expected input
    if len(args) != 4:
        print("Usage: StartPosition EndPosition input.bam/sam")
        return ()

    #return all arguments split up into big tuple
    return (int(args[1]), int(args[2]), args[3])
####################################################################
#call main function to start with
if __name__ == "__main__":
    main()
