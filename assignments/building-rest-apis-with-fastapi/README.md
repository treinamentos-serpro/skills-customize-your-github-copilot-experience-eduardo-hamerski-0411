# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para gerenciar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, modelos de dados, validação de entradas e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Listar e Consultar Livros

#### Descrição

Use o starter code para criar endpoints que permitam listar os livros do catálogo e consultar um livro específico pelo ID. Instale FastAPI e Uvicorn e execute a aplicação localmente.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI acessível localmente com Uvicorn.
- Implementar `GET /books` e retornar a lista de livros armazenada em memória.
- Implementar `GET /books/{book_id}` e retornar o livro correspondente ao ID.
- Retornar o status HTTP `404` quando o ID solicitado não existir.
- Permitir testar os endpoints pela documentação interativa em `/docs`.

### 🛠️ Cadastrar Livros

#### Descrição

Adicione um endpoint para cadastrar livros no catálogo. Use o modelo Pydantic fornecido para validar os dados recebidos e gere um ID para cada novo livro.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` com os campos `title` e `author` no corpo da requisição.
- Validar os dados de entrada com o modelo Pydantic.
- Atribuir um ID único ao novo livro e adicioná-lo ao catálogo.
- Retornar o livro criado com status HTTP `201`.

### 🛠️ Atualizar e Remover Livros

#### Descrição

Complete a API adicionando operações para atualizar e remover livros existentes. Verifique se o livro existe antes de alterar o catálogo.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar status HTTP `404` para atualizações ou remoções de IDs inexistentes.
- Retornar status HTTP `204` após remover um livro com sucesso.
- Disponibilizar os endpoints na documentação interativa em `/docs`.

Para executar a atividade, instale as dependências com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn starter-code:app --reload`.
