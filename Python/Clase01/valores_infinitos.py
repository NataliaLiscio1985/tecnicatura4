import math
from decimal import Decimal
# manejo de valores infinitos
infinito_positivo = float ('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f'es Infinito?: {math.isinf(infinito_positivo)}')

# manejo de valores infinitos
infinito_negativo = float ('-inf')
print(f'Infinito positivo: {infinito_negativo}')
print(f'es Infinito?: {math.isinf(infinito_negativo)}')

# modulo math
infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'es Infinito?: {math.isinf(infinito_positivo)}')

# modulo math
infinito_negativo = -math.inf
print(f'Infinito positivo: {infinito_negativo}')
print(f'es Infinito?: {math.isinf(infinito_negativo)}')

# modulo decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'es Infinito?: {math.isinf(infinito_positivo)}')

# modulo Decimal
infinito_negativo = Decimal('-Infinity')
print(f'Infinito positivo: {infinito_negativo}')
print(f'es Infinito?: {math.isinf(infinito_negativo)}')