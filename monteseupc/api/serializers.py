from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField, HyperlinkedIdentityField, ValidationError
from monteseupc.models import *


def validator_marca_procesador(value):
    if str(value['placa_mae'].processadores_suportados) == "ambos":
        return value
    elif str(value['processador'].marca) != str(value['placa_mae'].processadores_suportados):
        raise ValidationError("Processador incompativel com a Placa Mãe")
    return value

def validacao_placa_de_video(value):
    if value['placa_mae'].video_integrado == False and value['placa_de_video'] == None:
        raise ValidationError("A placa mãe não possui video integrado, escolha uma placa de vídeo")
    return value

def validacao_quantidade_de_slots(value):
    if value['qnt_memoria'] > value['placa_mae'].slots:
        raise ValidationError('A Placa mãe so possui {} slots, selecione uma quantidade menor ou igual.'.format(value['placa_mae'].slots))
    return value
    


    



class MonteseupcSerializer(ModelSerializer):
    processador = SlugRelatedField(
        # many=True,
        slug_field='produto',
        queryset=Processador.objects.all()
     )
    placa_mae = SlugRelatedField(
        # many=True,
        slug_field='produto',
        queryset=Placa_mae.objects.all()
     )
    memoria = SlugRelatedField(
        # many=True,
        slug_field='produto',
        queryset=Memoria.objects.all()
     )
    placa_de_video = SlugRelatedField(
        # many=True,
        slug_field='produto',
        allow_null=True,
        queryset=Placa_de_video.objects.all()
     )

    class Meta:
        model = Monte_seu_pc
        fields = ['id','processador', 'placa_mae', 'memoria',
                  'qnt_memoria', 'tamanho_da_memoria', 'placa_de_video']
        validators = [
            validator_marca_procesador,
            validacao_placa_de_video,
            validacao_quantidade_de_slots
        ]