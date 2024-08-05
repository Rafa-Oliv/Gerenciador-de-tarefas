# Gerenciador de tarefas

Este é um simples gerenciador de tarefas feito em Python, utilizando SQLite para armazenamento das tarefas. O aplicativo permite adicionar, listar, marcar como concluídas e excluir tarefas.

## Funcionalidades

- Adicionar tarefa
- Listar tarefas
- Marcar tarefa como concluída
- Remover tarefa
- Sair do gerenciador de tarefas

## Como Usar

1. Clone este repositório:

    ```sh
    git clone https://github.com/Rafa-Oliv/Gerenciador-de-tarefas.git
    cd Gerenciador-de-tarefas
    ```

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/MacOS
    source venv/bin/activate
    ```

3. Instale as dependências (este passo é opcional se não houver dependências adicionais):

    ```sh
    pip install -r requirements.txt
    ```

4. Execute o gerenciador de tarefas:

    ```sh
    python app.py
    ```

## Estrutura do Projeto

- `app.py`: Arquivo principal do gerenciador de tarefas.
- `TaskManager.py`: Arquivo contendo a classe `TaskManager` para gerenciar as tarefas.
- `Database.py`: Arquivo contendo a classe `Database` para manipulação do banco de dados SQLite.
- `requirements.txt`: Arquivo com as dependências necessárias (atualmente vazio).
-  `Executavel`: Pasta que contém o arquivo 'app.exe' versão executável do código.

## Requisitos

- Python 3.6+

## Licença

Este projeto está licenciado sob a MIT License.
