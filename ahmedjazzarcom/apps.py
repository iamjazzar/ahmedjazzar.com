import secretballot
from django.apps import AppConfig, apps


class AhmedjazzarcomConfig(AppConfig):
    name = 'ahmedjazzarcom'
    verbose_name = 'Ahmed Jazzar'

    def ready(self):
        blog_model = apps.get_model('ahmedjazzarcom', 'Blog')
        secretballot.enable_voting_on(blog_model)
