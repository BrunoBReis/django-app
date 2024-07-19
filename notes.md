## Alguns comandos interessantes

`$python3 -m venv .venv`
    - cira um ambiente virtual do python onde se consegue dockerizar todos as dependencias de pip

`$source .venv/bin/activate`
    - ativa o ambiente virtual

`$deactivate`
    - desativa o ambiente virtual

`$source deactivate`
    - forca o fechamento do ambiente virtual

`$python3 -m pip install Django`
    - instalando o Django 

`python3 -m pip install --upgrade pip`
    - upgrade pip version

`django-admin startproject meuprojeto`
    - inicia um projeto em Django

`python3 manage.py statapp posts`
    - inicia um posts no django

`python3 manage.py makemigrations`
    - inicializa o model para fazer a migracao

`python3 menage.py migrate`
    - aplica todas as migracoes (existem migracoes criadas pelo proprio django)

`python3 manage.py shell`
    - inicializa o python com o shell

`python3 manage.py createsuperuser`
    - cria um superusuario para a pagina de admin

## Fluxo para comecar o projeto

1. Criação do ambiente virtual
- Baixando as bibliotecas com o pip 
- Criação do ambiente do Django 
- Sair do ambiente virutal

## Fluxo para retomar o projeto

1. Retomada do ambiente virutal

## Criacao de paginas

1. Precisa-se criar uma URL
- Criacao do views
    - Local no qual usaremos o request do HTTP
- Atualizacao no urls com os views

## Criacao de templetes HTML

1. definir um pasta para o template
- definir os templates para as paginas
- alterar a pagina de template padrao em setting.py
    - templates -> dirs ['nome_da_pasta']

## Criacao de templetes CSS

1. basta criar uma pasta de static
- em settings.py import os 
- criar uma dirs estatica
- os.path.join(BASE_DIR, 'static'), define um caminho para acessar o static css
- basta alterar o .html com a chamada do static 

## Criacao de um app
1. comando do pots
- atualizacao no settings do main
    - atualizar a existencia de um novo app

## Layouts
1. criacao de um layout no meuprojeto
- utilizar o layout como base para as outras paginas

## Models
E caminho para inicializar um modelo no banco de dados
1. revisitar esse conteudo

## ORM
E uma forma de testar o banco de dados via terminal
1. inicializar o python com shell
- from posts.models import Post (metodo de post)
- fazer a criacao de um objeto para teste

## Atualizar painel de Admin
Toda vez que é feito um app é preciso atualizá-lo na página de admin
1. abrir a pasta do app
- ir para a página de admin
- atualizar a página
- admin.site.register(App)

## Adicionar uma imagem
É preciso alterar nas configurações e incluir a pasta de imagens
