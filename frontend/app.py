from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
API_URL = "http://backend:8000"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ordens')
def listar_ordens():
    response = requests.get(f"{API_URL}/ordens")
    ordens = response.json()
    return render_template("ordens.html", ordens=ordens)

@app.route('/fornecedores')
def listar_fornecedores():
    response = requests.get(f"{API_URL}/fornecedores")
    fornecedores = response.json()
    return render_template("fornecedores.html", fornecedores=fornecedores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
