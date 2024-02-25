from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_urls: dict[str, str] = {
    "upgrade": "https://discord.com/api/webhooks/1210969397192032328/LUoSubn5hUy36jLc5tbqVyQSNUU7RW8-F4pQoyNBhrPJFn3e5bLBaWKGkiG5csbbQh6d",
    "cash": "https://discord.com/api/webhooks/1211369168687988756/g0qHmEl71ZMtNQ7JjohHsMH-Bz60Nk-CB4euzWus2SdK12F88wCDQKwpMdhnP5E186RD",
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
