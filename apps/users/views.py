from rest_framework import generics
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from . import models, serializers, permissions

month_year_manual_parameters = [
    openapi.Parameter(
        name='year',
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description='Year',
        required=True
    ),
    openapi.Parameter(
        name='month',
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description='Month',
        required=True,
        enum=list(range(1, 13))
    )
]


class EmployeeStatisticsView(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()  # noqa
    serializer_class = serializers.EmployeeStatisticsSerializer
    permission_classes = (permissions.IsSuperUser,)

    def get_queryset(self):
        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)
        qs = self.queryset.annotate_client_count(year, month)
        qs = qs.annotate_total_product_count(year, month)
        qs = qs.annotate_total_order_sum(year, month)
        return qs

    @swagger_auto_schema(manual_parameters=month_year_manual_parameters)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EmployeeStatisticsListView(generics.ListAPIView):
    queryset = models.Employee.objects.all()  # noqa
    serializer_class = serializers.EmployeeStatisticsSerializer
    permission_classes = (permissions.IsSuperUser,)

    def get_queryset(self):
        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)

        qs = self.queryset.annotate_client_count(year, month)
        qs = qs.annotate_total_product_count(year, month)
        qs = qs.annotate_total_order_sum(year, month)
        return qs

    @swagger_auto_schema(manual_parameters=month_year_manual_parameters)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ClientStatisticsView(generics.RetrieveAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientStatisticsSerializer
    permission_classes = (permissions.IsSuperUser,)

    def get_queryset(self):
        year = self.request.query_params.get('year', timezone.now().year)
        month = self.request.query_params.get('month', timezone.now().month)
        qs = self.queryset.annotate_total_bought_product_count(year, month)
        qs = qs.annotate_total_order_sum(year, month)
        return qs

    @swagger_auto_schema(manual_parameters=month_year_manual_parameters)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
