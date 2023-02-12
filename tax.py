

def calculateTax(suma,dobinda,scop): # "suma" este argument
    """
    argumentul este utilizat pentru a putea fi apelata functia din exterior cu valoarea necesara
    """
    if not suma.isdigit() or type(dobinda) != int:   # verificam daca argumentul este sir numeric
        raise TypeError("Suma introdusa nu este o valoare numerica") # TypeError ne afiseaza eraoare cu mesajul dorit
    suma = int(suma)       
    calcul_impozit =  dobinda / 100 * suma  # formula pentru a calcula procentul
    rezultat = {                            # am ales dictionar fiincdca este mai usor citit si printat
        "suma" : suma,
        "dobinda" : dobinda,
        "scop" : scop,
        "impozit" : calcul_impozit          
    }                                      
    return  print(rezultat)
    """
    "return" returneaza valorile declarate in interiorul functiei
    ce au fost comasate in variabila "rezultat", pe ele le optinem in output.


    """



