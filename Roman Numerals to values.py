rom = 'MCMXCIV'

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

lista = list(rom)
val = 0

for i in range(len(lista)):
    if i < len(lista) - 1 and values[lista[i]] < values[lista[i + 1]]:
        val -= values[lista[i]]
    else:
        val += values[lista[i]]

print(val)