liste = {"apple":"elma"}
while(True):
    girdi = raw_input("Lutfen bir deger giriniz=")
    if not girdi in liste:
        liste[girdi] = raw_input("Listede yok sen gir=")
    else:
        print liste[girdi]
