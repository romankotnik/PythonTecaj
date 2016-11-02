"""
    Namen: Seznanitev in primerjava surovega SQL in ORM SQLAlchemy

"""

def surovi_sql():
    import sqlite3

    con = sqlite3.connect(':memory:')  # Podatkovna baza bo v spominu

    cur = con.cursor()
    cur.execute('CREATE TABLE osebe (ime text, priimek text, starost text, kupil boolean)')

    # V DB vnesemo podatke
    cur.execute('INSERT INTO osebe VALUES ("Janez", "Kranjski", 31, 0)')
    cur.execute('INSERT INTO osebe VALUES ("Marta", "Novak", 44, 1)')
    cur.execute('INSERT INTO osebe VALUES ("Mišo", "Prekmurc", 27, 1)')

    con.commit()  # Spremembe shranimo v DB

    for vrstica in cur.execute('SELECT * FROM osebe ORDER BY starost DESC'):
        print(vrstica)  # Preberimo vse vrstice

    con.close()
    #('Marta', 'Novak', '44', 1)
    #('Janez', 'Kranjski', '31', 0)
    #('Mišo', 'Prekmurc', '27', 1)


def orm_sqlalchemy():
from sqlalchemy import create_engine, CheckConstraint,  Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Razred za deklerativno definicijo podatkovnega modela

class Oseba(Base):
    __tablename__ = 'osebe'  # Ime tabele v podatkovni bazi, če tega ni SQLAlchemy sam poimenuje
    id = Column('id', Integer(), primary_key=True, nullable=False)  # Unikatna identifikacija objekta
    ime = Column('ime', String(), nullable=False)  # Column(<ime_polja_v_bazi>, PodatkovniTip, nullable=<JeLahkoBrezVrednosti?>, blank=<JeLahkoPrazno?>)
    priimek = Column('priimek', String(), nullable=False)
    starost = Column('starost', Integer(), nullable=False)
    kupil = Column('kupil', Boolean(), nullable=False, default=False)  # Privzeta vrednost je "False"

    __table_args__ = (
        # Nastavimo preverjanje starosti. Ta mora biti pozitivno celo število.
        CheckConstraint('starost > 0', name='Pozitivna starost'),
    )

    def __repr__(self):
        return '<Oseba ime="{}", priimek="{}", starost={} kupil={}>'.format(self.ime, self.priimek, self.starost, self.kupil)

engine = create_engine('sqlite:///:memory:', echo=True)  # Podatkovna baza je samo v spominu. Zaradi "echo=True" izpisuje kaj je naredil SQLAlchemy
Base.metadata.create_all(engine)  # Ustvari vse tabele, ki so dedovale od "Base"

DBSession = sessionmaker(bind=engine)  # Vzpostavitev seje. Seja lahko omogoča transakcijo. Lahko obstaja v drugi podatkovni bazi.
session = DBSession()  # ustvarimo eno sejo. Lahko imamo več sočasnih

oseba1 = Oseba(ime='Janez', priimek='Kranjski', starost=44, kupil=False)
oseba2 = Oseba(ime='Janez', priimek='Kranjski', starost=31, kupil=True)
oseba3 = Oseba(ime='Mišo', priimek='Prekmurc', starost=27, kupil=True)

session.add(oseba1)  # V sejo dodamo "oseba1", vendar ta še ni zapisana v podatkovno bazo.
session.add(oseba2)
session.add(oseba3)
session.commit()  # Vsi vnosi v seji se zapišejo.

# Da bo primer enak tistemu z direktnim SQL, sortirajmo po starosti, padajoče.
osebe = session.query(Oseba).order_by(Oseba.starost.desc()).all()  # V bazi poišči vse vnose
for oseba in osebe:
    print(oseba)


if __name__ == '__main__':
    surovi_sql()
    orm_sqlalchemy()
