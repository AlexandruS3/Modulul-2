

def calculateTax(suma): # "suma" este argument
    """
    argumentul este utilizat pentru a putea fi apelata functia din exterior cu valoarea necesara
    """
    if not suma.isdigit():   # verificam daca argumentul este sir numeric
        raise TypeError("Suma introdusa nu este o valoare numerica") # TypeError ne afiseaza eraoare cu mesajul dorit
    suma = int(suma)    
    dobinda = 20      # procent 
    scop = "salariu"          
    calcul_impozit =  dobinda / 100 * suma  # formula pentru a calcula procentul
    rezultat = {                            # am ales dictionar fiincdca este mai usor citit si printat
        "suma" : suma,
        "dobinda" : dobinda,
        "scop" : scop,
        "impozit pe venit" : calcul_impozit          
    }                                      
    return  print(rezultat)
    """
    "return" returneaza valorile declarate in interiorul functiei
    ce au fost comasate in variabila "rezultat", pe ele le optinem in output.


    """



