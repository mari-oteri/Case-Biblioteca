# Case - API de Biblioteca Digital

O projeto é baseado na implementação de uma API REST para um sistema de biblioteca como case proposto. 

O sistema oferece as seguintes funcionalidades:

- Cadastro e gerenciamento de usuários
- Cadastro e consulta de livros e autores
- Controle do ciclo de vida de empréstimos
- Aplicação de regras de negócio como:
    - Prazo padrão de empréstimo: 14 dias
    - Multa de R$2,00 por dia de atraso
    - Máximo de 3 empréstimos ativos por usuário
- Paginação
- Logging Estruturado
- Testes automatizados

---

## Arquitetura do sistema

    app/            
    ├── main.py           - Ponto de entrada da aplicação        
    ├── core/             - Infraestrutura e utilidades (paginação, logs e geração de dados)      
    ├── db/               - Conexão e modelos do banco de dados         
    ├── schemas/          - Validação de dados da API (Pydantic)          
    ├── repositories/     - Acesso aos dados (camada de persistência)       
    ├── services/         - Regras de negócio        
    ├── routers/          - Endpoints da API       
    └── tests/            - Testes automatizados  


### Fluxo de requisição:

Router → Service → Repository → Database

---
## Tecnologias Utilizadas

- Python 3.12  
- FastAPI  
- SQLAlchemy  
- Pydantic  
- Uvicorn  
- SQLite 
- pytest + httpx

---

## Entidades Principais

### Usuário / User
- id, name, email, created_at

### Autor / Author
- id, name

### Livro / Book
- id, title, author_id, total_copies, available_copies

### Empréstimo / Loan
- id, user_id, book_id, loan_date, due_date, return_date, fine_amount

---

## Regras de Negócio Implementadas

- Prazo padrão de empréstimo: *14 dias*
- Multa: *R$2,00 por dia de atraso*
- Usuário pode ter no máximo *3 empréstimos ativos*
- Um livro só pode ser emprestado se houver cópias disponíveis

---

## Execução do Projeto

### 

```bash
1. Clonar o repositório
git clone https://github.com/mari-oteri/Case-Biblioteca.git
cd Case-Biblioteca

2. Criar ambiente virtual

    python -m venv venv

3. Ativar o ambiente:

    venv\Scripts\activate


4. Instalar dependências

    pip install -r requirements.txt

5. Executar a aplicação

    uvicorn app.main:app --reload
```

Acesse no navegador:
- Para verificar se a aplicação está online:
http://127.0.0.1:8000/

- Para acessar a documentação / Swagger:
http://127.0.0.1:8000/docs




____

### Paginação

Os endpoints de listagem aceitam:

?page=1&size=10

_____

### Exemplos de uso da API 

#### Criar Usuário

```bash
POST /users
{
  "name": "Ana",
  "email": "ana@email.com"
}
```

#### Criar Livro

```bash
POST /books
{
  "title": "Alice no País das Maravilhas",
  "author_id": 1,
  "total_copies": 5
}
```

#### Realizar Empréstimo

```bash
POST /loans
{
  "user_id": 1,
  "book_id": 1
}
```

#### Devolver Livro

```bash
POST /loans/1/return
```

#### Listar Histórico do Usuário

```bash
GET /users/1/loans
```

____

### Testes Automatizados

#### Execução (Dentro do venv / ambiente virtual )

```bash
pytest
```
#### Foram desenvolvidos alguns testes de integração que validam algumas regras de negócio, dentre eles:
- Criação e listagem de livros
- Regras de negócio de empréstimo
- Cálculo de multa

_____