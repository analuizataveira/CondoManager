from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from datetime import datetime

app = Flask(__name__)
app.secret_key = "seu_secret_key_aqui"
API_URL = "http://backend:8000"

@app.route('/')
def index():
    return render_template("index.html")

# ROTAS PARA ORDENS DE SERVIÇO
@app.route('/ordens')
def listar_ordens():
    try:
        response = requests.get(f"{API_URL}/ordens")
        ordens = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        ordens = []
        flash("Erro ao conectar com a API", "error")
    return render_template("ordens.html", ordens=ordens)

@app.route('/ordens/nova', methods=['GET', 'POST'])
def nova_ordem():
    if request.method == 'POST':
        dados = {
            "tipo": request.form['tipo'],
            "descricao": request.form['descricao'],
            "status": request.form['status'],
            "data_agendada": request.form['data_agendada'],
            "fornecedor_id": int(request.form['fornecedor_id']) if request.form['fornecedor_id'] else None
        }
        try:
            response = requests.post(f"{API_URL}/ordens", json=dados)
            if response.status_code == 200:
                flash("Ordem de serviço criada com sucesso!", "success")
                return redirect(url_for('listar_ordens'))
            else:
                flash("Erro ao criar ordem de serviço", "error")
        except requests.exceptions.RequestException:
            flash("Erro ao conectar com a API", "error")
    
    # Carregar fornecedores para o dropdown
    try:
        response = requests.get(f"{API_URL}/fornecedores")
        fornecedores = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        fornecedores = []
    
    return render_template("nova_ordem.html", fornecedores=fornecedores)

@app.route('/ordens/<int:ordem_id>/editar', methods=['GET', 'POST'])
def editar_ordem(ordem_id):
    if request.method == 'POST':
        dados = {
            "tipo": request.form['tipo'],
            "descricao": request.form['descricao'],
            "status": request.form['status'],
            "data_agendada": request.form['data_agendada'],
            "fornecedor_id": int(request.form['fornecedor_id']) if request.form['fornecedor_id'] else None
        }
        try:
            response = requests.put(f"{API_URL}/ordens/{ordem_id}", json=dados)
            if response.status_code == 200:
                flash("Ordem de serviço atualizada com sucesso!", "success")
                return redirect(url_for('listar_ordens'))
            else:
                flash("Erro ao atualizar ordem de serviço", "error")
        except requests.exceptions.RequestException:
            flash("Erro ao conectar com a API", "error")
    
    # Carregar dados da ordem atual
    try:
        response = requests.get(f"{API_URL}/ordens/{ordem_id}")
        if response.status_code == 200:
            ordem = response.json()
        else:
            flash("Ordem não encontrada", "error")
            return redirect(url_for('listar_ordens'))
    except requests.exceptions.RequestException:
        flash("Erro ao conectar com a API", "error")
        return redirect(url_for('listar_ordens'))
    
    # Carregar fornecedores para o dropdown
    try:
        response = requests.get(f"{API_URL}/fornecedores")
        fornecedores = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        fornecedores = []
    
    return render_template("editar_ordem.html", ordem=ordem, fornecedores=fornecedores)

@app.route('/ordens/<int:ordem_id>/deletar', methods=['POST'])
def deletar_ordem(ordem_id):
    try:
        response = requests.delete(f"{API_URL}/ordens/{ordem_id}")
        if response.status_code == 200:
            flash("Ordem de serviço deletada com sucesso!", "success")
        else:
            flash("Erro ao deletar ordem de serviço", "error")
    except requests.exceptions.RequestException:
        flash("Erro ao conectar com a API", "error")
    
    return redirect(url_for('listar_ordens'))

# ROTAS PARA FORNECEDORES
@app.route('/fornecedores')
def listar_fornecedores():
    try:
        response = requests.get(f"{API_URL}/fornecedores")
        fornecedores = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        fornecedores = []
        flash("Erro ao conectar com a API", "error")
    return render_template("fornecedores.html", fornecedores=fornecedores)

@app.route('/fornecedores/novo', methods=['GET', 'POST'])
def novo_fornecedor():
    if request.method == 'POST':
        dados = {
            "nome": request.form['nome'],
            "especialidade": request.form['especialidade'],
            "contato": request.form['contato']
        }
        try:
            response = requests.post(f"{API_URL}/fornecedores", json=dados)
            if response.status_code == 200:
                flash("Fornecedor criado com sucesso!", "success")
                return redirect(url_for('listar_fornecedores'))
            else:
                flash("Erro ao criar fornecedor", "error")
        except requests.exceptions.RequestException:
            flash("Erro ao conectar com a API", "error")
    
    return render_template("novo_fornecedor.html")

@app.route('/fornecedores/<int:fornecedor_id>/editar', methods=['GET', 'POST'])
def editar_fornecedor(fornecedor_id):
    if request.method == 'POST':
        dados = {
            "nome": request.form['nome'],
            "especialidade": request.form['especialidade'],
            "contato": request.form['contato']
        }
        try:
            response = requests.put(f"{API_URL}/fornecedores/{fornecedor_id}", json=dados)
            if response.status_code == 200:
                flash("Fornecedor atualizado com sucesso!", "success")
                return redirect(url_for('listar_fornecedores'))
            else:
                flash("Erro ao atualizar fornecedor", "error")
        except requests.exceptions.RequestException:
            flash("Erro ao conectar com a API", "error")
    
    # Carregar dados do fornecedor atual
    try:
        response = requests.get(f"{API_URL}/fornecedores/{fornecedor_id}")
        if response.status_code == 200:
            fornecedor = response.json()
        else:
            flash("Fornecedor não encontrado", "error")
            return redirect(url_for('listar_fornecedores'))
    except requests.exceptions.RequestException:
        flash("Erro ao conectar com a API", "error")
        return redirect(url_for('listar_fornecedores'))
    
    return render_template("editar_fornecedor.html", fornecedor=fornecedor)

@app.route('/fornecedores/<int:fornecedor_id>/deletar', methods=['POST'])
def deletar_fornecedor(fornecedor_id):
    try:
        response = requests.delete(f"{API_URL}/fornecedores/{fornecedor_id}")
        if response.status_code == 200:
            flash("Fornecedor deletado com sucesso!", "success")
        else:
            flash("Erro ao deletar fornecedor", "error")
    except requests.exceptions.RequestException:
        flash("Erro ao conectar com a API", "error")
    
    return redirect(url_for('listar_fornecedores'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
