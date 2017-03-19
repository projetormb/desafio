# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify

from consumo import consumoTwitter

app = Flask(__name__, template_folder='./templates', static_url_path='/static')

@app.route('/')
def home():

    usuarios = []
    usuarios.append({ 'userID' : 'rmbertoni', 'userName' : 'Rafael Malta Bertoni'})
    usuarios.append({ 'userID' : 'lupcoelho', 'userName' : 'Luciana P. Coelho'})
    usuarios.append({ 'userID' : 'naoexiste', 'userName' : u'Usuário inexistente'})

    return render_template("index.html", usuarios=usuarios), 200

@app.route('/api', methods=['POST'])
def api():
    maxTweets = int(request.form['maxTweets'])
    userName = request.form['userName']

    retorno = consumoTwitter(userName, maxTweets)
    return jsonify(retorno)

app.run()
