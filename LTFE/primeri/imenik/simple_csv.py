import sqlite3
import json


with sqlite3.connect('Contacts.sqlite') as conn:
    cur = conn.cursor()

    # Najprej analizirajmo s čim imamo opravka
    cur.execute('SELECT * FROM sqlite_master WHERE TYPE = "table"')
    r = cur.fetchall()
    structure = json.dumps(r, indent=2)
    print(structure)

    # Izčrpamo imenik
    cur.execute('''
        SELECT zwacontact.ZFIRSTNAME, zwacontact.ZINDEXNAME, zwaphone.ZPHONE
        FROM zwaCONTACT, zwaPHONE
        WHERE zwaCONTACT.Z_PK = zwaPHONE.Z_PK
    ''')

    kontakti = cur.fetchall()
    for kontakt in kontakti:
        print(kontakt)


print(kontakti)

with open('Imenik.csv', mode='w', encoding='utf8') as fp:
    fp.write('sep=,\n')
    for kontakt in kontakti:
        fp.write(','.join(kontakt) + '\n')

    
