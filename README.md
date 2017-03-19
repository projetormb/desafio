Desafio de API
-----------------------------


Comunicando com o Twitter !!!

* Execução:

	python tweets.py
	Execute localhost:5000 no seu navegador para testar a página.

	python testes.py
	Testes automatizados do consumo da API.


* Dependências:


    'MySQLdb':
    $ pip install MySQL-python

    'OAuth1Session' em "requests_oauthlib":
    $ pip install requests-oauthlib

    'Flask':
    $ pip install flask

    'Unit Test':
    $ pip install unittest2




* Observações:

1) o banco de dados MySQL está hospedado na Kinghost, em mysql.mbcorporate.com.br
2) utilizei minha conta no twitter para ativar os tokens de acesso à suas APIs
3) os resultados podem ser vistos conforme a página https://twitter.com/rmbertoni/with_replies, ou seja, vai trazer N tweets inclusive replies.



* Referências:

https://pypi.python.org/pypi/requests-oauthlib/0.8.0
(usei essa lib para fazer autenticação no Twitter)


http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html
(não conhecia Flask, esse cara me ajudou bastante)
