from rest_framework import generics
from .models import Advantage, MenuItem
from .serializers import AdvantageSerializer, MenuItemSerializer

class AdvantageListCreateView(generics.ListCreateAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
