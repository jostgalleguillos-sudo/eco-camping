def mostrar_opciones():
    print("===Menú Principal===")
    print("1. Unidades por tipos de arreglo ")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("======")

def leer_opcion():
    try:
        opcion = int(input("Seleccione una opcion: "))
        return opcion
        except ValueError:
            return -1
def unidades_tipo(tipo):
    ramo,RAMO = input("ingrese nombre del arreglo floral: ")
    tipo_arre = input("ingrese su tipo de arreglo: ")
    color_principal = input("seleccione tipo de color: ")
    tamaño = ("ingrese tamaño del arreglo: (S-M o L")
    temporada= ("temporada de arreglo: ")
    incluye_tarjeta = ("desea tarjeta dedicatoria (s-n): ")
    if not validar_ramo,RAMO(ramo,RAMO):
        print("[error]: debe seleciconar un nombre valido")
        return
    if not validar_tipo(tipo_arre):
        print("debe seleccionar una opcion valida")
        return
    if not validar_color(color_principal):
        print("debe seleccionar una opcion valida")
        return
    if not validar_tamaño(tamaño):
        print("debe seleccionar una opcion valida")
        return
    if not validar_temp(temporada):
        print("debe seleccionar una opcion valida")
        return
if opc == "2":
    print("ingrese el precio del arreglo: ")
    int(input("minimo: ")
    if minimo == "0":
        if not == "0"
    int(input("maximo: ")
    if maximo == 
    print("los arreglos encontrados son: []")
if opc == "3":
    print("quiere actualizar el precio?: ")
if opc = "4":

if opc = "5":

    if opc= "6":
