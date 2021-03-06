from unicodedata import normalize

s = 'Sergio Luis López Ñerbel'
print('Nombre original:', s)
print('\n')
s1 = normalize('NFKD', s).encode("ascii","ignore").decode("ascii")
print('Nombre sin carácteres especiales:', s1)
print('\n')
print('Nombre en minúscula:', s1.lower())
