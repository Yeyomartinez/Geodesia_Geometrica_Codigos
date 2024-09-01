import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
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

def pedir_xyz():
    print("ADVERTENCIA: Una vez los valores sean inscritos no hay retroceso")
    print("X ≠ 0")
    x_entrada = float(input("Ingrese el valor de X= "))
    print("Y ≠ 0")
    y_entrada = float(input("Ingrese el valor de y= "))
   
    z_entrada = float(input("Ingrese el valor de Z= "))
    
    return x_entrada, y_entrada, z_entrada

def calculo_1ra_iteracion(a, e, x_entrada, y_entrada, z_entrada):
    Calculo_phi_1_a = 1 / (1 - e)
    Calculo_phi_1_b = z_entrada / math.sqrt(x_entrada**2 + y_entrada**2)
    Calculo_phi_1 = math.degrees(math.atan(Calculo_phi_1_a * Calculo_phi_1_b))
    Calculo_de_n_1 = a / math.sqrt(1 - e * (math.sin(math.radians(Calculo_phi_1))**2))
    Calculo_de_h_1 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(Calculo_phi_1))) - Calculo_de_n_1
    return Calculo_phi_1, Calculo_de_n_1, Calculo_de_h_1

def calculo_lambda(x_entrada, y_entrada):
    Calculo_lambda_final = math.degrees(math.atan(y_entrada / x_entrada))

    if x_entrada >= 0 and y_entrada >=0:
            calculo_lambda_final_1 = abs(Calculo_lambda_final)
            grados_0 = abs(int(calculo_lambda_final_1))
            grados_0_sin_abs = int(calculo_lambda_final_1)
            minutos_dec_0 = (calculo_lambda_final_1 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_lambda_1 =  f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
            
            print ("Su valor de λ: ", visualizacion_lambda_1, "E")
            
    elif x_entrada <= 0 and y_entrada >=0:
            calculo_lambda_final_1 = 180 - abs(Calculo_lambda_final)
            grados_0 = abs(int(calculo_lambda_final_1))
            grados_0_sin_abs = int(calculo_lambda_final_1)
            minutos_dec_0 = (calculo_lambda_final_1 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_lambda_1 =  f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
            
            print ("Su valor de λ: ", visualizacion_lambda_1, "E")
    elif x_entrada <= 0 and y_entrada <=0:
            calculo_lambda_final_1 = 180 - abs(Calculo_lambda_final)
            grados_0 = abs(int(calculo_lambda_final_1))
            grados_0_sin_abs = int(calculo_lambda_final_1)
            minutos_dec_0 = (calculo_lambda_final_1 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_lambda_1 =  f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
            
            print ("Su valor de λ: ", visualizacion_lambda_1, "W")
    elif x_entrada >= 0 and y_entrada <=0:
            calculo_lambda_final_1 = abs(Calculo_lambda_final)
            grados_0 = abs(int(calculo_lambda_final_1))
            grados_0_sin_abs = int(calculo_lambda_final_1)
            minutos_dec_0 = (calculo_lambda_final_1 - grados_0_sin_abs) * 60
            minutos_0 = abs(int(minutos_dec_0))
            minutos_0_sin_abs = int(minutos_dec_0)
            segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
            visualizacion_lambda_1 =  f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
            
            print ("Su valor de λ: ", visualizacion_lambda_1, "W")
    else:
        return (Calculo_lambda_final)
    return (visualizacion_lambda_1)
    

def calculo_2da_iteracion(calculo_phi_1, Calculo_de_n_1, a, e, x_entrada, y_entrada, z_entrada):
    calculo_phi_2_a = z_entrada + e * Calculo_de_n_1 * math.sin(math.radians(calculo_phi_1))
    calculo_phi_2_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_2 = math.degrees(math.atan(calculo_phi_2_a / calculo_phi_2_b))
    Calculo_de_n_2 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_2))**2))
    Calculo_de_h_2 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_2))) - Calculo_de_n_2
    return calculo_phi_2, Calculo_de_n_2, Calculo_de_h_2

def calculo_3ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_2, Calculo_de_n_2):
    calculo_phi_3_a = z_entrada + e * Calculo_de_n_2 * math.sin(math.radians(calculo_phi_2))
    calculo_phi_3_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_3 = math.degrees(math.atan(calculo_phi_3_a / calculo_phi_3_b))
    Calculo_de_n_3 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_2))**2))
    Calculo_de_h_3 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_2))) - Calculo_de_n_2
    return calculo_phi_3, Calculo_de_n_3, Calculo_de_h_3

