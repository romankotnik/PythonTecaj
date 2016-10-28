import editdistance
import matplotlib.pyplot as plt
import numpy as np

"""
    Večina tweetov je izmišljenih ali sestavljenih.
"""

twitter_objave = [
  '#Slovenija podiže dodatnih 27 km ograde na granici, #Hrvatska ne vidi potrebu za istim potezom #migranti #izbjeglice http://bit.ly/2eyXvkD',
  'INFO dan o javnem razpisu za #SRIP in #KOC na prioritet. področjih pametne specializac. #S4 v petek, 4.11.2016. Več: http://bit.ly/2dZNzlT.JR',
  'Are you the #javascript #ninja that we are looking for? http://buff.ly/2eyfoC3',
  'PadLeft in FP used yesterday at @jsromandie #ramdajs #javascript #fp #functionalprogramming',
  'Does #JavaScript sometimes make U feel stupid? U R not alone #js #API #php #HTML #WordPress #CSS #SASS #LESS #ui #ux http://meteorlife.com/does-the-javascript-mess-sometimes-make-you-feel-stupid-you-are-not-alone/ …',
  'A Design Workflow Comparison: Photoshop vs Illustrator vs Sketch - https://designmodo.com/design-workflow-comparison/ …',
  'Premijer Hrvatske: Nema potrebe za podizanjem ograde na granicama http://www.klix.ba/clanak/161022071 … #izbjeglice #andrejplenkovic',
  'Paradox Interactive has Halloween Sale. Expansions galore! https://www.paradoxplaza.com/featured-deals?type=20&utm_source=Community+Newsletter&utm_campaign=a52dcf5447-emsub_papl_plaza_email_20161027_hasa&utm_medium=email&utm_term=0_6b1b68c4d1-a52dcf5447-146446121 …'
  'Lojze Peterle: priznavajo, da sem kompetenten in kvalificiran za funkcijo predsednika EP ter vključujoč in pošten',
  'Nagrada mađarskoj snimateljici koja je šutirala izbjeglice http://www.euskola.com/nagrada-madarskoj-snimateljici-koja-je-sutirala-izbjeglice/?utm_campaign=nagrada-madarskoj-snimateljici-koja-je-sutirala-izbjeglice&utm_medium=twitter&utm_source=twitter … #izbjeglice #madjarska #nagrada #snimateljica',
  'Sirijska djeca prave odjeću za Veliku Britaniju, rade 12 sati za 2 KM http://www.klix.ba/clanak/161024002 … #izbjeglice',
  'I did not know this, but apparently that happens if you connect USB-C devices on android together. https://fscl01.fonpit.de/userfiles/6473453/image/nexus_5x_6p_power_supply_android_marshmallow_usb_type_c-w782.jpg …',
  'So, I cannot charge the iPhone 7+ I bought LAST MONTH on the new MacBook Pro released TODAY without an adaptor. How ridiculous is that?',
  'To je ta sadistična psihopatologija inšpektorjev, "davkarije", politikov (ki so tak zakon sprejeli) in celega naroda',
  'Godina dana nakon promjene zakona o #azil -u: nedovoljna provjera i ubrzane #deportacije #izbjeglice http://dw.com/p/2Rc39',
  'Njemačka štampa o samoubistvu mladog izbjeglice u Šmelnu. Navodno su mu dovikivali: "Skoči već jednom!" #izbjeglice http://dw.com/p/2RbqM',
  'Če so vam vdrli preko oddaljenega namizja in zašifrirali datoteke z bitlockerjem, nas kontaktirajte. Morda imamo rešitev. #ransomware',
  'Na slovenskoj granici ćemo donijeti pune četiri konvoje izbjeglica',
  'čudn3 s0 t3 1zbj3gl1c3'
]

vse_razdalje = []

for tweet in twitter_objave:
    stavek = tweet.split()
    razdalja_tweeta = []
    for beseda in stavek:
        tmp = editdistance.eval('izbjeglice', beseda)
        razdalja_tweeta.append(tmp)

    vse_razdalje.append(razdalja_tweeta)


visina, sirina = len(vse_razdalje), max([ len(vse_razdalje[i]) for i in range(len(vse_razdalje)) ])
vse_razdalje = np.array(vse_razdalje)

empty = np.full((visina, sirina), np.NAN)

for x in range(len(vse_razdalje)):
    for y in range(len(vse_razdalje[x])):
        empty[x,y] = vse_razdalje[x][y]


### Statistika
besede = {}

for tweet in twitter_objave:
    stavek = tweet.split()
    for beseda in stavek:
        tmp = editdistance.eval('izbjeglice', beseda)
        if tmp < 5:
            besede[beseda] = tmp

print(besede)


#empty *= 1.0/empty.max()
#empty = abs(empty - 1.0)

#fig, ax = plt.subplots()
#ax.imshow(empty, cmap=plt.cm.afmhot, interpolation='nearest')
#ax.set_title('dropped spines')

#plt.show()
