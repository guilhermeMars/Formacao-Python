texto_01 = "Hoje em dia, quando a gente fala da ciência de dados, pensa num guarda-chuva que inclui muitas coisas. Então vou dar um exemplo de uma parte disso que a gente costuma chamar de ciências de dados. E a ideia é, pensa numa empresa que vende sorvete ou outros objetos gelados que a gente gosta de tomar, né? — em momentos, principalmente, quentes — e quando você começa a analisar as vendas mensais ou diárias e do lado desses números você coloca a temperatura do dia ou a temperatura média do mês, você pode perceber que existe uma relação ou, mais especificamente, uma correlação entre esses dois valores, essas duas sequências de valores."

texto_02 = "Imagine que você aguardou por meses pelo show da sua banda favorita, e quando chega o grande dia, o show é cancelado, pois um dos membros não pode comparecer. Esse membro pode ser o vocalista, guitarrista ou baterista, importante para que a banda exista, pois só assim conseguem fazer os shows e produzir suas músicas. O mesmo acontece no Angular, pois todo o desenvolvimento de uma aplicação é baseado em componentes, e cada um é importante para uma aplicação."

from collections import Counter

def analisa_frequencia(texto):
    letras = Counter(texto.lower())
    # print(letras)

    num_letras = sum(letras.values())
    # print(num_letras)

    # List Comprehension
    proporcoes = [(letra, frequencia / num_letras) for letra, frequencia in letras.items()]
    proporcoes = Counter(dict(proporcoes))

    top_dez = proporcoes.most_common(10)
    # print(top_dez)

    for caractere, proporcao in top_dez:
        print("{} -> {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia(texto_01)
print("#####")
analisa_frequencia(texto_02)
