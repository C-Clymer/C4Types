####################################################################
import glob
import sys
import statistics
import os
####################################################################
'''
This will scan through the HG38 file and prompt to ask if we want to save
the chr it is currently openOutFileUsed to strip out all extra chr
'''

def main():

    #check for arguments by calling parseArgs
    args = parseArgs(sys.argv)
    #if there are no arguments then close program
    if args == ():
        return
    inputFa, outputFa = args
    openOutFile = open(outputFa,'w')
    with open(inputFa) as inFile:
        for line in inFile:
            if line[0] == '>':
                save = True
                print(line)
                deleteChr = input("Delete this chr[y/n]? ")
                if deleteChr == 'y':
                    save = False
                else:
                    save = True
            if save == False:
                pass
            else:
                openOutFile.write(line)
    return


'''
Check arguments passed by user and returns arguments.
'''
def parseArgs(args):
    #check for commandline arguments, change compare value to be 1 more than
    #amount you are expecting, if it is less than expected then
    #print out the expected input
    if len(args) != 3:
        print("Usage: input.fa output.fa ")
        return ()

    #otherwise set each var to the respected argument
    arg1 = args[1]
    arg2 = args[2]

    #return all new vars
    return (arg1, arg2)
####################################################################
#call main function to start with
if __name__ == "__main__":
    main()
