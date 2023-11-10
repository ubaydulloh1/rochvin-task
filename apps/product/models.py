from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.base.models import BaseModel


class Product(BaseModel):
    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    name = models.CharField(verbose_name=_("Name"), max_length=511)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=20, decimal_places=2, help_text=_("Price in sum."))

    def __str__(self):
        return f"{self.pk}. {self.name}"


class Order(BaseModel):
    class Meta:
        db_table = 'order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    client = models.ForeignKey(
        to="users.Client",
        verbose_name=_("Client"),
        on_delete=models.CASCADE,
        related_name='orders'
    )
    employee = models.ForeignKey(
        to="users.Employee",
        verbose_name=_("Employee"),
        on_delete=models.CASCADE,
        related_name='orders'
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to="Product",
        related_name='orders',
        through='OrderProduct',
        through_fields=('order', 'product')
    )
    total_price = models.DecimalField(
        verbose_name=_("Total price"),
        max_digits=20,
        decimal_places=2,
        help_text=_("Total price in sum.")
    )
    order_date = models.DateField(verbose_name=_("Order date"), auto_now_add=True)

    def __str__(self):
        return f"{self.pk}. {self.client.get_full_name()} -> {self.order_date}"


class OrderProduct(BaseModel):
    class Meta:
        db_table = 'order_product'
        verbose_name = _('Order product')
        verbose_name_plural = _('Order products')
        unique_together = ("order", "product")

    order = models.ForeignKey(
        to="Order",
        verbose_name=_("Order"),
        on_delete=models.CASCADE,
        related_name='order_products'
    )
    product = models.ForeignKey(
        to="Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name='order_products'
    )
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))

    def __str__(self):
        return f"{self.pk}. {self.order} -> {self.product}"
