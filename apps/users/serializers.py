from rest_framework import serializers

from . import models


class EmployeeStatisticsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')
    client_count = serializers.IntegerField(default=0)
    total_product_count = serializers.IntegerField(default=0)
    total_order_sum = serializers.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        model = models.Employee
        fields = (
            'id',
            "full_name",
            "client_count",
            "total_product_count",
            "total_order_sum",
        )


class ClientStatisticsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')
    total_bought_product_count = serializers.IntegerField(default=0)
    total_order_sum = serializers.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        model = models.Client
        fields = (
            'id',
            "full_name",
            "total_bought_product_count",
            "total_order_sum",
        )
