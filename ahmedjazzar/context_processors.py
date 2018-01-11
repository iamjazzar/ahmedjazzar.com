from ahmedjazzarcom import models


def ahmedjazzar(request):
    social_accounts = models.SocialAccount.objects.all()

    return {
        'social_accounts': social_accounts,
    }
