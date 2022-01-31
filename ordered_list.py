import requests
from flask import Flask

app = Flask('Ordered_numbers')


@app.route('/olamundo', methods=['GET'])
def OlaMundo():
    return {'ola': 'mundo'}


@app.route('/orderednumber', methods=['GET'])
def numerosOrdenados():
    def menor(lista):
        imv = 0  # onde imv armazena a posição do menor elemento (indice do menor valor)
        for i in range(1, len(lista)):  # percorremos todos os indices de 1 ao tamanho da lista
            if lista[i] < lista[imv]:
                imv = i
        return lista.pop(imv)

    def ordena(lista):
        copia = lista.copy()  # criamos o copia pois tudo que alteramos na lista dentro da funcao, é alterado na lista externa também
        lista_ordenada = []

        while len(copia) > 0:
            m = menor(copia)
            lista_ordenada.append(m)
        return lista_ordenada

    page = 1
    dados = []
    has_next = True
    while has_next:
        response = requests.get(f'http://challenge.dienekes.com.br/api/numbers?page={page}')
        results = response.json()
        if 'numbers' in results:
            if len(results['numbers']) == 0:
                has_next = False
            else:
                dados = dados + results['numbers']

                page = page + 1
                print(page)
        else:
            page = page + 1

    x = dados
    y = ordena(x)
    print(y)

    per_page = 50
    pagination_end = page * per_page
    page_ordem = y[pagination_end - per_page:pagination_end]

    return {'Lista ordenada': page_ordem}


app.run(port=8082)
