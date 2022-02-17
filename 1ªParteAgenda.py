try:
    fdatos= open("Contactos.txt")
except :
    fdatos=open("Contactos.txt","w")
    Contacto=(input("Nombre del contacto"))
    Numero=(input("Numero del contacto"))
    fdatos.write(Contacto,"-----",Numero)
    fdatos.close()
    fdatos=open("Contactos","r")
    pass
Contacto=(input("Nombre del contacto"))
    Numero=int(input("Numero del contacto"))
    fdatos.write(Contacto,"-----",Numero)