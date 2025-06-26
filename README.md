# 🏢 CondoManager

Sistema de Gerenciamento de Condomínios - Projeto final da disciplina C216

## 📋 Descrição

O CondoManager é um sistema completo para gerenciamento de condomínios, permitindo o agendamento de serviços de manutenção e cadastro de fornecedores especializados.

## 🛠️ Tecnologias Utilizadas

- **Backend**: FastAPI (Python)
- **Frontend**: Flask (Python) 
- **Banco de Dados**: PostgreSQL
- **Orquestração**: Docker e Docker Compose
- **Interface**: Bootstrap 5

## ✅ Requisitos Atendidos

- ✅ Backend com FastAPI
- ✅ Frontend com Flask  
- ✅ Persistência com PostgreSQL
- ✅ Orquestração com Docker e Docker Compose
- ✅ Pelo menos 3 páginas (Início, Ordens, Fornecedores)
- ✅ 1+ tabelas no banco (ordens, fornecedores)
- ✅ 5+ métodos REST (GET, POST, PUT, DELETE, PATCH)

## 🚀 Como Executar

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd CondoManager
```

2. **Execute com Docker Compose**
```bash
docker-compose up --build
```

3. **Acesse as aplicações**
- Frontend: http://localhost:5000
- Backend API: http://localhost:8000
- Documentação API: http://localhost:8000/docs

## 📁 Estrutura do Projeto

```
CondoManager/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # API FastAPI
│   │   ├── models.py        # Modelos do banco
│   │   ├── schemas.py       # Schemas Pydantic
│   │   ├── crud.py          # Operações CRUD
│   │   └── database.py      # Configuração DB
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── templates/           # Templates HTML
│   ├── static/             # CSS e assets
│   ├── app.py              # Aplicação Flask
│   ├── Dockerfile
│   └── requirements.txt
└── docker-compose.yml      # Orquestração
```

## 🎯 Funcionalidades

### Ordens de Serviço
- ✅ Criar nova ordem de serviço
- ✅ Listar todas as ordens
- ✅ Atualizar ordem completa (PUT)
- ✅ Atualizar apenas status (PATCH) 
- ✅ Deletar ordem
- ✅ Obter ordem específica (GET)

### Fornecedores
- ✅ Cadastrar novo fornecedor
- ✅ Listar todos os fornecedores
- ✅ Atualizar fornecedor (PUT)
- ✅ Deletar fornecedor
- ✅ Obter fornecedor específico (GET)

## 📊 API Endpoints

### Ordens de Serviço
- `GET /ordens` - Listar todas
- `POST /ordens` - Criar nova
- `GET /ordens/{id}` - Obter específica
- `PUT /ordens/{id}` - Atualizar completa
- `PATCH /ordens/{id}/status` - Atualizar status
- `DELETE /ordens/{id}` - Deletar

### Fornecedores  
- `GET /fornecedores` - Listar todos
- `POST /fornecedores` - Criar novo
- `GET /fornecedores/{id}` - Obter específico
- `PUT /fornecedores/{id}` - Atualizar
- `DELETE /fornecedores/{id}` - Deletar

## 🗄️ Banco de Dados

**Tabela: ordens**
- id (Primary Key)
- tipo (String)
- descricao (String)
- status (String)
- data_agendada (Date)
- fornecedor_id (Foreign Key - OPCIONAL)

**Tabela: fornecedores**
- id (Primary Key)
- nome (String)
- especialidade (String)  
- contato (String)


## 👥 Autor
Projeto desenvolvido como requisito da disciplina C216 - Inatel
