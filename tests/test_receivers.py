from faker import Faker
import random
import string


from src.cloudtipsadp import Cloudtipsadp
from src.cloudtipsadp.clients import Connect, SandboxClient

connect = Connect(SandboxClient())
cta = Cloudtipsadp()

fake = Faker()
fake_ru = Faker('ru_RU')


def test_recipient_is_already_in_the_system_but_not_in_our_scope():
    """Получатель уже есть в системе, но не в нашем скоупе."""
    pass


def test_new_recipient_created():
    """Новый получатель создан."""
    gen_number = ''.join(random.choice(string.digits) for _ in range(10))
    phone_number = f'+7{gen_number}'
    name = fake_ru.name()
    ob = cta.receivers_create(cta.receivers(name, phone_number))
    assert phone_number == ob.get('data')['created'][0]['phoneNumber']
    assert name == ob.get('data')['created'][0]['name']


def test_recipient_is_already_in_the_system_and_is_in_your_scope_since():
    """
    Получатель уже есть в системе и находится в вашем скоупе,так как
    находится в массиве skipped.
    """
    response = {'data': {'created': [], 'skipped': [
        {'phoneNumber': '+79162047558', 'name': 'Adam',
         'userId': '44a38440-595d-494e-a028-09804355757a',
         'layoutId': '55757a3e', 'layoutStatus': 'None'}]}, 'succeed': True,
                'errors': None, 'validationErrors': None}
    ob = cta.receivers_create(cta.receivers('Adam', '+79162047558'))
    assert response == ob
