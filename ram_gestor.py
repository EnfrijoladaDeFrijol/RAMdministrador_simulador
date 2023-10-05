import os
import sys
import random

# -----------------------------------------------

def imprimirTitulo():
    print("""
         ___    _   __  __               _            
        | _ \  /_\ |  \/  |  __ _ ___ __| |_ ___ _ _  
        |   / / _ \| |\/| | / _` / -_|_-<  _/ _ \ '_| 
        |_|_\/_/ \_\_|  |_| \__, \___/__/\__\___/_|   
                            |___/                     
    \t\t\tAutor -> Luis Arturo Meza Sánhcez
    """)
    
def imprimirLinea():
    print("----"*15)

def imprimirDatosRam(ram_total, ram_os,ram_disp):
    print("\n\tRAM total ................................. {}".format(ram_total))
    print("\tRAM usada por el sistema operativo ........ {}".format(ram_os))
    print("\tRAM disponbile ............................ {}".format(ram_disp))
    print()

def imprimirMenu():
    imprimirLinea()
    print("\n\t\tOpciones de gestiòn de RAM\n")
    print("\t\t1. Partciòn estàtica")
    print("\t\t2. Partciòn dinàmica")
    print("\t\t3. Pagianciòn")
    print("\t\t4. Segmentaciòn")
    print("\t\t5. Salir")

def limpiarPantalla(sistema_operativo):
    if (sistema_operativo == "win32"):
        os.system("cls")
    elif (sistema_operativo == "linux" or sistema_operativo == "linux2"):
        os.system("clear")
    elif (sistema_operativo == "darwin"):
        os.system("clear")
    else:
        imprimirLinea()
        imprimirLinea()

# -----------------------------------------------

def solicitarProceso():
    proceso = int(input("\t   Ingresa el tamaño del proceso: "))
    return proceso

# --------- ( PARTIIÓN ESTÁTICA ) --------------------
# Hacemos las particiones de manera aleatoria
# Par esta parte vamos a usar 5 particiones siempre para evitar problemas con esto
def particionEstatica(ram_disp):
    imprimirLinea()
    print("\n\t  P A R T I C I Ó N   E S T Á T I C A")
    print("\t\t  ingresa '0' ṕara salir")
    imprimirLinea()
    print("\n\tRAM disponible ............................ {}\n".format(ram_disp))
    particiones_disp = [ram_disp*0.02,  ram_disp*0.08, ram_disp*0.10, ram_disp*0.25, ram_disp*0.50]

    print("  Particiones disponibles: ",particiones_disp)
    while (len(particiones_disp)>0):
        miProceso = solicitarProceso()
        if (miProceso == 0):
            print("\t[ADVERTENCIA] Saliendo de partición estática")
            break
        if (miProceso > particiones_disp[len(particiones_disp)-1]):
            print(("\n\t[ERROR] EL proceso: ingresado: {} es demasiado grande").format(miProceso))
            
        for i in range(len(particiones_disp)):
            if ((miProceso <= particiones_disp[i]) and (miProceso != 0) ):
                # Obtenemos el indice para borrar esa particion de la lista para simular que ya está ocupada
                # Y esto lo hacemos en cada delete de algún dato porque por lo mismo se redimensiona
                inidice_Proceso = particiones_disp.index(particiones_disp[i])
                del particiones_disp[inidice_Proceso]
                print(("\n\t[MENSAJE] Proceso con tamaño {} asignado con éxito...").format(miProceso))
                print("\n\tParticiones disponibles: ",particiones_disp)
                break
            

    #print("\t\tColocando el proceso...")

# --------- ( PARTIIÓN DINÁMICA ) --------------------
def particionDinamico(ram_disp):
    imprimirLinea()
    print("\n\t   P A R T I C I Ó N   D I N Á M I C A")
    print("\t\t  ingresa '0' ṕara salir")
    imprimirLinea()
    while True:
        print("\n\tRAM disponible ............................ {}\n".format(ram_disp))
        miProceso = solicitarProceso()
        if (miProceso == 0):
            print("\n\t\t[MENSAJE] Saliendo...\n\n")
            break
        elif (miProceso <= ram_disp):
            ram_disp = ram_disp - miProceso
        elif (miProceso > ram_disp):
            print("\n\t[ERROR] Tamaño de proceso sobrepasa la RAM")
            break
        elif (ram_disp == 0):
            print("\n\t[ERROR] Se acabò la memoria RAM")
            break
        else:
            print("\n\t[ADVERTENCIA] Ingrese un valor válido")
            break

