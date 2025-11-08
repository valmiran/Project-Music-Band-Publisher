# Project Music Band Publisher

## Sobre o projeto

Este projeto é uma plataforma para publicação e gerenciamento de bandas de música.  
Está sendo desenvolvido em conjunto para fins de aprendizado e colaboração em Django e PostgreSQL.
<br>

## Progresso até agora

- Inicialização do projeto Django com `django-admin startproject music_band`.
- Criação dos apps principais: `core` e `base`.
- Configuração do banco de dados PostgreSQL no `settings.py`:
  - Banco: `musicbanddb`
  - Usuário: `postgres`
  - Senha: `admin`
  - Host: `localhost`
  - Porta: `5432`
- Criação manual do banco de dados `musicbanddb` no PostgreSQL.
- Execução das migrações iniciais com `python manage.py    makemigrations` e finalizadas com `python manage.py migrate`.
- Implementação da view `home` em `core/views.py` para renderizar a página inicial.
- Configuração das rotas em `core/urls.py`:
  - URL raiz (`/`) aponta para a view `home`.
- Inclusão das URLs do app `core` no arquivo principal `music_band/urls.py`.
- Criação do template `index.html` para a página inicial.
- Testes de acesso à página inicial realizados com sucesso.

<br>
<br>

## Como rodar o projeto

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
2. Crie o banco de dados `musicbanddb` no PostgreSQL.
3. Execute as migrações:
   ```
   python manage.py migrate
   ```
4. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```
5. Acesse [http://localhost:8000](http://localhost:8000) para visualizar a página inicial.

<br>
<br>

## Próximos passos

- Definir os modelos das bandas e usuários.
- Implementar autenticação e cadastro.
- Criar páginas para cadastro e listagem de bandas.
- Dividir tarefas entre os membros do grupo.
- Documentar decisões e dúvidas para facilitar o trabalho em equipe.
-Formentar a analise de requisitos em coadunação com o professor.

---

## 🗂️ Modelo de Dados (Banco de Dados)

Abaixo estão descritas as principais tabelas do sistema e as decisões técnicas tomadas para sua implementação.

### 📋 Estrutura das Tabelas

#### 1. Usuário (`Usuario`)
Estende o modelo padrão de autenticação do Django (`AbstractUser`).
- **Motivo:** Aproveitar todo o sistema de segurança, login e criptografia de senhas que o Django já oferece, adicionando apenas os campos personalizados necessários.
- **Campos Principais:**
  - `username`, `email`, `password` (herdados do Django)
  - `tipo`: Define o perfil de acesso (Admin, Membro da Banda, Visitante).

#### 2. Projeto (`Projeto`)
Armazena os grandes projetos da banda.
- **Campos Principais:** `titulo`, `descricao`, `data_inicio`, `data_fim`, `status` (Em andamento, Concluído, Cancelado).
- **Relação:** Vinculado ao usuário que o criou (`criado_por`).

#### 3. Evento (`Evento`)
Registra eventos específicos (shows, ensaios), que podem ou não fazer parte de um projeto maior.
- **Campos Principais:** `titulo`, `descricao`, `data`, `local`, `status` (Planejado, Realizado, Cancelado).
- **Relações:**
  - Pode ser vinculado a um `Projeto` (opcional).
  - Vinculado ao usuário criador (`criado_por`).

#### 4. Artista (`Artista`)
Perfil estendido para usuários que são membros da banda.
- **Motivo:** Separar dados sensíveis de login (tabela Usuário) de dados públicos do perfil artístico.
- **Campos Principais:** `genero_musical`, `biografia`, `foto_perfil`.
- **Relação:** Conexão 1-para-1 com `Usuario` e N-para-N com `Instrumento`.

#### 5. Instrumento (`Instrumento`)
Lista de instrumentos que os artistas podem tocar.
- **Campos Principais:** `nome`, `tipo` (Corda, Sopro, Percussão, etc.).

#### 6. Notificação (`Notificacao`)
Sistema para alertar usuários sobre novidades.
- **Campos Principais:** `mensagem`, `data_hora`, `visualizada` (bool).
- **Relações:** Pode apontar para um `Projeto` ou `Evento` relacionado.

#### 7. Atualização (`Atualizacao`)
Histórico de mudanças feitas em projetos ou eventos.
- **Decisão Técnica:** Uso de **Relação Polimórfica** (`GenericForeignKey`).
- **Motivo:** Permite que uma única tabela de atualizações sirva tanto para `Projeto` quanto para `Evento`, sem precisar duplicar tabelas ou criar campos vazios.

---


**Colabore, tire dúvidas e compartilhe ideias!**
