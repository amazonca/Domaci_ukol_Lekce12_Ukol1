# Nyní je naším úkolem vytvořit seznam velitelů, kteří zvítězili v boji proti přesile,
# tj. jejich armáda byla slabší než armáda soupeřů a oni přesto zvítězili.
# Budeme k tomu potřebovat sloupečky s výsledkem bitvy (attacker_outcome),
# informacemi o síle útočníků a obránců (attacker_size a defender_size) a se jmény velitelů.

#NACTENI SOUBORU DO VHODNE STRUKTURY:
#header a data za mna sam nacte modul csv - je na to velmi uzitecny
import csv
with open("battles.tsv", encoding = "utf-8") as soubor_battles:
    data = csv.DictReader(soubor_battles, delimiter="\t") #z modulu csv pouzi metodu DictReader, polozky su oddelene tabulatorem
    # csv.DictReader(...):
    # čte soubor řádek po řádku
    # první řádek bere jako hlavičku
    # každý další řádek vrací jako slovník

    #ted musim z toho vybrat:
    # 1. attacker outcome "win" & attacker size < defender size -> attacker_commander (je ich vic, oddeleno carkou)
    # 2. attacker outcome "loss" & attacker size > defender size -> defender_commander (je ich vic, oddeleno carkou)

    velitele = set() #dam si set nie list, aby sa mi tam nepridavali duplikaty

    for row in data:    # musi to byt uvnitr with, pretoze je to DictReader object a mimo with uz k "data" python neumi pristupit protoze uz je zavren
        #nektere bitvy nemaji zadanou velikost nektere armady,
        #takovou bitvu musime preskocit, protoze nevime ktera armada byla vetsi nebo mensi
        if row["attacker_size"] == "" or row["defender_size"] == "":
            continue

        # na niektorych riadkoch nebude list leaders definovany, takze siho musim definovat tu:
        leaders = None

        # Zjistime, jestli danou bitvu velitel vyhral proti presile
        if row["attacker_outcome"] == "win" and float(row["attacker_size"]) < float(row["defender_size"]): # pokud utocnik vyhral s mensi armadou
            leaders = row["attacker_commander"].strip().split(", ") #pozor je tady carka a mezera, aby mi zmizli mezery pred tymi dalsimi menami
        elif row["attacker_outcome"] == "loss" and float(row["attacker_size"]) > float(row["defender_size"]): # pokud obrance vyhral s mensi armadou
            leaders = row["defender_commander"].strip().split(", ") #pozor je tady carka a mezera, aby mi zmizli mezery pred tymi dalsimi menami

        #pridame list leaders do setu velitele
        if leaders is not None:  # pokud leaders existuje tj jedna z tech podminek byla splnena
            for leader in leaders:
                velitele.add(leader)

print(sorted(velitele))
# ['Brynden Tully', 'Cley Cerwyn', 'Cotter Pyke', 'Davos Seaworth', 'Donal Noye', 'Edmure Tully', 'Garlan Tyrell', 'Jacelyn Bywater', 'Jason Mallister', 'Jon Snow', 'Karyl Vance', 'Mace Tyrell', 'Ramsay Snow', 'Randyll Tarly', 'Robb Stark', 'Rodrik Cassel', 'Sandor Clegane', 'Stannis Baratheon', 'Theon Greyjoy', 'Tyrion Lannister', 'Tytos Blackwood', 'Tywin Lannister']
print(len(velitele)) #22
