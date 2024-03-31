import discord
import asyncio

class DiscordReader(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = None

    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        self.message = message

    async def get_message(self):
        while self.message is None:
            await asyncio.sleep(1)
        message = self.message
        self.message = None
        return message

    async def get_message_content(self):
        message = await self.get_message()
        return message.content

    async def get_message_author(self):
        message = await self.get_message()
        return message.author

    async def get_message_channel(self):
        message = await self.get_message()
        return message.channel

    async def get_message_attachments(self):
        message = await self.get_message()
        return message.attachments

    async def get_message_embeds(self):
        message = await self.get_message()
        return message.embeds

    def get_text(self, filters):
        msg = self.get_message_content()
        author = self.get_message_author()
        if author in filters['excluded_users']:
            return None
        return msg