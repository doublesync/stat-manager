from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser
from django.contrib.auth.models import User

class DiscordBackend(BaseBackend):
  def authenticate(self, request, user) -> DiscordUser:
    findUser: DiscordUser = DiscordUser.objects.filter(id=user['id'])
    if len(findUser) == 0:
      newUser: DiscordUser = DiscordUser.objects.createDiscordUser(user)
      return newUser
    return findUser

  def get_user(self, user_id):
    try:
      return DiscordUser.objects.get(pk=user_id)
    except DiscordUser.DoesNotExist:
      return None