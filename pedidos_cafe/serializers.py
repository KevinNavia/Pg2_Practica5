from rest_framework import serializers
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.factory import CafeFactory
from pedidos_cafe.builder import CafePersonalizadoBuilder, CafeDirector
from api_patrones.logger import Logger


class PedidoCafeSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCafe
        fields = [
            "id",
            "cliente",
            "tipo_base",
            "ingredientes",
            "tamanio",
            "fecha",
            "precio_total",
            "ingredientes_finales",
        ]

    def get_precio_total(self, obj):
        cafe = CafeFactory.crear_cafe(obj.tipo_base, obj.tamanio, obj.ingredientes)
        return cafe.calcular_precio()

    def get_ingredientes_finales(self, obj):
        cafe = CafeFactory.crear_cafe(obj.tipo_base, obj.tamanio, obj.ingredientes)
        return cafe.obtener_ingredientes()