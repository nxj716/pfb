# A complete Python program to translate a DNA sequence into a protein sequence. 
# Dictionary-gencode uses- http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1.
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


#a test dna seq (or swap with your dna sequences inside the ''.):
dna = 'ATGuTAGGGATTTAACTATT'

# Standardize input to uppercase
dna = dna.upper()
#creat a string list (protein)
protein = ''
    

#split a DNA sequence up into codons
for start in range(0,len(dna)-2,3):
    codon = dna[start:(start+3)]
    aa = gencode.get(codon, 'X') #X for unknown codons (codons not in the above adictionary-gencode)
    protein = protein + aa
    
    # Stop translation if a stop codon (_) is encountered
    if aa == '_':
        break #The program stops reading any remaining DNA nucleotides as translation terminates.
            
    
print (protein)                                                                                                  

                                                                                                                
