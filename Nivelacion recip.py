import math as m 
def elipsoides():
    print("Seleccione el elipsoide a utilizar:")
    print("1) Internacional (1924)")
    print("2) GRS - 80")
    print("3) WGS - 84")
    print("4) Airy (1830)")
    print("5) Bessel (1841)")
    print("6) Clarke (1866)")
    print("7) Everest (1830)")
    print("8) Hayford (1910)")
    print("9) Krassovsky (1940)")
    print("10) WGS - 72")
    
    Seleccionar_variable = int(input("Ingrese el número correspondiente al elipsoide: "))
    
    if Seleccionar_variable == 1:
        a = 6378388.0
        e = 0.00672267002278908
    elif Seleccionar_variable == 2:
        a = 6378137.0
        e = 0.00669438002290
    elif Seleccionar_variable == 3:
        a = 6378137.0
        e = 0.006694379990
    elif Seleccionar_variable == 4:
        a = 6377563.396
        e = 0.00667054004120
    elif Seleccionar_variable == 5:
        a = 6377397.155
        e = 0.006674372229629
    elif Seleccionar_variable == 6:
        a = 6378206.4
        e = 0.006768658
    elif Seleccionar_variable == 7:
        a = 6377276.345
        e = 0.006637847
    elif Seleccionar_variable == 8:
        a = 6378388.0
        e = 0.00672267002278908
    elif Seleccionar_variable == 9:
        a = 6378245.0
        e = 0.006693421622965943
    elif Seleccionar_variable == 10:
        a = 6378135.0
        e = 0.006694318
    else:
        print("OPCIÓN NO VÁLIDA")
    
    return a, e
def entradadevariables():
    valor_de_alpha_grados = float(input("Ingrese el valor de α en grados: "))
    valor_de_alpha_minutos = float(input("Ingrese el valor de α en minutos: "))
    valor_de_alpha_segundos = float(input("Ingrese el valor de α en segundos: "))
    Distancia = float(input("Ingrese el valor de S: "))
    valor_de_z1_grados = float(input("Ingrese el valor de z1 en grados: "))
    valor_de_z1_minutos = float(input("Ingrese el valor de z1 en minutos: "))
    valor_de_z1_segundos = float(input("Ingrese el valor de z1 en segundos: "))
    valor_de_z2_grados = float(input("Ingrese el valor de z2 en grados: "))
    valor_de_z2_minutos = float(input("Ingrese el valor de z2 en minutos: "))
    valor_de_z2_segundos = float(input("Ingrese el valor de z2 en segundos: "))
    Valor_H1 = float(input("Ingrese el valor de la cota 1: "))
    Calculo_de_alpha_decimal = valor_de_alpha_grados + valor_de_alpha_minutos/60 + valor_de_alpha_segundos/3600
    Calculo_de_alpha_radianes = m.radians(Calculo_de_alpha_decimal)
    Calculo_de_z1_decimal = valor_de_z1_grados + valor_de_z1_minutos/60 + valor_de_z1_segundos/3600
    Calculo_de_z1_radianes = m.radians(Calculo_de_z1_decimal)
    Calculo_de_z2_decimal = valor_de_z2_grados + valor_de_z2_minutos/60 + valor_de_z2_segundos/3600
    Calculo_de_z2_radianes = m.radians(Calculo_de_z2_decimal)
    return (Calculo_de_alpha_radianes,Calculo_de_z1_radianes, Calculo_de_z2_radianes,Valor_H1, Distancia) 

def Calculos_Niv (Calculo_de_alpha_radianes, Calculo_de_z1_radianes, Calculo_de_z2_radianes, a, e,Valor_H1,Distancia):
    calculo_N =  a / m.sqrt(1 - e * (m.sin(Calculo_de_alpha_radianes)**2))
    calculo_p = a*(1-e)/(1 - e * (m.sin(Calculo_de_alpha_radianes)**2))**(3/2)
    Calculo_P_aplha_1 = (calculo_N*calculo_p) 
    Calculo_P_aplha_2 = (calculo_N*((m.cos(Calculo_de_alpha_radianes)**2)) +  calculo_p*((m.sin(Calculo_de_alpha_radianes)**2)))
    Calculo_P_final = Calculo_P_aplha_1/Calculo_P_aplha_2
    A = 1 + Valor_H1/Calculo_P_final
    Comp_B = m.tan((Calculo_de_z2_radianes-Calculo_de_z1_radianes)/2)
    Como_B_1 = Comp_B/Calculo_P_final*2
    B = 1 + Distancia*(Como_B_1)
    C = 1 + (Distancia**2)/(Calculo_P_final**2)*12
    H2 = Distancia*Comp_B*A*B*C
    Cota_final_1 = H2 + Valor_H1
    Cota_final_2 = Valor_H1 - H2
    print ("el valor de H2 =", Cota_final_1)
    print ("el valor de H1 =", Cota_final_2)
    
a,e = elipsoides()
Calculo_de_alpha_radianes,Calculo_de_z1_radianes, Calculo_de_z2_radianes,Valor_H1,Distancia =entradadevariables()
Calculos_Niv (Calculo_de_alpha_radianes, Calculo_de_z1_radianes, Calculo_de_z2_radianes, a, e,Valor_H1,Distancia)
    