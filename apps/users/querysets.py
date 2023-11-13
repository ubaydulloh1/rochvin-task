from django.db import models


class EmployeeQueryset(models.QuerySet):
    def annotate_client_count(self, year, month):
        return self.annotate(
            client_count=models.Count(
                expression='orders__client',
                distinct=True,
                filter=models.Q(
                    orders__ordered_at__year=year,
                    orders__ordered_at__month=month,
                )
            )
        )

    def annotate_total_product_count(self, year, month):
        return self.annotate(
            total_product_count=models.Sum(
                'orders__order_products__quantity',
                filter=models.Q(
                    orders__ordered_at__year=year,
                    orders__ordered_at__month=month,
                )
            )
        )

    def annotate_total_order_sum(self, year, month):
        return self.annotate(
            total_order_sum=models.Sum(
                'orders__total_price',
                filter=models.Q(
                    orders__ordered_at__year=year,
                    orders__ordered_at__month=month,
                )
            )
        )


class ClientQueryset(models.QuerySet):
    def annotate_total_bought_product_count(self, year, month):
        return self.annotate(
            total_bought_product_count=models.Sum(
                'orders__order_products__quantity',
                filter=models.Q(
                    orders__ordered_at__year=year,
                    orders__ordered_at__month=month,
                )
            )
        )

    def annotate_total_order_sum(self, year, month):
        return self.annotate(
            total_order_sum=models.Sum(
                'orders__total_price',
                filter=models.Q(
                    orders__ordered_at__year=year,
                    orders__ordered_at__month=month,
                )
            )
        )
