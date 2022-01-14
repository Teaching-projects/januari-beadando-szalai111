#Ez egy szöveg alapú kalandjáték
import time
import random
eletero=100
eletero2=0

def eleterovesztes1(eletero):
    global eletero2
    eletero2=eletero-random.randint(0,30)
    print("Ennyi életed maradt",eletero2)
    return eletero2
        
def jelenet1():
    print("Felébredtél egy cellában, és egy kedves páncélos úriember leodbja neked a kulcsot. Kinyitod az ajtót vagy maradsz?(kimegyek vagy maradok)")
    time.sleep(2)
    valasz=input("Hozd meg a döntésed: ")
    valasz_helyes=False
    while(valasz_helyes==False):
        if(valasz.upper()=="MARADOK"):
            print("Ottmaradtál a celládban életed végéig (Ami nem ér véget).")
            valasz_helyes=True
        elif(valasz.upper()=="KIMEGYEK"):
            print("Kinyitottad a cellaajtót és kimentél.")
            valasz_helyes=True
            jelenet2()
        else:
            print("Ez nem a helyes válasz! Írd be vagy kimegyek-et vagy az maradok-őt.")
            valasz=input("Hozd meg a döntésed: ")
        


def jelenet2():
    print("Miután egy kicsit mentél az intézetben találkozol egy picit szárított húsnak kinéző emberrel, aki rádtámad. Merre akarsz kitérni? (Megjegyzésképp balra láttál valamit.) ")
    time.sleep(2)
    valasz=input("Hozd meg a döntésed: ")
    valasz_helyes=False
    while(valasz_helyes==False):
        if(valasz.upper()=="BALRA"):
            print("Egy másik megvágta a karod,viszont a végén nyertél.")
            valasz_helyes=True
            eleterovesztes1(eletero)
            jelenet3()
        elif(valasz.upper()=="JOBBRA"):
            print("Mindkét ellenfeled elkerülted, és egy nehéz harc alatt sérülés nélkül legyőzted őket.")
            valasz_helyes=True
            print("Ennyi életed maradt",eletero)
            jelenet3()
        else:
            print("Ez nem a helyes válasz! Írd be vagy azt hogy balra vagy azt hogy jobbra.")
            valasz=input("Hozd meg a döntésed: ")


def jelenet3():
    print("Kinyitottál egy hatalmas kaput, ahol található a kijárathoz vezető kapu, viszont egy démon őrzi. A fegyvereddel hátulról vagy előről rontassz neki? (elol vagy hatul)")
    time.sleep(2)
    valasz=input("Hozd meg a döntésed: ")
    valasz_helyes=False
    while(valasz_helyes==False):
        if(valasz.upper()=="ELOL"):
            print("Miért tennéd? Rádcsapott és majdnem meghaltál,viszont azért valahogy legyőzted.")
            valasz_helyes=True
            eleterovesztes1(eletero2)
            jelenet4()
        elif(valasz.upper()=="HATUL"):
            print("A szörnyet könnyen legyőzted a vakpontjáról és kinyitottad a kaput.")
            valasz_helyes=True
            jelenet4()
        else:
            print("Ez nem a helyes válasz! Írd be vagy az elölt vagy a hátult.")
            valasz=input("Hozd meg a döntésed: ")



def jelenet4():
    print("Kijutottál, viszont egy szakadékhoz jutottál, melynek szélén egy madárfészek van. Megkockáztatod és belefekszel? (bele vagy kiulsz)")
    time.sleep(2)
    valasz=input("Hozd meg a döntésed: ")
    valasz_helyes=False
    while(valasz_helyes==False):
        if(valasz.upper()=="BELE"):
            print("Egy óriás madár elragad és elvisz egy új helyre.")
            valasz_helyes=True
            vege()
        elif(valasz.upper()=="KIULSZ"):
            print("Rájöttél, hogy nem fog érted senki se jönni, és az egyetlen menekvésed a madár fészke, mely mikor végül belefekszel elragad, és elvisz egy új helyre.")
            valasz_helyes=True
            vege()
        else:
            print("Ez nem a helyes válasz! Írd be vagy a belét vagy a kiülszt.")
            valasz=input("Hozd meg a döntésed: ")

def vege():
    print("Itt az első terület vége")



jelenet1()


        
