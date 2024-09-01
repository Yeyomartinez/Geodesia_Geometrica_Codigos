"""Jair Cruz"""
import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

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

def seleccionar_phi_1():
    print("DIJITE SU RESPECTIVO φ₁ y λ₁")
    Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
    valor_phi_1_grados = float(input("Ingrese el valor de φ₁ en grados: "))
    valor_phi_1_minutos = float(input("Ingrese el valor de φ₁ en minutos: "))
    valor_phi_1_segundos = float(input("Ingrese el valor de φ₁ en segundos: "))
    
    Calculo_de_phi_decimal = valor_phi_1_grados + valor_phi_1_minutos/60 + valor_phi_1_segundos/3600
    
    if Seleccionar_norte_sur == 1:
        resultado_ns = Calculo_de_phi_decimal * 1
    elif Seleccionar_norte_sur == 2:
        resultado_ns = Calculo_de_phi_decimal * -1
    else:
        print("NO VALIDO")
        
    resultado_phi_rad_1= m.radians (resultado_ns)
        
    return (resultado_phi_rad_1)

def seleccionar_lambda_1():
    Seleccionar_lambda_e_w = int(input("Seleccione (1) si su longitud es ESTE, o a su vez seleccione (2) si su longitud es WEST: "))
    valor_lambda_grados = float(input("Ingrese el valor de λ₁ en grados: "))
    valor_lambda_minutos = float(input("Ingrese el valor de λ₁ en minutos: "))
    valor_lambda_segundos = float(input("Ingrese el valor de λ₁ en segundos: "))
    
    Calculo_de_lambda_decimal_1 = valor_lambda_grados + valor_lambda_minutos/60 + valor_lambda_segundos/3600
    
    if Seleccionar_lambda_e_w == 1:
        resultado_ew = Calculo_de_lambda_decimal_1 * 1
    elif Seleccionar_lambda_e_w == 2:
        resultado_ew = Calculo_de_lambda_decimal_1 * -1
    else:
        print("NO VALIDO")
        
    resultado_lambda_1 = resultado_ew
        
    return (resultado_lambda_1)

def seleccionar_phi_2():
    print("DIJITE SU RESPECTIVO φ₂ y λ₂")
    Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
    valor_phi_2_grados = float(input("Ingrese el valor de φ₂ en grados: "))
    valor_phi_2_minutos = float(input("Ingrese el valor de φ₂ en minutos: "))
    valor_phi_2_segundos = float(input("Ingrese el valor de φ₂ en segundos: "))
    
    Calculo_de_phi_decimal = valor_phi_2_grados + valor_phi_2_minutos/60 + valor_phi_2_segundos/3600
    
    if Seleccionar_norte_sur == 1:
        resultado_ns = Calculo_de_phi_decimal * 1
    elif Seleccionar_norte_sur == 2:
        resultado_ns = Calculo_de_phi_decimal * -1
    else:
        print("NO VALIDO")
        
    resultado_phi_rad_2= m.radians (resultado_ns)
        
    return (resultado_phi_rad_2)

def seleccionar_lambda_2():
    Seleccionar_lambda_e_w = int(input("Seleccione (1) si su longitud es ESTE, o a su vez seleccione (2) si su longitud es WEST: "))
    valor_lambda_grados = float(input("Ingrese el valor de λ₂ en grados: "))
    valor_lambda_minutos = float(input("Ingrese el valor de λ₂ en minutos: "))
    valor_lambda_segundos = float(input("Ingrese el valor de λ₂ en segundos: "))
    
    Calculo_de_lambda_decimal_2 = valor_lambda_grados + valor_lambda_minutos/60 + valor_lambda_segundos/3600
    
    if Seleccionar_lambda_e_w == 1:
        resultado_ew = Calculo_de_lambda_decimal_2 * 1
    elif Seleccionar_lambda_e_w == 2:
        resultado_ew = Calculo_de_lambda_decimal_2 * -1
    else:
        print("NO VALIDO")
        
    resultado_lambda_2 = resultado_ew
        
    return (resultado_lambda_2)

