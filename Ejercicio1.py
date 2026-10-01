import math

# Si el prototipo pide un diccionario:
donas_dict = {n: (math.sqrt(2)) ** (n - 1) for n in range(1, 11)}

# Si pide una lista por comprension:
donas_lista = [(math.sqrt(2)) ** (n - 1) for n in range(1, 11)]