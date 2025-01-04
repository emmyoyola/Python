### Módulos ###
    # Acceder a otros ficheros

# Accede a todas las fn del fichero
import mi_modulo

mi_modulo.sumValue(1, 3, 4)
mi_modulo.printValue("Hola")

# Accede a una(varias) fn específica del fichero
from mi_modulo import sumValue, printValue

sumValue(2, 3, 4)

import math

print(math.pi)
print(math.pow(2, 8))
