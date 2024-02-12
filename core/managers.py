from django.contrib.auth import models

class DiscordAuthorizationManager(models.UserManager):
    def createDiscordUser(self, user) -> dict:
        new_user: object = self.create(
            id=user["id"],
            discord_tag=user["username"],
            avatar=user["avatar"],
            public_flags=user["public_flags"],
            flags=user["flags"],
            locale=user["locale"],
            mfa_enabled=user["mfa_enabled"],
        )
        return new_user