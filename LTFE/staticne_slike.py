from PIL import Image, ImageEnhance, ImageOps
import matplotlib as mpl
import matplotlib.pyplot as plt


def histogram(slika, pokazi=True):
    """Izriše histogram za dano sliko. Ta je lahko sivinska ali barvna.

    Args:
        slika (object): PIL/Pillow objekt
        pokazi (bool): Če želimo takoj videti graf. (Default: True)

    Retuns:
        object: PIL/Pillow objekt

    """
    hst = slika.histogram()
    st_barv = len(histogram) // 256   # stevilo bar; 1 = sivinska, 3 = RGB
    if st_barv == 1:
        bl = hst
        plt.plot(bl, color='bl', alpha=0.5)
        plt.fill_between(range(255), bl, color='black', alpha=0.5)
    elif st_barv == 3:
        r, g, b = hst[:256], hst[256:512], hst[512:] # Razkosamo na 3

        plt.plot(r, color='r', alpha=0.5)
        plt.fill_between(range(256), r, color='red', alpha=0.5)

        plt.plot(g, color='g', alpha=0.5)
        plt.fill_between(range(256), g, color='green', alpha=0.5)

        plt.plot(b, color='b', alpha=0.5)
        plt.fill_between(range(256), b, color='blue', alpha=0.5)
    else:
        raise TypeError('Znam procesirat samo 1 in 3 barvne histograme!')

    plt.autoscale(tight=True)

    if pokazi:
        plt.show()


def v_sivinsko(slika, autokontrast=False, izravnava=False):
    """Sliko pretvori v sivinski barvni prostor.

    Args:
        slika: (object): PIL/Pillow objekt slike
        autokontrast (bool): Avtomatsko popravi kontrast slike. (Default: False)
        izravnava (bool): Skuša izravati histogram slike. (Default: False)

    Returns:
        object: PIL/Pillow objekt

    """
    _slika = slika.copy()
    if _slika.mode != 'L':
        _slika.convert('L')

    if autokontrast:
        _slika = ImageOps.autocontrast(_slika)

    if izravnava:
        _slika = ImageOps.equalize(_slika)

    return _slika

def v_crnobelo(slika, autokontrast=False, izravnava=False):
    """Sliko pretvori v dvorbarvni prostor.

    Args:
        slika: (object): PIL/Pillow objekt slike
        autokontrast (bool): Avtomatsko popravi kontrast slike. (Default: False)
        izravnava (bool): Skuša izravati histogram slike. (Default: False)

    Returns:
        object: PIL/Pillow objekt

    """
    _slika = v_sivinsko(slika, autokontrast=autokontrast, izravnava=izravnava)
    return _slika.point(lambda x: 0 if x < 128 else 255, '1')


def v_sepia(slika, autokontrast=False, izravnava=False):
    """Pretvori slika v sepia (učinek starinske slike).

    Args:
        slika: (object): PIL/Pillow objekt slike
        autokontrast (bool): Avtomatsko popravi kontrast slike. (Default: False)
        izravnava (bool): Skuša izravati histogram slike. (Default: False)

    Returns:
        object: PIL/Pillow objekt

    """

    def linearizacija(bela_barva):
        """Linearizira barvni prostor med med črno in poljubno barvo.

        Args:
            bela_barva (array): Mora biti oblike [int, int, int].

        Returns:
            array: Linearizirana barvna paleta

        """
        ramp = []
        r, g, b = bela_barva
        for i in range(255):
            ramp.extend((round(r*i/255), round(g*i/255), round(b*i/255)))
        return ramp

    sepia = linearizacija([255, 240, 192])
    sivinska = v_sivinsko(slika, autokontrast=autokontrast, izravnava=izravnava)
    return sivinska.putpalette(sepia)
