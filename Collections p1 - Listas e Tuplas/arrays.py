## Array, evitar usar
# Precisa definir o tipo do array no início
# Utilizado normalmente para lidar com números
# Evitamos pois existem bibliotecas que lidam melhor com isso (numpy)

import array as arr

arr.array('d', [1, 3.5])