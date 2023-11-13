import factory
from apps.users import factories as user_factories
from apps.product import models


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = factory.Sequence(lambda n: f'product{n}')
    quantity = factory.Faker('pyint')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    client = factory.SubFactory(user_factories.ClientFactory)
    employee = factory.SubFactory(user_factories.EmployeeFactory)
    total_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    ordered_at = factory.Faker('date_time_this_year', tzinfo=None)


class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.OrderProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('pyint')
