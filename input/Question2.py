
f=open ("C:\\Users\\Laetitia\\Documents\\SIMPLON\\Programmation\\Python\\plp\\input\\connexion.log.txt","r")
for line in f:
    heure = line.split(" ") [1]
    print(heure)
    sIP=line.split(";")[0]
    sID=line.split(";")[1]
    if heure<"08:00" or heure>"19:01":
        print(sIP,sID)
        break