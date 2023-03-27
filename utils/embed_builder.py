import discord

class EmbedBuilder:
    def __init__(self):
        self.embed = discord.Embed()

    def title(self, title):
        self.embed.title = title
        return self

    def description(self, description):
        self.embed.description = description
        return self

    def author(self, name=None, url=None, icon_url=None):
        self.embed.set_author(name=name, url=url, icon_url=icon_url)
        return self

    def footer(self, text=None, icon_url=None):
        self.embed.set_footer(text=text, icon_url=icon_url)
        return self

    def image(self, url):
        self.embed.set_image(url=url)
        return self

    async def send(self, ctx):
        await ctx.send(embed=self.embed)
