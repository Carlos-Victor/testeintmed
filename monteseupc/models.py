from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
# Create your models here.



processadores = [
    ('INTEL', 'Intel'),
    ('AMD', 'Amd'),
    ('ambos', 'Intel e AMD'),
]
slots_suportado = [
    ('1', '1'),
    ('2', '2'),
]
memoria_suportada = [
    ('1', '8'),
    ('2', '12'),
    ('3', '16'),
    ('4', '32'),
    ('5', '64'),
]

tamanho_memorias = [
    ('1', '4'),
    ('2', '8'),
    ('3', '16'),
    ('4', '32'),
    ('5', '64'),
]

class Monte_seu_pc(models.Model):
    user = get_user_model()
    processador = models.ForeignKey("Processador", verbose_name=("Processador"), on_delete=models.CASCADE)
    placa_mae = models.ForeignKey("Placa_mae", verbose_name=("Placa mae"), on_delete=models.CASCADE)
    Memoria = models.ForeignKey("Memoria", verbose_name=("Memoria Ram"), on_delete=models.CASCADE)
    qnt_memoria = models.IntegerField("Quantidade de Memoria", validators=[MinValueValidator(1),MaxValueValidator(4)])
    tamanho_da_memoria = models.CharField("Tamanho da Memoria",choices=tamanho_memorias, max_length=50)
    placa_de_video = models.ForeignKey("Placa_de_video", verbose_name=("Placa de Video"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")
        def __str__(self):
            return self.user
    
class Processador(models.Model):
    produto = models.CharField("Produto", max_length=50)
    marca = models.CharField("Marca", choices=processadores,max_length=50)
    def __str__(self):
        return self.produto

class Placa_mae(models.Model):
    produto = models.CharField("Produto", max_length=50)
    processadores_suportados = models.CharField("Processador Suportado", choices=processadores,max_length=50)
    slots = models.IntegerField("Quantidade de Slots", choices=slots_suportado)
    memom_suportada = models.IntegerField("Quantidade de Slots", choices=memoria_suportada)
    video_integrado = models.BooleanField("Video integrado", default=True)
    def __str__(self):
        return self.produto

class Memoria(models.Model):
    produto = models.CharField("Produto", max_length=50)
    def __str__(self):
        return self.produto

class Placa_de_video(models.Model):
    produto = models.CharField("Produto", max_length=50)
    def __str__(self):
        return self.produto




