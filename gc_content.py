def gc_content(dna)
dna=dna.upper()
g=dna.count("G")
c=dna.count("C")
return (g+c)/ 
len(dna)*100  


sequence =
"ATGCGATACGCTTGA"
gc=
gc_content(sequence)
print(f"gc content : {gc:.2f}%")
