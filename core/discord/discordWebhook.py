from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_urls: dict[str, str] = {
    "upgrade": "https://discord.com/api/webhooks/1212877354213445702/IaPkjxax2gWqTSBYEQrqC4A1ebOD1GA1tSIbPcsOqPijHW6z3xr1RaMtpDa8TDZolADQ",
    "cash": "https://discord.com/api/webhooks/1212877633046446210/dbZH4oNTMbJcFN4J2eOmwn55cNNjoJnFnz1usi0VSfQ6iQCK4sgTOjZZQDfqpdIjp3de",
}

default_webhook_msg: str = "Webhook test message"


def send_webhook(url, title="", message=""):
    webhook: any = DiscordWebhook(url=webhook_urls[url])
    webhookEmbed: any = DiscordEmbed(title=title, description=message, color="03b2f8")
    webhookEmbed.set_timestamp()
    webhookEmbed.set_footer(text="Powered by The Association")
    webhookEmbed.set_author(
        name="Association Assistant",
        url="https://stat-manager-8e8740f61676.herokuapp.com/basketball/player/50/",
        icon_url="https://cdn-icons-png.freepik.com/512/180/180658.png",
    )
    webhook.add_embed(webhookEmbed)
    webhook.execute()
