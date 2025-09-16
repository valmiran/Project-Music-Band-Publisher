📘 Guia de Utilização — Portal da Banda CESMAC
Introdução

O Portal da Banda CESMAC é uma aplicação desenvolvida em Django 5, voltada para gerenciar publicações, eventos, seleções e conteúdos da banda.
O sistema permite que apenas integrantes, professores e convidados autorizados realizem login para interagir e publicar. Visitantes podem acessar as páginas públicas como home, agenda, mídia e contato.

Tecnologias Utilizadas

Python 3.11+

Django 5.x

Pillow (biblioteca para trabalhar com imagens)

tzdata (para compatibilidade de timezones no Windows)

Bootstrap/Tailwind (customização da interface)

Instalação e Configuração
1. Clonar o repositório

Faça o download do código:

git clone https://github.com/seuusuario/banda-cesmac.git
cd banda-cesmac

2. Criar ambiente virtual

No Windows:

python -m venv .venv
.venv\Scripts\Activate


No Linux/macOS:

python3 -m venv .venv
source .venv/bin/activate

3. Instalar dependências

Utilize o arquivo requirements.txt ou instale manualmente:

pip install -r requirements.txt
# ou
pip install "django==5.0.*" Pillow tzdata

4. Migrar banco de dados
python manage.py makemigrations
python manage.py migrate

5. Criar superusuário
python manage.py createsuperuser

6. Rodar servidor
python manage.py runserver


Acesse em: http://127.0.0.1:8000/

Funcionalidades

Home: Banner principal, história da banda, missão, visão e valores, últimas publicações, agenda e integrantes.

Publicações: Postagens com imagem ou vídeo, curtidas e comentários.

Eventos: Cadastro de ensaios, shows e participações.

Seleções: Inscrição em processos seletivos com formulário completo.

Mídia: Galeria de fotos, discografia e links externos (Spotify, YouTube).

Parcerias: Professores, apoiadores e patrocinadores.

Administração: Painel administrativo completo acessível em http://127.0.0.1:8000/admin
.

Perfis de Usuário

Administrador: gerencia todos os recursos (usuários, posts, eventos, seleções).

Professor: pode abrir seleções e publicar conteúdos.

Integrante: pode postar, comentar e se inscrever em seleções.

Visitante: tem acesso somente às páginas públicas.

Comandos Úteis

Ativar ambiente virtual

Windows: .venv\Scripts\Activate

Linux/macOS: source .venv/bin/activate

Desativar venv: deactivate

Criar migrações: python manage.py makemigrations

Aplicar migrações: python manage.py migrate

Criar superusuário: python manage.py createsuperuser

Rodar servidor: python manage.py runserver

Licença

Este projeto é de caráter acadêmico e foi desenvolvido como parte de uma atividade de extensão no CESMAC.
