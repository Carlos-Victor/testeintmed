from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField, HyperlinkedIdentityField, ValidationError
from monteseupc.models import *
import re


def validator_marca_procesador(value):
    if str(value['placa_mae'].processadores_suportados) == "ambos":
        return value
    elif str(value['processador'].marca) != str(value['placa_mae'].processadores_suportados):
        raise ValidationError("Processador incompativel com a Placa Mãe")
    return value


def validacao_placa_de_video(value):
    if value['placa_mae'].video_integrado == False and value['placa_de_video'] == None:
        raise ValidationError(
            "A placa mãe não possui video integrado, escolha uma placa de vídeo")
    return value


def validacao_quantidade_de_memoria(value):
    total_de_memoria_escolhida = int(
        re.sub("[^0-9]", '', value['tamanho_da_memoria'])) * int(value['quantidade_de_memoria'])
    tamanho_memorias = int(
        re.sub("[^0-9]", '', str(value['placa_mae'].memom_suportada)))
    print("TO AQUI", tamanho_memorias)
    if total_de_memoria_escolhida > tamanho_memorias:
        raise ValidationError('A placa mãe so suporta {}GB de memoria, por favor escolha igual ou menor'.format(
            tamanho_memorias, total_de_memoria_escolhida))
    return value


def validacao_quantidade_de_slots(value):
    if value['quantidade_de_memoria'] > value['placa_mae'].slots:
        raise HttpRespo('A Placa mãe so possui {} slots, selecione uma quantidade menor ou igual.'.format(
            value['placa_mae'].slots))
    return value


class MonteseupcSerializer(ModelSerializer):
    processador = SlugRelatedField(
        slug_field='produto',
        queryset=Processador.objects.all()
    )
    placa_mae = SlugRelatedField(
        slug_field='produto',
        queryset=Placa_mae.objects.all()
    )
    memoria = SlugRelatedField(
        slug_field='produto',
        queryset=Memoria.objects.all()
    )
    placa_de_video = SlugRelatedField(
        slug_field='produto',
        allow_null=True,
        queryset=Placa_de_video.objects.all()
    )

    class Meta:
        model = Monte_seu_pc
        fields = ['id', 'processador', 'placa_mae', 'memoria',
                  'quantidade_de_memoria', 'tamanho_da_memoria', 'placa_de_video']
        validators = [
            validator_marca_procesador,
            validacao_placa_de_video,
            validacao_quantidade_de_slots,
            validacao_quantidade_de_memoria,

        ]


class ProcessadorSerializer(ModelSerializer):
    class Meta:
        model = Processador
        fields = ['produto', 'marca']


class Placa_maeSerializer(ModelSerializer):
    class Meta:
        model = Placa_mae
        fields = ['produto', 'processadores_suportados',
                  'slots', 'memom_suportada', 'video_integrado']


class MemoriaSerializer(ModelSerializer):
    class Meta:
        model = Memoria
        fields = ['produto']


class Placa_de_videoSerializer(ModelSerializer):
    class Meta:
        model = Placa_de_video
        fields = ['produto']
