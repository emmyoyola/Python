import pandas as pd
import numpy as np

pop = pd.Series([132.2423, 12.346, 85.648, 13.466, 38.744])
print(pop)
pop.name = 'Population in millions'
print(pop)
print(pop.dtype)
print(pop.values)
print(type(pop.values))
print(pop.index)
pop.index = ['Canada', 'France', 'Germany', 'Italy', 'Japan']
print(pop.index)
print(pop[4])
print(pop['Italy'])
print(pop)

pop2 = pd.Series([23.434, 122.332, 95.836, 84.917],
        index=['Col', 'Bra', 'Ven', 'Ecu'],
        name = 'Population South')
print(pop2)

pop3 = pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')
print(pop3)
print(pop3.iloc[-1])
print(pop3[-1])
print(pop3['United States'])
print(pop3[0:3])    # No imprime el índice 3
print(pop3.iloc[0:3])   # No imprime el índice 3
print(pop3['Canada':'Italy'])   # Iprime Italy
print(pop3.iloc[[0,3]])     # Para crear una nueva serie

print(pop3 > 70)
print(pop3[pop3 > 70])
print(pop3.mean())
print(pop3.std())
print(pop3 * 1_000_000)
print(np.log(pop3))
print(pop3['France': 'Italy'].mean())
pop3[pop3 < 70] = 99.99
pop3['Canada'] = 40.5
print(pop3)


