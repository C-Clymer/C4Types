# C4Types
This goal of this project is to determine if a C4 gene is present in a patient.

This project is still ongoing.

Current main file is bam_sam_reader.py.  This script scans the file in specified regions of
the genome to determine if there is any split/break in the region.

find_read.py is used to find specific reads in a sam file. I used it to confirm the location of a specific read between
two different versions of the human genome.

hgedit.py was used to strip out all the extra chromosomes inside hg38 since we are only concerened with chr 1-22,x,y,m