# --------- ( SEGMENTACIÒN ) --------------------
def segmentacion(ram_disp):
    imprimirLinea()
    print("\n\t\t S E G M E N T A C I Ò N ")
    imprimirLinea()
    print("\n\tRAM disponible ............................ {}\n".format(ram_disp))
    miProceso = solicitarProceso()
    #print(miProceso)
    if (miProceso <= ram_disp): # En caso de que haya espacio
        datos = miProceso*0.5   # 50%
        codigo = miProceso*0.3  # 30%
        pila = miProceso*0.2    # 20%
        
        # Impresiòn de datos
        print() # NOTA: Arreglar los decimales
        print("\t\tDatos (50%) ...... {}".format(datos))
        print("\t\tCòdigo (30%) ..... {}".format(codigo))
        print("\t\tPila (20%) ....... {}".format(pila))
        print("\t\t------------------------")
        print("\t\tTotal (100%) ...... {}".format(miProceso))
        print()
    else:
        print("\n\t [ADVERTENCIA] Memoria insuficiente")

# ------------ ( PAGINACIÒN ) ------------------
def calcularPaginacion(diferecia_paginacion, num_paginacion):
    num_paginacion = num_paginacion - diferecia_paginacion
    return num_paginacion

def paginacion(ram_disp):
    imprimirLinea()
    print("\n\t\t   P A G I N A C I Ò N \n")
    imprimirLinea()

    while True:
        print("\n\tRAM disponible ............................ {}\n".format(ram_disp))
        print("\t\tOpciones:   2   4   16   32 \n\t\t\t 0 (cancelar)")
        # Pedimos el dato pero lo guardamos como string para tener en cuenta los diferentes errores que 
        # puede llegar a producir y ya despuès lo recasteamos a int para poder operarlo
        division = input("\n\t   Ingresa el tamaño de la divsiiòn: ")
        imprimirLinea()
        if (division == "2" or division == "4" or division == "16" or division == "32"):
            division = int(division) # Aquì casteamos e string a un int para poder operarlo
            num_paginacion = ram_disp/division # 1024 / 16
            while True:
                if (num_paginacion < 0): # Caso proceso introducido excede lo disponibe
                    print("\n\t[ERROR] Es demasiado grande no va a entrar")
                    break
                elif (num_paginacion == 0): # Caso cuando justo se ocupo el espacio exacto
                    print("\n\t\tPaginaciòn disponible: ",num_paginacion)
                    print("\n\t   [ADVERTENCIA] Se acabò la memoria\n")
                    break
                else:          
                    print("\n\t\tPaginaciòn disponible: ",num_paginacion)
                    miProceso = solicitarProceso()
                    diferencia_paginacion = miProceso/division
                    num_paginacion = calcularPaginacion(diferencia_paginacion,num_paginacion)
            break
        elif division == "0":
            break
        else:
            print("\n\t\t[ADVERTENCIA] Opciòn no vàlida\n")
        #miProceso = solicitarProceso()

# -----------------------------------------------

def main():
    sistema_operativo = sys.platform
    limpiarPantalla(sistema_operativo)
    ram_total = 2048
    ram_os = 1024
    ram_disp = ram_total - ram_os
    
    while True:
        imprimirLinea()
        imprimirTitulo()
        imprimirDatosRam(ram_total,ram_os,ram_disp)
        imprimirMenu()
        opc = input("\t\t>> ")

        if opc == "1":
            limpiarPantalla(sistema_operativo)
            particionEstatica(ram_disp)
        elif opc == "2":
            limpiarPantalla(sistema_operativo)
            particionDinamico(ram_disp)
        elif opc == "3":
            limpiarPantalla(sistema_operativo)
            paginacion(ram_disp)
        elif opc == "4": # Segmentaciòn
            limpiarPantalla(sistema_operativo)
            segmentacion(ram_disp)
        elif opc == "5":
            print("\n\t [ADVERTENCIA] Saliendo...")
            break
        else:
            print("\n\t\t[ADVERTENCIA] Opciòn no vàlida...\n\n")

main()