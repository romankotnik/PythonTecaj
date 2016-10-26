import re

opis = '''
    (Ne povedat slavistom, da uporabljam decimalno piko.)
    Moj avto ima prevoženih preko 125000km.
    Motor je bencinar 1.0.
    Porabo ima 5.5l/km.
    Je 5-vraten model Hyundai i20.
'''

pesem = '''
    4 majhne račke šle so na potep. Daleč čez 9 gora. Mama kliče ga-ga-ga
    3 mahjne račke so doma. 3 majhne račke šle so na potep ...

    Za 9-imi gorami, za 9-imi vodámi, za 9-imi hribi in dolinami je živela zver.

    13 malih slončno se je pozibavalo na pajčevini tam pod drevesom ...
'''



regex = r'[-+]?[0-9]*\.?[0-9]+[\w/]*'
rezultat = re.findall(regex, opis)
print(rezultat)
