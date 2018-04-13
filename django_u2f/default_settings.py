from django.conf import settings


U2F_CHALLENGE_EXPIRATION = getattr(settings, 'U2F_CHALLENGE_EXPIRATION', 60)
