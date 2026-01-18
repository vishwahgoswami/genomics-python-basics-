>>>dna='atgcatctcgatcgtacgtacgtacgtcgctagctgctagctacgtcgcgatcgtacgatcgatttatatataatatattatgttggtgtcggcgcgtctctcgagag'
no_c=dna.count(c)
no_g=dna.count(g)
dna_length=len(dna)
gc_percentage=(no_c+ no_g)*100/dna_length
print(gc_percentage)

