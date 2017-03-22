Desafio de API
---------------


Comunicando com o Twitter !!!

Este exemplo em python tem a finalidade de comunicar com a API do twitter, mostrando os últimos tweets e gravando no banco de dados MySQL.


* Instalação (utilizando como exemplo, uma pasta "repoDesafio" e ambiente virtual como "envDesafio"):


    mkdir envDesafio
    virtualenv envDesafio
    source ./envDesafio/bin/activate

    pip install requests-oauthlib
    pip install flask
    pip install unittest2

    sudo apt-get update
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install python-dev
    pip install mysql-python

    mkdir repoDesafio
    cd ./repoDesafio/

    git clone https://github.com/projetormb/desafio .

    cd ./api

    python tweets.py
    ## Execute localhost:5000 no seu navegador para testar a página.

    python testes.py
    ## Testes automatizados do consumo da API, resultados serão mostrados no console.



* Observações:

1) o banco de dados MySQL está hospedado na Kinghost, em mysql.mbcorporate.com.br
2) utilizei minha conta no twitter para ativar os tokens de acesso à suas APIs
3) os resultados podem ser vistos conforme a página https://twitter.com/rmbertoni/with_replies, ou seja, vai trazer N tweets inclusive replies.
