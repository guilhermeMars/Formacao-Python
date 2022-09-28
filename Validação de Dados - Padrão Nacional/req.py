# Requests Python
# Já vem instalada junto com o Python

import requests

req = requests.get('https://viacep.com.br/ws/01001000/json/')
print(req.text)
