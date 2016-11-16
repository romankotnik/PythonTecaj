dat = open('datoteka.txt')
print(dat.read())  # preberemo vsebino

# Deskriptor datoteke moramo zapreti
# sicer pride do uhajanja informacij (leak)
dat.close()  



with open('datoteka.txt') as dat:
    print(dat.read())



class defektOpen:
    def __init__(self, file, mode='r', *args, **kwargs):
        self.__filename = file
        self.__mode = mode

    def __enter__(self):
        # Odpremo deskriptor z os.open
        # Nastavimo še kakšno stvar
        # return self.__deskriptor
        print('Jeeej, zagnal si *with* stavek!')
        return None

    def __exit__(self, type, value, traceback):
        # Se izvede ob zaključku with stavka
        # Tukaj počistimo za seboj (deskriptor, medpomnilnik)
        # Ničesar ne vrnemo
        pass


with defektOpen('datoteka.txt') as dat:
    print(dat)
