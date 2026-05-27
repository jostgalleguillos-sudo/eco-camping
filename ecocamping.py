print("Gestion de Eco-campin 'Bosque Vivo")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENÚ DE CONTROL DE REGISTRO")
    print("1.- Ver sitios disponibles")
    print("2.- Registro de nuevos vehiculos en el sitio(Entrada)")
    print("3.- Registro de salida de vehiculos(Salida)")
    print("4.- Estado actual del campin")
    print("5.- Salir")
    try:
        opcion =int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida, por favor seleccione entre 1 y 5")
        continue
    
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitios libres para recibir vehiculos: {disponibles}")
    elif opcion == 2:
        sitio_libres = capacidad_maxima - sitios_ocupados
        if sitio_libres == 0:
            print("Lo sentimos no quedan espacios en el camping")
        else:
            try:
                ingreso = int(input("¿cúantos sitios o vehiculos van a ingresar?"))
                if ingreso <= 0:
                    print("Error la cantidad de ingreso debe ser mayor a 0")
                elif ingrso > sitio_libres:
                    print(f"Solo puede ingresar unmaximo de {sitio_libres} sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"Ingreso registrado, se han ocupado {ingreso} de sitios")
            except ValueError:
                print("Error: debe ingresar un numero valido")
    else:
        print("Opcion fuera rango")
