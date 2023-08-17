from django.core.management import BaseCommand
from acl.models import *
from acl.permissions import PERMISSIONS, ROLE_CODES

SINGER_PERMS = [
    'music_list',
    'music_create',
    'music_edit',
    'music_delete',
    'music_detail',

    'album_list',
    'album_create',
    'album_edit',
    'album_delete',
    'album_detail',
]

USER_PERMS = [
    'music_list',
    'music_detail',

    'album_list',
    'album_detail',
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='clear old states and cities',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Role.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"CLEAR"))

        role, created = Role.objects.update_or_create(
            name='singer', code=ROLE_CODES.SINGER)
        role.permissions.set(Permission.objects.filter(code__in=SINGER_PERMS))

        role, created = Role.objects.update_or_create(
            name='user', code=ROLE_CODES.USER)
        role.permissions.set(Permission.objects.filter(code__in=USER_PERMS))
        self.stdout.write(self.style.SUCCESS(f"DONE..."))
