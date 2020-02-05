#  API Monte seu PC (v0.1)

API para Estacionamento
### Sumário
+ [Pré Requisitos](#pré-requisitos)
+ [Comandos da aplicação](#comandos-da-aplicação)
+ [Desenvolvido com](#desenvolvido-com)
+ [Desenvolvido por](#desenvolvido-por)
 
### Pré Requisitos
+ [python](https://docs.docker.com/compose/)
+ [Django](https://docs.docker.com/compose/)
+ [Django rest](https://www.django-rest-framework.org/)

### Comandos da aplicação
- Primeiro comando:
```
sh start.sh
``` 
- Segundo comando:
```
python manage.py runserver 0.0.0.0:8000
```
- Aplicação localhost:8000
- Só será possivel entrar na api se você for superuser ou possuir um token válido.

## Usuario está sendo criado no fixture
```
Username: monteseupc
senha: intmed
```
**Rotas**

|Verb  |URI Pattern              
:----:|-------------------------|
| POST |api/monteuseupc/             
| GET  |api/processadores/          
| GET  |api/memorias/               
| GET  |api/placasdevideo/          
| GET  |api/placamaes/


### Desenvolvido com
+ [Django](https://docs.djangoproject.com/en/3.0/) - Framework Django
+ [Django Rest Framework](https://www.django-rest-framework.org/) - Django Rest Framework

### Desenvolvido por
+ **Carlos Victor** 