from ahmedjazzarcom import models


def ahmedjazzar(request):
    social_accounts = models.SocialAccount.objects.all()
    latest_posts = models.Blog.objects.order_by('-created')[:5]

    return {
        'social_accounts': social_accounts,
        'latest_posts': reversed(latest_posts)
    }
