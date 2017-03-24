filu = open("historiaa.txt")

#Henkilön valitsemien elokuvien katselukerrat
henkilomap = {"(Antero)":0, "(Matti)":0, "(Tuomas)":0, "(Mymmy)":0, "(Robin)": 0, "(Ville)":0,
				"(Joonas)":0, "(Niklas)":0, "(yhteinen)":0, "(arvonta)":0}

#Henkilön valitsemat elokuvat ja arvosanat listana
henkilon_leffat_map = {"(Antero)":[], "(Matti)":[], "(Tuomas)":[], "(Mymmy)":[], "(Robin)":[], "(Ville)":[],
				"(Joonas)":[], "(Niklas)":[], "(yhteinen)":[], "(arvonta)":[]}

#Henkilön osallistumiskerrat
osallistujamap = {"Antero":0, "Matti":0, "Tuomas":0, "Mymmy":0, "Robin": 0, "Ville":0,
				"Joonas":0, "Niklas":0}

#Genrejen katselukerrat
genremap = {"Action":0, "Adventure":0, "Animation":0,"Biography":0, "Comedy":0,
			"Crime":0, "Documentary":0, "Drama":0, "Family":0, "Fantasy":0, 
			"History":0, "Horror":0, "Music":0, "Musical":0, "Mystery":0,
			"Romance":0, "Sci-Fi":0, "Short":0, "Sport":0, "Thriller":0,
			"War":0, "Western":0, "IMDB top 250":0, "Netflix":0}
#----------------------------------
#TIETOJEN KERUU
#----------------------------------
for line in filu:


	#LASKEE KUINKA USEIN KENENKIN ELOKUVA ON KATSOTTU JA LISÄÄ henkilomap
	for henkilo in henkilomap:
		if henkilo in line:
			henkilomap[henkilo] = henkilomap[henkilo] + 1
	if "(mie)" in line:
		henkilomap["(Antero)"] = henkilomap["(Antero)"] + 1


	#LISÄÄ henkilon_leffat_mapiin listan elokuvista kunkin nimen taakse
	for henk in henkilon_leffat_map:

		if henk == "(Antero)":
			if "(mie)" in line:
				rivilista = line.split("(mie)")
				leffa = rivilista[0]
				arvosana = rivilista[1]
				henkilon_leffat_map[henk].append(leffa + arvosana)

		if henk in line:
			rivilista = line.split(henk)
			leffa = rivilista[0]
			arvosana = rivilista[1]
			henkilon_leffat_map[henk].append(leffa + arvosana)

	#LASKEE OSALLISTUMISKERRAT, ISÄNNÄLLE OMA IF KOSKA EI TIEDOSTOSSA, PURKKAINEN
	for osallistuja in osallistujamap:
		if osallistuja in line and ".2" in line:
			osallistujamap[osallistuja] = osallistujamap[osallistuja] + 1
	if ".2" in line:
		osallistujamap["Matti"] = osallistujamap["Matti"] + 1

	#LASKEE GENREJEN KATSONTAMÄÄRÄT
	for genre in genremap:
		if genre in line:
			genremap[genre] = genremap[genre] + 1 

#------------------------------------------
#TULOSTUKSET:
#------------------------------------------
print ("Fax:")
print ()

for henkilo in henkilomap:
	if henkilo == "(yhteinen)":
		print("Yhteinen valinta on katsottu " + str(henkilomap[henkilo]) + " kertaa.")
	elif henkilo == "(arvonta)":
		print("Arvottu elokuva on katsottu " + str(henkilomap[henkilo]) + " kertaa.") 
	else:
		print("Hahmon " + henkilo.strip('(').strip(')') + " elokuva on katsottu " + str(henkilomap[henkilo]) + " kertaa.")

print ()

for osallistuja in osallistujamap:
	if osallistujamap[osallistuja] < 10:
				print("Hahmo " + osallistuja + " on (valitettavasti) \
osallistunut iltamaan " + str(osallistujamap[osallistuja]) + " kertaa.")


	else:
		print("Hahmo " + osallistuja + " on (todistettavasti) \
osallistunut iltamaan " + str(osallistujamap[osallistuja]) + " kertaa.")

print ()

for genre in genremap:
	print("Genreä " + genre +" on katsottu " + str(genremap[genre]) + " kertaa.")

print ()
#----------------------------------------

#HAETAAN ELOKUVIA NIMEN MUKAAN
while True:
	print ("Syötä hahmon nimi tulostaaksesi hänen valitsemansa elokuvat genreineen, sekä niiden saamat arvosanat:")
	nimi = input()
	nimi_suluissa = "(" + nimi + ")"

	if nimi_suluissa in henkilon_leffat_map:
		print (nimi + " on valinnut katsottavaksi elokuvat:")
		print()

		for alkio in henkilon_leffat_map[nimi_suluissa]:
			print (alkio)

	else:
		print("Nimeä ei löydy listasta. Listasta löytyy nimet:" )
		for alkio in henkilon_leffat_map:
			print(alkio[1:-1])

	print()
	print()
	print()
#---------------------------------------------------------------------