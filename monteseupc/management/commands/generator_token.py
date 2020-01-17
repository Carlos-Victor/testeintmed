from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import glob

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        token = Token.objects.get_or_create(
            user_id=User.objects.all().filter(username="monteseupc")[0].id)
        arquivo = open('front/.env', 'r')
        lista = arquivo.readlines()
        if len(lista) == 0:
            print("TO AQUI")
            lista.append("VUE_APP_TOKEN="+ str(token)[9:49])
            gravar = open('front/.env', 'w').writelines(lista)
        else:
            for token_lista in lista:
                if "VUE_APP_TOKEN=" in token_lista:
                    token_id = lista.index(token_lista)
                    lista[token_id] = "VUE_APP_TOKEN="+ str(token)[9:49]
                    gravar = open('front/.env', 'w').writelines(lista)