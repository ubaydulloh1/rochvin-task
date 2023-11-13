import factory
from apps.users.models import User, Client, Employee


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'test{n}@gmail.com')


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    user = factory.SubFactory(UserFactory)
    first_name = factory.Sequence(lambda n: f'first_name{n}')
    last_name = factory.Sequence(lambda n: f'last_name{n}')
    middle_name = factory.Sequence(lambda n: f'middle_name{n}')
    birth_date = factory.Faker('date')


class EmployeeFactory(ClientFactory):
    class Meta:
        model = Employee
