# -*- coding: latin1 -*-

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./templates', static_url_path='/static')

@app.route('/')
def home():
    #return "oi mundo eu sou o flask", 200

    dados = {}
    dados['cabec3'] = 'cabecalho 3 teste em flask'

    usuarios = []
    usuarios.append({ 'userID' : 'rmbertoni', 'userName' : 'Rafael Malta Bertoni'})
    usuarios.append({ 'userID' : 'lupcoelho', 'userName' : 'Luciana P. Coelho'})




    return render_template("index.html", dados=dados, usuarios=usuarios), 200

@app.route('/api')
def api():
    return "retorno da api em flask", 200


app.run()



#@app.route('/login')
#def tweets():
#    username = request.args.get('username')
#    password = request.args.get('password')
