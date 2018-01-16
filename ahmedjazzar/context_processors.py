from django.conf import settings

from ahmedjazzarcom import models


def ahmedjazzar(request):
    social_accounts = models.SocialAccount.objects.all()
    latest_posts = models.Blog.get_ready().order_by('-created')[:3]

    return {
        'is_debug': settings.DEBUG,
        'social_accounts': social_accounts,
        'latest_posts': latest_posts
    }
