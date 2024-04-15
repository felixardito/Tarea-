#crear un diccionario con el nombre de 10 companeros de clase y sus calificaciones
dic={"clara":10,
     "jazmin":9,
     "matias":8,
     "jovany":6,
     "angel":8,
     "samantha":5,
     "denisse":9,
     "mario":10,
     "marlen":7,
     "joel":8
     }
print(dic)

#crear una funcion para agregar diccionarios a una lista
mi={
    "id":1,
    "nombre":"lapiz",
    "precio":2.00,
    "cantidad":100
}
lista1=[]
lista1.append(mi)

def agregar_producto(lista,id,nombre,precio,cantidad):
    dicc={
        "id":id,
        "nombre":nombre,
        "precio":precio,
        "cantidad":cantidad
    }
    lista.append(dicc)
agregar_producto(lista1,2,"cuaderno",1.50,90)
print(lista1)