# teste-python

### Delivery API

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
# Instale o ambiente virtual
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

```bash
# criar um usuario admin para conseguir logar na pagina admin do django
$ python manage.py createsuperuser
```
```bash
# rodar o servidor localmente
$ python manage.py runserver
```

### Pagina de administrador

- Após todos os passos acima, entrar na url "http://127.0.0.1:8000/admin" que é a url padrao do django e acessar com seu login e senha criado a alguns passos acima.