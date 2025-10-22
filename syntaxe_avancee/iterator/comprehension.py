liste  = ['A', 'B', 'C', 'AA', 'BB']

liste2 = [(letter, letter) for letter in liste if len(letter) > 1]
print(liste2) #['AA', 'BB'] #['AAAA', 'BBBB'] #[('AA', 'AA'), ('BB', 'BB')]

gen2 = ((letter, letter) for letter in liste if len(letter) > 1)
print(gen2) #<generator object <genexpr> at 0x00000250B91635E0>
liste.append("ZZ")
print(list(gen2))
print(list(gen2)) #[]