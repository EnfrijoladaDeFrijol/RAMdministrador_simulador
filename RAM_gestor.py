def imprimirTitulo():
    print("""
.    ___    _   __  __               _            
    | _ \  /_\ |  \/  |  __ _ ___ __| |_ ___ _ _  
    |   / / _ \| |\/| | / _` / -_|_-<  _/ _ \ '_| 
    |_|_\/_/ \_\_|  |_| \__, \___/__/\__\___/_|   
                        |___/                     
    """)
    
def imprimirLinea():
    print("----"*15)
    
# -----------------------------------------------


    
def main():
    imprimirLinea()
    imprimirTitulo()
    imprimirLinea()
    
    ram_total = 2048
    ram_os = 1024
    ram_disp = ram_total - ram_os
    
    print(ram_disp)

main()