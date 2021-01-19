f=open ("C:\\Users\\Laetitia\\Documents\\SIMPLON\\Programmation\\Python\\plp\\input\\connexion.log.txt","r")
lines = [i for i in f.readlines()]

for line in lines :
    print (line.split(";")[1])
    user = open ("C:\\Users\\Laetitia\\Documents\\SIMPLON\\Programmation\\Python\\plp\\input\\utilisateurs.txt", "a")
user.write (line.split(";")[1] +"\n")#

user.close()

for line in f: 
    liste_prenoms = line.strip()
    liste_prenoms2= liste_prenoms.split(";")
    print (liste_prenoms2)

user.close()


f=open ("C:\\Users\\Laetitia\\Documents\\SIMPLON\\Programmation\\Python\\plp\\input\\connexion.log.txt","r")
for line in f:
    heure = line.split(" ") [1]
    # print(heure)
    sIP=line.split(";")[0]
    sID=line.split(";")[1]
    if heure<"08:00" or heure>"19:01":
        print(sIP,sID)
        break



   