def calculo_de_area(resultado_phi_rad_1, resultado_lambda_1, resultado_phi_rad_2,resultado_lambda_2,a , e  ):
    b = a**2 * (1-e)
    x = 1/2
    parte_1 = m.sin(resultado_phi_rad_2)/(1-e*(m.sin(resultado_phi_rad_2))**2)
    parte_2 = x * 1/m.sqrt(e)
    parte_3 = m.log ((1 + m.sqrt(e) * m.sin(resultado_phi_rad_2))/(1 - m.sqrt(e) * m.sin(resultado_phi_rad_2)))
    evalucion_primer_phi2 = parte_1 + parte_2 * parte_3
    parte_1_1 = m.sin(resultado_phi_rad_1)/(1-e*(m.sin(resultado_phi_rad_1))**2)
    parte_2_1= x * 1/m.sqrt(e)
    parte_3_1 = m.log ((1 + m.sqrt(e) * m.sin(resultado_phi_rad_1))/(1 - m.sqrt(e) * m.sin(resultado_phi_rad_1)))
    evalucion_primer_phi1 = parte_1_1 + parte_2_1 * parte_3_1
    if resultado_lambda_2 < 0 :
      resultado_lambda_2_c = abs(resultado_lambda_2) + 180
    else:
        resultado_lambda_2_c = resultado_lambda_2
        
    if resultado_lambda_1 < 0 :
        resultado_lambda_1_c = abs(resultado_lambda_1) + 180
    else :
        resultado_lambda_1_c = resultado_lambda_1
    res_2_rad = m.radians(resultado_lambda_2_c)
    res_1_rad = m.radians(resultado_lambda_1_c)
    delta_lambda = x*b*(res_2_rad - res_1_rad )
    delta_phi = (evalucion_primer_phi2 -evalucion_primer_phi1 )
    calculo_A = abs(delta_lambda * delta_phi)
    print("El calculo del area designada es = ", calculo_A/1e6, "km²")
    print("El calculo del area designada es = ", calculo_A, "m²")
   
    n = 10000
    e_1 = m.sqrt (e)
    Serie_de_yeyo = pd.Series([((i * e_1**(2*(i-1))) / (2*i - 1)) for i in range(n)])
    b_2 = a**2 * (1-e)
    suma = Serie_de_yeyo.sum()
    Area_total = m.pi*4*b_2*suma
   
    print("El calculo del area superficial del elipsoide designado es = ", Area_total/1e6, "km²")
    print("El calculo del area superficial del elipsoide designado es = ", Area_total, "m²")
    
    volumen_elipsoide = 4/3 * m.pi * a**2 * m.sqrt(b_2)
    
    print("El calculo del volumen superficial del elipsoide designado es = ", volumen_elipsoide/1e9, "km³")
    print("El calculo del volumen superficial del elipsoide designado es = ", volumen_elipsoide, "m³")

def calculo_coordendas_1_xyz (a, e, resultado_phi_rad_1, resultado_lambda_1):
    calculo_N_1 =  a / m.sqrt(1 - e * (m.sin(resultado_phi_rad_1)**2))
    calculo_x_1 = (calculo_N_1 )*m.cos(resultado_phi_rad_1)*m.cos(m.radians(resultado_lambda_1))
    calculo_y_1 = (calculo_N_1)*m.cos(resultado_phi_rad_1)*m.sin(m.radians(resultado_lambda_1))
    
    calculo_z_1 = (calculo_N_1*(1-e))*m.sin(resultado_phi_rad_1)
    
    return(calculo_x_1,calculo_y_1,calculo_z_1,calculo_N_1 )

def calculo_coordendas_2_xyz (a, e, resultado_phi_rad_2, resultado_lambda_2):
    calculo_N_2 =  a / m.sqrt(1 - e * (m.sin(resultado_phi_rad_2)**2))
    calculo_x_2 = (calculo_N_2 )*m.cos(resultado_phi_rad_2)*m.cos(m.radians(resultado_lambda_2))
    calculo_y_2 = (calculo_N_2)*m.cos(resultado_phi_rad_2)*m.sin(m.radians(resultado_lambda_2))
    calculo_z_2 = (calculo_N_2*(1-e))*m.sin(resultado_phi_rad_2)
    return(calculo_x_2,calculo_y_2,calculo_z_2,calculo_N_2)

