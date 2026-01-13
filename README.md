# Case - API de Biblioteca Digital

O projeto é baseado na implementação de uma API REST para um sistema de biblioteca, permitindo:

- Cadastro e gerenciamento de *usuários*
- Cadastro e consulta de *livros* e *autores*
- Controle do ciclo de vida de *empréstimos*
- Aplicação de regras de negócio como:
  - Prazo padrão de empréstimo: *14 dias*
  - Multa de *R$2,00 por dia de atraso*
  - Máximo de *3 empréstimos ativos* por usuário

---

## Arquitetura do sistema

app/            
 ├── main.py           - Ponto de entrada da aplicação        
 ├── core/             - Infraestrutura e utilidades (ex: paginação)      
 ├── db/               - Conexão e modelos do banco de dados         
 ├── schemas/          - Validação de dados da API (Pydantic)          
 ├── repositories/     - Acesso aos dados (camada de persistência)       
 ├── services/         - Regras de negócio        
 └── routers/          - Endpoints da API    


### Fluxo de requisição:

Router → Service → Repository → Database

---
## Tecnologias Utilizadas

- Python 3.12  
- FastAPI  
- SQLAlchemy  
- Pydantic  
- Uvicorn  
- SQLite (ambiente de desenvolvimento)

---

## 🗄️ Entidades Principais

### Usuário (User)
- id, name, email, created_at

### Autor (Author)
- id, name

### Livro (Book)
- id, title, author_id, total_copies, available_copies

### Empréstimo (Loan)
- id, user_id, book_id, loan_date, due_date, return_date, fine_amount

---

## Regras de Negócio Implementadas

- Prazo padrão de empréstimo: *14 dias*
- Multa: *R$2,00 por dia de atraso*
- Usuário pode ter no máximo *3 empréstimos ativos*
- Um livro só pode ser emprestado se houver cópias disponíveis

---

## Execução do Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/mari-oteri/Case-Biblioteca.git
cd Case-Biblioteca

2. Criar ambiente virtual

    python -m venv venv

    Ativar o ambiente:

    venv\Scripts\activate


3. Instalar dependências

    pip install -r requirements.txt

4. Executar a aplicação

    uvicorn app.main:app --reload

    Acesse no navegador:
        - Para verificar se a aplicação está online:
        http://127.0.0.1:8000/

        - Para acessar a documentação / Swagger:
        http://127.0.0.1:8000/docs


⸻

🌐 Principais Endpoints

Usuários
	•	POST /users
	•	GET /users
	•	GET /users/{id}

Autores
	•	POST /authors
	•	GET /authors

Livros
	•	POST /books
	•	GET /books
	•	GET /books/{id}/available

Empréstimos
	•	POST /loans
	•	POST /loans/{id}/return
	•	GET /loans/active
	•	GET /loans/overdue

⸻

📦 Paginação

Os endpoints de listagem aceitam:

?page=1&size=10

⸻

🧠 Decisões Técnicas
	•	Arquitetura em camadas para facilitar manutenção e testes
	•	Separação clara entre regras de negócio e acesso a dados
	•	Uso de Pydantic para validação e documentação automática
	•	Banco SQLite para desenvolvimento local (facilmente substituível por PostgreSQL em produção)