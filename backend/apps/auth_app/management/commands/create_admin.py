from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Создаёт базового суперюзера'

    def handle(self, *args, **kwargs):
        User = get_user_model()  # get the currently active user model,
        user = User.objects.create_superuser(
                username = 'admin',
                phone = '+79009009090',
                email = 'admin@forever.com',
                password = 'admin_forever'
            )
