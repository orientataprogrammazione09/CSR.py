print("""
#------------------------------------------------------------------------------- #                   
#nome = CSR.py
#autore = ildruogo08
#stato = beta
#-------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------#
""")

from socket import *                                               #il modulo socket mette in comunicazione i computer

print("benvenuto su CSR")

print("\ninserisci il target:")                                        #qui si definiscono le informazione per la connessione
target = str(input())
print("\ninserisci le porte da scannerizzare:")

print("dalla porta")
porta_i = int(input())
print("\nfino alla porta")
porta_f = int(input())

porte = range(porta_i,porta_f)
                                                                        
for porta in porte:                                                      #qui vado a creare un ciclo for
    s = socket(AF_INET, SOCK_STREAM)                                      #qui creo una connnessione per ogni porta nel range          
    conn = s.connect_ex((target, porta))                                   #qui vado a a usare  il metodo s.connect_ex(()) che è uguale a s.connect ma  se la porta è chiusa ne usa un' altra
    
if conn == 0:                                                            #qui si trova una condizione che significa che se la connessione va a buon fine allora metti a schermo la porta e l'host insieme ad [APERTA]
    print("[APERTA]", str(porta) + ":" , target)

else:
    print("[CHIUSA]", str(porta) + ":" , target)                          #anche qui si trova una condizione che vuol dire che se la porta è chiusa mette a schermo il messaggio
