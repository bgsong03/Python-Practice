sequence = "CAGCAGCTACCGAACACGGTCCCCGACAATCGTAACATCCACAATA"
new = ""
for i in range(len(sequence)):
  if sequence[i] == 'C':
    new += 'G'
  elif sequence[i] == 'G':
    new += 'C'
  elif sequence[i] == 'T':
    new += 'A'
  elif sequence[i] == 'A':
    new += 'U'

print(new)