from rest_framework import viewsets
from monteseupc.models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class MonteseupcViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Monte_seu_pc.objects.all()
    serializer_class = MonteseupcSerializer

class ProcessadorViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer

class Placa_maeViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Placa_mae.objects.all()
    serializer_class = Placa_maeSerializer

class MemoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Memoria.objects.all()
    serializer_class = MemoriaSerializer

class Placa_de_videoViewSet(viewsets.ModelViewSet):

    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Placa_de_video.objects.all()
    serializer_class = Placa_de_videoSerializer

