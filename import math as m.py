import math as m

def entradadenortesyestes():
    print("Dijite el valor N y E del punto A")
    valor_de_Na = float(input("NORTE(A): "))
    valor_de_Ep = float(input("ESTE(A): "))
    print("Dijite el valor N y E del punto B")
    valor_de_Nb = float(input("NORTE(B): "))
    valor_de_Eb = float(input("ESTE(B): "))
    print("Dijite el valor de α")
    valor_de_alpha_grados = float(input("Ingrese el valor de α en grados: "))
    valor_de_alpha_minutos = float(input("Ingrese el valor de α en minutos: "))
    valor_de_alpha_segundos = float(input("Ingrese el valor de α en segundos: "))
    print("Dijite el valor de β")
    valor_de_beta_grados = float(input("Ingrese el valor de β en grados: "))
    valor_de_beta_minutos = float(input("Ingrese el valor de β en minutos: "))
    valor_de_beta_segundos = float(input("Ingrese el valor de β en segundos: "))

    Calculo_de_alpha_decimal = valor_de_alpha_grados + valor_de_alpha_minutos/60 + valor_de_alpha_segundos/3600
    Calculo_de_alpha_radianes = m.radians(Calculo_de_alpha_decimal)
    Calculo_de_beta_decimal = valor_de_beta_grados + valor_de_beta_minutos/60 + valor_de_beta_segundos/3600
    Calculo_de_beta_radianes = m.radians(Calculo_de_beta_decimal)

    return (
        valor_de_Na, valor_de_Ep, valor_de_Nb, valor_de_Eb,
        Calculo_de_alpha_radianes, Calculo_de_beta_radianes,
        Calculo_de_alpha_decimal, Calculo_de_beta_decimal
    )

def calculo_cordenadas_punto_p(
    valor_de_Na, valor_de_Ep, valor_de_Nb, valor_de_Eb,
    Calculo_de_alpha_radianes, Calculo_de_beta_radianes,
    Calculo_de_alpha_decimal, Calculo_de_beta_decimal
):
    """hiang = abs(Calculo_de_alpha_decimal - Calculo_de_beta_decimal)
    delta = 180 - (Calculo_de_alpha_decimal + Calculo_de_beta_decimal)"""
    print("Método 1")
    ctg_alpha = 1 / m.tan(Calculo_de_alpha_radianes)
    ctg_beta = 1 / m.tan(Calculo_de_beta_radianes)
    z = ctg_alpha + ctg_beta

    Este_p = (valor_de_Ep * z + valor_de_Nb - valor_de_Na - valor_de_Eb*ctg_alpha)/ctg_beta
    
    print("Este en p =", Este_p)
(
    valor_de_Na, valor_de_Ea, valor_de_Nb, valor_de_Eb,
    Calculo_de_alpha_radianes, Calculo_de_beta_radianes,
    Calculo_de_alpha_decimal, Calculo_de_beta_decimal
) = entradadenortesyestes()

calculo_cordenadas_punto_p(
    valor_de_Na, valor_de_Ea, valor_de_Nb, valor_de_Eb,
    Calculo_de_alpha_radianes, Calculo_de_beta_radianes,
    Calculo_de_alpha_decimal, Calculo_de_beta_decimal)