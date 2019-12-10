from rest_framework import viewsets
from monteseupc.models import Monte_seu_pc
from .serializers import MonteseupcSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class MonteseupcViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Monte_seu_pc.objects.all()
    serializer_class = MonteseupcSerializer