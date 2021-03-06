'''Y el marín tomaba de sus 100 cervezas, no compartía con nadie, avanzaba con certeza
acabó con una y vio 99 cervezas, al ver que acababan se rascó la cabeza'''

cervezas = 100

while cervezas>0:
    if cervezas == 1:
        print('Y el marín tomaba de su última cerveza, no compartía con nadie, avanzaba con certeza')
    else:
        print('Y el marín tomaba de sus', cervezas,'cervezas, no compartía con nadie, avanzaba con certeza')
    cervezas = cervezas-1
    if cervezas == 1:
        print('acabó con una y vio', cervezas, 'cerveza, al ver que acababan se rascó la cabeza.\n')
    elif cervezas == 0:
        print('acabó con esta y vio', cervezas, 'cervezas, al ver que acabaron se voló la cabeza.\n')
    else:
        print('acabó con una y vio', cervezas, 'cervezas, al ver que acababan se rascó la cabeza.\n')
print('Esta fue la historia de un triste marín.')
