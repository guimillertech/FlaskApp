

```markdown
# Flask App - Formulários e Visualização de Dados

Este projeto é uma aplicação web construída com Flask, que permite adicionar cursos através de formulários e visualizar os dados em uma tabela. Ele utiliza SQLite como banco de dados.

## Funcionalidades

- Adicionar cursos com nome, descrição, endereço e carga horária.
- Visualizar a lista de cursos em uma tabela.
- Conectar-se a bancos de dados

## Tecnologias Utilizadas

- Flask
- SQLite
- SQLAlchemy
- HTML/CSS

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente:

1. Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicialize o banco de dados:
    ```bash
    flask db init
    flask db migrate -m "Inicializa banco de dados"
    flask db upgrade
    ```

5. Execute a aplicação:
    ```bash
    flask run
    ```

6. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

```plaintext
.
├── app.py              # Arquivo principal da aplicação Flask
├── instance            # Arquivo do banco de dados SQLITE3
│   ├── cursos.sqlite3
├── templates/          # Diretório com os templates HTML
│   ├── index.html
│   ├── sobre.html
│   ├── novo_curso.html
│   ├── cursos.html
└── static/             # Diretório para arquivos estáticos (CSS, JS, imagens)
```

## Funcionalidades e Rotas

### Sobre (`/cursos`)

Página onde os usuários podem visualizar os cursos salvos e adicionar outros.

### Adicionar Curso (`/novo_curso`)

Página com um formulário para adicionar novos cursos.

## Requisitos

- Python 3.11
- Flask
- Flask-SQLAlchemy
- SLQLITE3

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


### Contato

Para mais informações, entre em contato via [guimillertech@gmail.com](mailto:guimiller@gmail.com).

```

