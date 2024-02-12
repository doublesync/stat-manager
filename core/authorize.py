from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser
from django.contrib.auth.models import User

class DiscordBackend(BaseBackend):
  def authenticate(self, request, user) -> DiscordUser:
    find_user: DiscordUser = DiscordUser.objects.filter(id=user['id'])
    if len(find_user) == 0:
      new_user: DiscordUser = DiscordUser.objects.create_new_discord_user(user)
      return new_user
    return find_user

  def get_user(self, user_id):
    try:
      return DiscordUser.objects.get(pk=user_id)
    except DiscordUser.DoesNotExist:
      return None