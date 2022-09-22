import cmath



def converte_temperatura(temp_farenheint):
    """ Converte temperatura em Farenheint (ºF) para Celsius (ºC).
    
    O usuário insere a temperatura em Farenheit(ºF).
    Com a fórmula:
    °C = (°F − 32) ÷ 1,8
    a função converte a temperatura para graus Celsius (ºC).
    """
    c = (temp_farenheint - 32) / 1.8
    celsius = round(c, 2)
    return celsius

converte_temperatura(77.2)









    