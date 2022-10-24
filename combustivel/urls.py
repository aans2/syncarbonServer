from django.urls import path

from combustivel.views import CombustivelConsumo

urlpatterns = [
    path('api/combustivel/add', CombustivelConsumo.as_view(), name='CombustivelConsumo')
]