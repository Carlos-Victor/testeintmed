from rest_framework.serializers import ModelSerializer
from monteseupc.models import Monte_seu_pc


class MonteseupcSerializer(ModelSerializer):
    class Meta:
        model = Monte_seu_pc
        fields = ['processador', 'placa_mae', 'memoria',
                  'qnt_memoria', 'tamanho_da_memoria', 'placa_de_video', 'user']
