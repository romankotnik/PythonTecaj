import re

opis = '''
    (Ne povedat slavistom, da uporabljam decimalno piko.)
    Moj avto ima prevoženih preko 125000km.
    Motor je TurboDiezel 2.0.
    Porabo ima 6.2L/km.
    Je 5-vraten model.
'''

pesem = '''
    4 majhne račke šle so na potep. Daleč čez 9 gora. Mama kliče ga-ga-ga
    3 mahjne račke so doma. 3 majhne račke šle so na potep ...

    Za 9-imi gorami, za 9-imi vodámi, za 9-imi hribi in dolinami je živela zver.

    13 malih slončno se je pozibavalo na pajčevini tam pod drevesom ...
'''

# Najdi vse številke!
# Katere številke se pojavljajo?
regex = r'[0-9]+'
rezultat = re.findall(regex, pesem)
print(rezultat)




#regex = r'[+-]?\d*[\.,\ ]?\d+'
# Uloviti moramo 125,826.13; 2.0; 6.2 in 5
regex = r'[-+]?[0-9]*\.?[0-9]+'
rezultat = re.findall(regex, opis)
print(rezultat)
