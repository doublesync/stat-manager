from django.db import models
from .managers import DiscordAuthorizationManager

# Create your models here.
class DiscordUser(models.Model):
    objects = DiscordAuthorizationManager()
    id = models.BigIntegerField(primary_key=True, serialize=False)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)
    last_reward = models.DateTimeField(null=True)

    def is_authenticated(self, request):
        return True

    def __str__(self):
        return f"{self.discord_tag}"