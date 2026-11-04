# 📘 Atividade: Aplicações Web com Flask

## 🎯 Objetivo

Crie uma aplicação web em Python que exiba e permita gerenciar um catálogo de livros usando Flask, templates Jinja e formulários HTML. Você praticará rotas de páginas web e o fluxo de dados entre formulários e o servidor.

## 📝 Tarefas

### 🛠️ Exibir o Catálogo em uma Página Web

#### Descrição

Complete a rota principal e o template Jinja para apresentar os livros de exemplo no navegador. Inicie o servidor local e confira a página em `/`.

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação Flask localmente.
- Exibir o título da aplicação e os livros armazenados na lista `books`.
- Usar um loop Jinja para gerar um item HTML para cada livro.
- Mostrar uma mensagem adequada quando o catálogo estiver vazio.

### 🛠️ Adicionar Livros por um Formulário

#### Descrição

Adicione à página um formulário HTML para cadastrar um livro. Quando enviado, o servidor deve ler os campos do formulário, validar os valores e atualizar o catálogo em memória.

#### Requisitos
O programa concluído deve:

- Incluir campos `title` e `author` e enviar os dados usando o método `POST`.
- Ignorar ou rejeitar o envio quando título ou autor estiver vazio.
- Adicionar os livros válidos com um ID único.
- Redirecionar para a página principal depois do envio para atualizar a lista exibida.

### 🛠️ Remover Livros do Catálogo

#### Descrição

Permita que o usuário remova um livro diretamente pela página. Cada livro exibido deve ter seu próprio formulário de remoção.

#### Requisitos
O programa concluído deve:

- Exibir um botão de remoção associado ao ID de cada livro.
- Enviar a remoção usando `POST` para a rota `/books/<book_id>/delete`.
- Remover da lista somente o livro cujo ID corresponde ao solicitado.
- Redirecionar para a página principal depois da remoção.

Instale a dependência com `python -m pip install flask` e execute a aplicação com `flask --app starter-code run --debug`.
