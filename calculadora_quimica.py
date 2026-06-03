import re
from masas_elementos import masas
from scipy.constants import Avogadro
nombre_unidades={
    "1":"gramos",
    "2":"moles",
    "3":"moleculas"
}

def compuesto_masa_molar(compuesto):
    valores=re.findall(r"\d+|[A-Z][a-z]|[A-Z]",compuesto)
    molar={}
    for index,elemento in enumerate(valores):       
        if elemento.isdigit() is True:
            elemento_anterior=valores[index-1]
            molar[elemento_anterior]=masas[elemento_anterior]*int(elemento)
        else: 
            molar[elemento]=masas[elemento]
    suma=0
    for elemento,masa in molar.items():
            suma+=masa                    
    return suma

while True:
    print("\n¿Qué quieres hacer?")
    print("1 - Calcular masa molar de un compuesto")
    print("2 - Convertir unidades (gramos,moles,moléculas)")
    print("3 - Salir")
    
    opcion=input("\nElige una opcion: ")
    if opcion == "1":
        try:
            print("\nCalculadora de masa molar de un compuesto")
            compuesto=input("Ingrese un compuesto: ") 
            
            resultado=compuesto_masa_molar(compuesto)
                
            print(f"\nMasa molar de {compuesto}: {resultado} g/mol")
            
        except (ValueError,KeyError)  : 
            print("Valor incorrecto vuelva a intentar")
        
    elif opcion == "2":
        try:
            compuesto=input("Ingrese un compuesto para convertir: ")   
            
            masa_molar=compuesto_masa_molar(compuesto)
            
            cantidad=float(input("Qué cantidad: ")) 
            
            
            print("¿Qué unidad tienes?")
            print("1 - Gramos")
            print("2 - Moles")
            print("3 - Moléculas")
            
            unidad=input("Elige un numero: ")
            
            print("¿A qué unidad lo quieres convertir?")
            print("1 - Gramos")
            print("2 - Moles")
            print("3 - Moléculas")
            
            conversion=input("Elige un numero: ")
            
            unidades={
                "1":cantidad/masa_molar,
                "2":cantidad,
                "3":cantidad/Avogadro
            }
            
            cantidad_moles=unidades[unidad]
            conversiones={
                "1":cantidad_moles*masa_molar,
                "2":cantidad_moles,
                "3":cantidad_moles*Avogadro
            }
            
            
            print(f"\n{cantidad} {nombre_unidades[unidad]} convertido en {nombre_unidades[conversion]}: {conversiones[conversion]:.4f}")
        except(ValueError,KeyError):
            print("Compuesto inválido o opción incorrecta")   
            
    elif opcion == "3":
        break
    else:
        print("Opción invalida, vuelva a elegir")