def calculo_4ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_3, Calculo_de_n_3):
    calculo_phi_4_a = z_entrada + e * Calculo_de_n_3 * math.sin(math.radians(calculo_phi_3))
    calculo_phi_4_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_4 = math.degrees(math.atan(calculo_phi_4_a / calculo_phi_4_b))
    Calculo_de_n_4 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_3))**2))
    Calculo_de_h_4 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_3))) - Calculo_de_n_3
    return calculo_phi_4, Calculo_de_n_4, Calculo_de_h_4

def calculo_5ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_4, Calculo_de_n_4):
    calculo_phi_5_a = z_entrada + e * Calculo_de_n_4 * math.sin(math.radians(calculo_phi_4))
    calculo_phi_5_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_5 = math.degrees(math.atan(calculo_phi_5_a / calculo_phi_5_b))
    Calculo_de_n_5 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_4))**2))
    Calculo_de_h_5 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_4))) - Calculo_de_n_4
    return calculo_phi_5, Calculo_de_n_5, Calculo_de_h_5

def calculo_6ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_5, Calculo_de_n_5):
    calculo_phi_6_a = z_entrada + e * Calculo_de_n_5 * math.sin(math.radians(calculo_phi_5))
    calculo_phi_6_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_6 = math.degrees(math.atan(calculo_phi_6_a / calculo_phi_6_b))
    Calculo_de_n_6 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_5))**2))
    Calculo_de_h_6 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_5))) - Calculo_de_n_5
    return calculo_phi_6, Calculo_de_n_6, Calculo_de_h_6

def imprimir_resultados(calculo_phi_6, Calculo_de_h_6):
    grados_0 = abs(int(calculo_phi_6))
    grados_0_sin_abs = int(calculo_phi_6)
    minutos_dec_0 = (calculo_phi_6 - grados_0_sin_abs) * 60
    minutos_0 = abs(int(minutos_dec_0))
    minutos_0_sin_abs = int(minutos_dec_0)
    segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
    visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
    if calculo_phi_3 >= 0:
        print("Su valor de φ:", visualizacion_phi, "N")
    elif calculo_phi_3 <= 0:
        print("Su valor de φ:", visualizacion_phi, "S")
    else:
        print("Su valor de φ:", visualizacion_phi, "ECUADOR")
    
    visualizacion_H = f"{Calculo_de_h_6:.4f}"
    print("Su valor de H (altura sobre el nivel del mar):", visualizacion_H, "M")
    
    return (visualizacion_phi)

def graficar_coordenadas(a, e, x_entrada, y_entrada, z_entrada, visualizacion_phi, visualizacion_lambda_1, Calculo_de_h_6):
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

    ax.quiver(0, 0, 0, x_entrada, y_entrada, z_entrada, color='#800080', label=f'Direccion de φ: {visualizacion_phi}', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, x_entrada, y_entrada, 0, color='black', label=f'Dirección de λ: {visualizacion_lambda_1}', arrow_length_ratio=0.1)
    vector_altura = np.array([x_entrada, y_entrada, z_entrada]) * 1/4
    ax.quiver(x_entrada, y_entrada, z_entrada, vector_altura[0], vector_altura[1], vector_altura[2], color='b', label=f'Altura sobre el nivel del mar: {Calculo_de_h_6}', arrow_length_ratio=0.1)
    ax.text(x_entrada, y_entrada, z_entrada, f'φ = {visualizacion_phi}\nλ = {visualizacion_lambda_1}', color='black', fontsize=7)
    ax.set_xlabel('X')
    ax.set_ylabel('y')
    ax.set_zlabel('Z')
    ax.legend()
    
    plt.show()

a, e = elipsoides()
x_entrada, y_entrada, z_entrada = pedir_xyz()
calculo_phi_1, Calculo_de_n_1, Calculo_de_h_1 = calculo_1ra_iteracion(a, e, x_entrada, y_entrada, z_entrada)
calculo_phi_2, Calculo_de_n_2, Calculo_de_h_2 = calculo_2da_iteracion(calculo_phi_1, Calculo_de_n_1, a, e, x_entrada, y_entrada, z_entrada)
calculo_phi_3, Calculo_de_n_3, Calculo_de_h_3 = calculo_3ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_2, Calculo_de_n_2)
calculo_phi_4, Calculo_de_n_4, Calculo_de_h_4 = calculo_4ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_3, Calculo_de_n_3)
calculo_phi_5, Calculo_de_n_5, Calculo_de_h_5 = calculo_5ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_4, Calculo_de_n_4)
calculo_phi_6, Calculo_de_n_6, Calculo_de_h_6 = calculo_6ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_5, Calculo_de_n_5)
visualizacion_lambda_1 = calculo_lambda(x_entrada, y_entrada)
visualizacion_phi=imprimir_resultados(calculo_phi_6, Calculo_de_h_6)
graficar_coordenadas(a, e, x_entrada, y_entrada, z_entrada, visualizacion_phi, visualizacion_lambda_1, Calculo_de_h_6)