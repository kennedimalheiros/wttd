# Eventex

Sistema de Eventos

[![Build Status](https://travis-ci.org/kennedimalheiros/wttd_python.svg?branch=master)](https://travis-ci.org/kennedimalheiros/wttd_python)
[![Code Health](https://landscape.io/github/kennedimalheiros/wttd_python/master/landscape.svg?style=flat)](https://landscape.io/github/kennedimalheiros/wttd_python/master)


## Como desenvolver

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualev.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

`
git clone https://github.com/kennedimalheiros/wttd_python.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
`

## Como fazer o deploy?
1. Crie uma instância no heroku.
2. Envie as configurações para heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

`
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#Configuro o email
git push heroku master --force
`