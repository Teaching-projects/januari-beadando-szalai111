#Ez egy szöveg alapú kalandjáték
eletero=100
def jelenet1():
    import time
    print("Felébredtél egy cellában, és egy kedves páncélos úriember leodbja neked a kulcsot. Kinyitod az ajtót vagy maradsz?(kimegyek vagy maradok)")
    time.sleep(4)
    opciov=input("Hozd meg a döntésed: ")
    valasz="helytelen"
    while(valasz=="helytelen"):
        if(opciov.upper()=="MARADOK"):
            print("Ottmaradtál a celládban életed végéig (Ami nem ér véget).")
            valasz="helyes"
        elif(opciov.upper()=="KIMEGYEK"):
            print("Kinyitottad a cellaajtót és kimentél.")
            valasz="helyes"
            jelent2()
        else:
            print("Ez nem a helyes válasz! Írd be vagy kimegyek-et vagy az maradok-őt.")
            opciov=input("Hozd meg a döntésed: ")


def jelent2():
    import time
    print("Miután egy kicsit mentél az intézetben találkozol egy picit szárított húsnak kinéző emberrel, aki rádtámad. Merre akarsz kitérni? (Megjegyzésképp balra láttál valamit.) ")
    time.sleep(4)
    opciov=input("Hozd meg a döntésed: ")
    valasz="helytelen"
    while(valasz=="helytelen"):
        if(opciov.upper()=="BALRA"):
            print("Egy másik megvágta a karod, és 30 életerőt vesztettél, viszont a végén nyertél.")
            print(eletero-30)
            valasz="helyes"
            jelent3()
        elif(opciov.upper()=="JOBBRA"):
            print("Mindkét ellenfeled elkerülted, és egy nehéz harc alatt sérülés nélkül legyőzted őket.")
            valasz="helyes"
            jelent3()
        else:
            print("Ez nem a helyes válasz! Írd be vagy azt hogy balra vagy azt hogy jobbra.")
            opciov=input("Hozd meg a döntésed: ")

def jelent3():
    import time
    print("Jelenleg 70 életerőd van")
    print("Kinyitottál egy hatalmas kaput, ahol található a kijárathoz vezető kapu, viszont egy démon őrzi. A fegyvereddel hátulról vagy előről rontassz neki? (elol vagy hatul)")
    time.sleep(4)
    opciov=input("Hozd meg a döntésed: ")
    valasz="helytelen"
    while(valasz=="helytelen"):
        if(opciov.upper()=="ELOL"):
            print("Miért tennéd? Rádcsapott és majdnem meghaltál, vesztettél 45 életerőt.")
            eletero-40
            opciov=input("Hozd meg a döntésed: ")
        elif(opciov.upper()=="HATUL"):
            print("A szörnyet könnyen legyőzted a vakpontjáról és kinyitottad a kaput.")
            valasz="helyes"
            jelent4()
        else:
            print("Ez nem a helyes válasz! Írd be vagy az elölt vagy a hátult.")
            opciov=input("Hozd meg a döntésed: ")


def jelent4():
    import time
    while eletero >= 40:
        print("Kijutottál, viszont egy szakadékhoz jutottál, melynek szélén egy madárfészek van. Megkockáztatod és belefekszel? (bele vagy kiulsz)")
        time.sleep(4)
        opciov=input("Hozd meg a döntésed: ")
        valasz="helytelen"
        while(valasz=="helytelen"):
            if(opciov.upper()=="BELE"):
                print("Egy óriás madár elragad és elvisz egy új helyre.")
                valasz="helyes"
            elif(opciov.upper()=="KIULSZ"):
                print("Rájöttél, hogy nem fog érted senki se jönni, és az egyetlen menekvésed a madár fészke, mely mikor végül belefekszel elragad, és elvisz egy új helyre.")
                valasz="helyes"
            else:
                print("Ez nem a helyes válasz! Írd be vagy a belét vagy a kiülszt.")
                opciov=input("Hozd meg a döntésed: ")
    else:
        print("Kivéreztél és a táborodtól kezdheted újra a cellában.")
    

jelenet1()

        
