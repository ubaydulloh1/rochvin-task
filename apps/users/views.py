from rest_framework import generics
from . import models, serializers, permissions


class EmployeeStatisticsView(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeStatisticsSerializer
    permission_classes = (permissions.IsSuperUser,)


class ClientStatisticsView(generics.RetrieveAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientStatisticsSerializer
    permission_classes = (permissions.IsSuperUser,)
