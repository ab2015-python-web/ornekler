kelimeler = open("text.txt", "r").read().split(" ")
dizi = {}

for kelime in kelimeler:
	if (len(kelime) > 3):
		dizi[kelime] = kelimeler.count(kelime)



for key,val in dizi.items():
	print "%15s kelime : %s" %(key,"*" * val)
	 
