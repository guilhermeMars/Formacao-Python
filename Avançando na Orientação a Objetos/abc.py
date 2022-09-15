# abstract base classes
# Classes abstratas são aquelas que exigem que você implemente um método específico para seu funcionamento
# Complementa a ideia do duck typing
# https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/42183

from abc import ABC
# Tem muitos abc nas collections, normalmente vai atender ao caso
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

filmes = Playlist() # Avisa no console qual as funções necessárias para implementar


from numbers import Complex

class numeros(Complex):
    pass

numero_complexo = numeros()