def graficar_coordenadas(a, e, calculo_x_1, calculo_y_1, calculo_z_1, calculo_x_2, calculo_y_2, calculo_z_2):
    phi = np.linspace(-np.pi/2, np.pi/2, 100)
    lambda_0 = np.linspace(0, 2*np.pi, 100)
    phi, lambda_0 = np.meshgrid(phi, lambda_0)
    r = a / np.sqrt(1 - e * np.sin(phi)**2)

    x = r * np.cos(phi) * np.cos(lambda_0)
    y = r * np.cos(phi) * np.sin(lambda_0)
    z = r * np.sin(phi)
    
    figura_elipse = plt.figure()
    ax = figura_elipse.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='#E6E6FA', alpha=0.3, linewidth=0, antialiased=False)
    
    b = a * np.sqrt(1 - e)
    theta_eq = 0
    x_eq = a * np.cos(theta_eq) * np.cos(phi)
    y_eq = b * np.cos(theta_eq) * np.sin(phi)
    z_eq = np.zeros_like(phi)
    ax.plot(x_eq.flatten(), y_eq.flatten(), z_eq.flatten(), color='black', alpha=0.2)
    x_eq_back = -x_eq
    y_eq_back = y_eq
    z_eq_back = z_eq
    ax.plot(x_eq_back.flatten(), y_eq_back.flatten(), z_eq_back.flatten(), color='black', alpha=0.2)
    phi_mer = 0
    x_mer = a * np.cos(lambda_0) * np.cos(phi_mer)
    y_mer = b * np.cos(lambda_0) * np.sin(phi_mer)
    z_mer = b * np.sin(lambda_0)
    ax.plot(x_mer.flatten(), y_mer.flatten(), z_mer.flatten(), color='black', alpha=0.2 )
    x_mer_back = -x_mer
    y_mer_back = y_mer
    z_mer_back = z_mer
    ax.plot(x_mer_back.flatten(), y_mer_back.flatten(), z_mer_back.flatten(), color='black', alpha=0.2)
    puntos_cardinales = {
        'Este': (0, a * np.sqrt(1 - e), 0),
        'Oeste': (0, -a * np.sqrt(1 - e), 0),
        'Norte': (0, 0, a * np.sqrt(1 - e)),
        'Sur': (0, 0, -a * np.sqrt(1 - e))
    }
    for nombre, punto in puntos_cardinales.items():
        ax.scatter(*punto, color='black', s=20)
        ax.text(punto[0], punto[1], punto[2], nombre, color='black', fontsize=6.5, zorder=1)
        

    ax.scatter(calculo_x_1, calculo_y_1, calculo_z_1, color='red', s=40, label='Punto 1')
    ax.scatter(calculo_x_2, calculo_y_2, calculo_z_2, color='blue', s=40, label='Punto 2')
    
    ax.plot([calculo_x_1, calculo_x_2], [calculo_y_1, calculo_y_1], [calculo_z_1, calculo_z_1], color='green', linewidth=2)
    ax.plot([calculo_x_2, calculo_x_2], [calculo_y_1, calculo_y_2], [calculo_z_2, calculo_z_2], color='green', linewidth=2)
    ax.plot([calculo_x_2, calculo_x_1], [calculo_y_2, calculo_y_2], [calculo_z_2, calculo_z_2], color='green', linewidth=2)
    ax.plot([calculo_x_1, calculo_x_1], [calculo_y_2, calculo_y_1], [calculo_z_1, calculo_z_1], color='green', linewidth=2)
    
    plt.legend()
    plt.show()
        


a, e = elipsoides()
resultado_phi_rad_1 = seleccionar_phi_1()
resultado_lambda_1 = seleccionar_lambda_1()
resultado_phi_rad_2 = seleccionar_phi_2()
resultado_lambda_2 = seleccionar_lambda_2()
calculo_de_area(resultado_phi_rad_1, resultado_lambda_1, resultado_phi_rad_2,resultado_lambda_2,a , e  )
calculo_x_1,calculo_y_1,calculo_z_1,calculo_N_1  = calculo_coordendas_1_xyz (a, e, resultado_phi_rad_1, resultado_lambda_1)
calculo_x_2,calculo_y_2,calculo_z_2,calculo_N_2 = calculo_coordendas_2_xyz (a, e, resultado_phi_rad_2, resultado_lambda_2)
graficar_coordenadas(a, e, calculo_x_1, calculo_y_1, calculo_z_1, calculo_x_2, calculo_y_2, calculo_z_2)
"""Jair Cruz"""
