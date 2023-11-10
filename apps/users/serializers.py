from rest_framework import serializers

from . import models


class EmployeeStatisticsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = models.Employee
        fields = (
            'id',
            "full_name",
        )


class ClientStatisticsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = models.Client
        fields = (
            'id',
            "full_name",
        )
