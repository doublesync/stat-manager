from django.db import models
from .managers import DiscordAuthorizationManager

# Create your models here.
class DiscordUser(models.Model):
    objects: any = DiscordAuthorizationManager()
    id: int = models.BigIntegerField(primary_key=True, serialize=False)
    discord_tag: str = models.CharField(max_length=100)
    avatar: str = models.CharField(max_length=100)
    public_flags: int = models.IntegerField()
    flags: int = models.IntegerField()
    locale: str = models.CharField(max_length=100)
    mfa_enabled: bool = models.BooleanField()
    last_login: str = models.DateTimeField(null=True)
    last_reward: str = models.DateTimeField(null=True)

    def is_authenticated(self, request) -> bool:
        return True

    def __str__(self) -> str:
        return f"{self.discord_tag}"