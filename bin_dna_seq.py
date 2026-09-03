#Binning DNA sequences
#input .dna files contain DNA sequences of varying length, one DNA sequence per line. The scripts create nine new folders (eg. one sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc. ). Write out each DNA sequence in the input files to a separate file in the appropriate folder. 


import os

# create a variable to hold the sequence number. It is outside of all loops.
sequence =1 

#look at files with.dna one by one (!!!as elements in a list/the current folder:   
for file_name in os.listdir('.'):
    if file_name.endswith('.dna'): #NB: endswith is a string method
        print ('Found a file named: ', file_name, '+.dna')
        
        # open one by one .dna files
        file_object = open(file_name)
        
        # split DNA as elements of a list/file
        for line in file_object:
            ##store dna seq in a varible- dna. 
            dna = line.rstrip('\n') #!!! One line is one dna in the original dna.txt 
            length = len(dna)
            print ('Find a dna sequence with length of ', str(length))
                       

            #!!!a condition test to decide which bin (and path) to go. You can change the stop from 1000 to a more appropriate number for your cases.      
            for lower_num in range(100,1000,100):
                upper_num = lower_num+99
                #!!! decision point: 
                if length > lower_num and length < upper_num: 
                     # Create new folders of bins by automatically naming after lengths:
                    bin_folder_name= str(lower_num)+'-'+str(upper_num)
                    print ('this dna goes to bin : ', bin_folder_name)
                    
                    # destination bin folder can be written into path as one argument of `open` function to create a new file:
                    #NB-no / needed at the begining of path (see below of pathlib method for cross platforms)
                    path = bin_folder_name+'/'+str(sequence)+'.dna'
                    print ('path is : ' + path)
                    output = open(path,'w')
                    output.write(dna)
                    output.close()
                    print ('output is : ' + str(sequence)+'.dna')
                    
                    sequence = sequence + 1


       
