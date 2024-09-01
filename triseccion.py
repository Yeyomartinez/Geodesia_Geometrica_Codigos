import math as m

def entradadenortesyestes():
    print("Dijite el valor N y E del punto A")
    valor_de_Na = float(input("NORTE(A): "))
    valor_de_Ea = float(input("ESTE(A): "))
    print("Dijite el valor N y E del punto B")
    valor_de_Nb = float(input("NORTE(B): "))
    valor_de_Eb = float(input("ESTE(B): "))
    print("Dijite el valor N y E del punto C")
    valor_de_Nc = float(input("NORTE(C): "))  
    valor_de_Ec = float(input("ESTE(C): "))    
    print("¡Recuerde que los angulos no pueden ser multiplos de 90 CERRADOS!")
    print("Dijite el valor de X")
    valor_de_X_grados = float(input("Ingrese el valor de X en grados= "))
    valor_de_X_minutos = float(input("Ingrese el valor de X en minutos: "))
    valor_de_X_segundos = float(input("Ingrese el valor de X en segundos: "))
    print("Dijite el valor de Y ")
    valor_de_Y_grados = float(input("Ingrese el valor de Y en grados= "))
    valor_de_Y_minutos = float(input("Ingrese el valor de Y en minutos: "))
    valor_de_Y_segundos = float(input("Ingrese el valor de Y en segundos: "))
    print("Dijite el valor de Z ")
    valor_de_Z_grados = float(input("Ingrese el valor de Z en grados= "))
    valor_de_Z_minutos = float(input("Ingrese el valor de Z en minutos: "))
    valor_de_Z_segundos = float(input("Ingrese el valor de Z en segundos: "))
    
    Calculo_de_X_decimal = valor_de_X_grados + valor_de_X_minutos / 60 + valor_de_X_segundos / 3600
    Calculo_de_X_radianes = m.radians(Calculo_de_X_decimal)
    Calculo_de_Y_decimal = valor_de_Y_grados + valor_de_Y_minutos / 60 + valor_de_Y_segundos / 3600
    Calculo_de_Y_radianes = m.radians(Calculo_de_Y_decimal)
    Calculo_de_Z_decimal = valor_de_Z_grados + valor_de_Z_minutos / 60 + valor_de_Z_segundos / 3600
    Calculo_de_Z_radianes = m.radians(Calculo_de_Z_decimal)
    suma_de_angulos = Calculo_de_X_decimal + Calculo_de_Y_decimal + Calculo_de_Z_decimal
    grados_0 = abs(int(suma_de_angulos))
    grados_0_sin_abs = int(suma_de_angulos)
    minutos_dec_0 = (suma_de_angulos - grados_0_sin_abs) * 60
    minutos_0 = abs(int(minutos_dec_0))
    minutos_0_sin_abs = int(minutos_dec_0)
    segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
    visualizacion_ang = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    print("La suma de los angulos son", visualizacion_ang)
    if  719 <= suma_de_angulos <= 721:
        Valor_t = 720
        if suma_de_angulos > Valor_t:
            nivel_confianza = (Valor_t / suma_de_angulos)*100
            visualizacion_confianza = f"{nivel_confianza:.3f}"
        else:
            nivel_confianza = (suma_de_angulos / Valor_t)*100
            visualizacion_confianza = f"{nivel_confianza:.3f}"
        
    elif 359 <= suma_de_angulos <= 361:
        Valor_t = 360
        if suma_de_angulos > Valor_t:
            nivel_confianza = (Valor_t / suma_de_angulos)*100
            visualizacion_confianza = f"{nivel_confianza:.3f}"
        else:
            nivel_confianza = (suma_de_angulos / Valor_t)*100
            visualizacion_confianza = f"{nivel_confianza:.3f}"
        
    else: 
        return suma_de_angulos

    print("Nivel de confianza de las coordenadas E y N con respecto a los ángulos:", visualizacion_confianza, "%")
    
    return valor_de_Na, valor_de_Ea, valor_de_Nb, valor_de_Eb, valor_de_Nc, valor_de_Ec, Calculo_de_X_radianes, Calculo_de_Y_radianes, Calculo_de_Z_radianes

def calculo_cordenadas_punto_p(valor_de_Na, valor_de_Ea, valor_de_Nb, valor_de_Eb, valor_de_Nc, valor_de_Ec, Calculo_de_X_radianes, Calculo_de_Y_radianes, Calculo_de_Z_radianes):
    Ec_Ea = valor_de_Ec - valor_de_Ea
    Eb_Ea = valor_de_Eb - valor_de_Ea
    Ea_Eb = valor_de_Ea - valor_de_Eb
    Ec_Eb = valor_de_Ec - valor_de_Eb
    Eb_Ec = valor_de_Eb - valor_de_Ec
    Ea_Ec = valor_de_Ea - valor_de_Ec
    
    Nc_Na = valor_de_Nc - valor_de_Na
    Nb_Na = valor_de_Nb - valor_de_Na
    Na_Nb = valor_de_Na - valor_de_Nb
    Nc_Nb = valor_de_Nc - valor_de_Nb
    Nb_Nc = valor_de_Nb - valor_de_Nc
    Na_Nc = valor_de_Na - valor_de_Nc

    A_a = m.degrees(m.atan2(Ec_Ea, Nc_Na)) - m.degrees(m.atan2(Eb_Ea, Nb_Na))
    B_b = m.degrees(m.atan2(Ea_Eb, Na_Nb)) - m.degrees(m.atan2(Ec_Eb, Nc_Nb))
    C_c = m.degrees(m.atan2(Eb_Ec, Nb_Nc)) - m.degrees(m.atan2(Ea_Ec, Na_Nc))

    ctg_X = 1 / m.tan(Calculo_de_X_radianes)
    ctg_Y = 1 / m.tan(Calculo_de_Y_radianes)
    ctg_Z = 1 / m.tan(Calculo_de_Z_radianes)
    ctg_Aa = 1 / m.tan(m.radians(A_a))
    ctg_Bb = 1 / m.tan(m.radians(B_b))
    ctg_Cc = 1 / m.tan(m.radians(C_c))
    
    k_1 = 1 / (ctg_Aa - ctg_X)
    k_2 = 1 / (ctg_Bb - ctg_Y)
    k_3 = 1 / (ctg_Cc - ctg_Z)
    
    z = k_1 + k_2 + k_3
    
    Este_p = (k_1 * valor_de_Ea + k_2 * valor_de_Eb + k_3 * valor_de_Ec) / z
    Norte_p = (k_1 * valor_de_Na + k_2 * valor_de_Nb + k_3 * valor_de_Nc) / z
    
    print("Norte en p =", Norte_p)
    print("Este en p =", Este_p)

valor_de_Na, valor_de_Ea, valor_de_Nb, valor_de_Eb, valor_de_Nc, valor_de_Ec, Calculo_de_alpha_radianes, Calculo_de_gamma_radianes, Calculo_de_beta_radianes = entradadenortesyestes()
calculo_cordenadas_punto_p(valor_de_Na, valor_de_Ea, valor_de_Nb, valor_de_Eb, valor_de_Nc, valor_de_Ec, Calculo_de_alpha_radianes, Calculo_de_gamma_radianes, Calculo_de_beta_radianes)
