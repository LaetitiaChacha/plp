f = open("C:\\Users\\Laetitia\\Documents\\SIMPLON\\Programmation\\Python\\plp\\input\\connexion.log.txt", 'r')
for line in f:
    liste_prenoms = line.strip()
    liste_prenoms2= liste_prenoms.split(";")
    print (liste_prenoms2) 




 

    