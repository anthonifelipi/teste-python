# teste-python

### Kollection API

API para gerar fretes a partir de uma determinada Order.

## Review

Esse projeto foi feito a partir de um teste tecnico para empresa Angular onde o objetivo era criar um app Delivery e 2 models, sendo elas Order e Freight. Onde com as especificações da Order era necessario buscar na API melhor envio as informações pedidas no escopo do teste.

## Features da API

- Emitir uma Order
- Fazer cotação de frete com algumas transportadoras com as informaões obtidas na Order

## Tecnologias Utilizadas

Neste Projeto usei as seguintes tecnologias:

- [x] Python
- [x] Django_rest_framework
- [x] Testes de models em Python

### Para rodar o projeto em sua máquina

- Necessario ter instalado em sua maquina o Python3

  **Clone o projeto deste repositório**

  ```bash
  $ git clone git@github.com:anthonifelipi/teste-python.git
  ```

```bash
$ cd teste-python.git
```

**Siga esses passos no terminal**

```bash
# Instale as dependencias
$ python -m venv venv
```

```bash
# entrar no ambiente
$ source venv/bin/activate
```

```bash
# instalar as dependencias.
$ pip install -r requirements.txt
```

```bash
# rodas as migrations
$ python manage.py migrate
```
