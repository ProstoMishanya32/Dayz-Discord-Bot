import nextcord
from nextcord import utils as nextcord_utils
from nextcord.ext.commands import Bot, Cog
from nextcord.ext import commands
from kernel import config


class MainButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @nextcord.ui.button(label = 'Создать сообщение', style = nextcord.ButtonStyle.red)
    async def mainbuttons(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        view = FirstButtton()
        emb = nextcord.Embed(
            title=f'**Введите Заголовок**',
            description = '*Затем нажмите на кнопу "Готово" для окончательного создания с выбраннами параметрами, или "Продолжить", чтобы продолжить создание сообщения*',
            colour=000000,
        )
        emb.set_footer(
            text=interaction.guild,
            icon_url=config.server.ul_image_server, )
        emb.set_image(config.embed.embed_welcome)
        await interaction.response.edit_message(embed=emb, view = view)
        self.value = True
        self.stop()


class FirstButtton(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label = 'Продолжить', style = nextcord.ButtonStyle.red)
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = interaction.channel
        message = await channel.fetch_message( channel.last_message_id) #Берем последнее сообщение Юзера
        self.value = True
        self.stop()
        await descrition(interaction, message.content)
    @nextcord.ui.button(label='Продолжить без заголовка', style=nextcord.ButtonStyle.green)
    async def not_title(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await descrition(interaction)
        self.value = True
        self.stop()
    @nextcord.ui.button(label = 'Готово', style = nextcord.ButtonStyle.grey)
    async def done(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        pass # Включение скрипта создания сообщения

async def descrition(interaction, content):
    if len(content) == 0:
        view = FirstButtton()
        emb = nextcord.Embed(
            title=f'**Похоже вы ничего не ввели**',
            description='*Повторите попытку\nВведите Заголовок*',
            colour=000000,
        )
        emb.set_footer(
            text=interaction.guild,
            icon_url=config.server.ul_image_server, )
        emb.set_image(config.embed.embed_welcome)
        await interaction.response.edit_message(embed=emb, view = view)
    else:
        view = SecondButtton()
        emb = nextcord.Embed(
            title=f'**Введите описание сообщения**',
            description='*Затем нажмите на кнопу "Готово" для окончательного создания с выбраннами параметрами, или "Продолжить", чтобы продолжить создание сообщения*',
            colour=000000,
        )
        emb.set_footer(
            text=interaction.guild,
            icon_url=config.server.ul_image_server, )
        emb.set_image(config.embed.embed_welcome)
        await interaction.response.send_message(embed=emb, view = view)
        #Заполнение заголовка в БД
class SecondButtton(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None


    @nextcord.ui.button(label = 'Продолжить', style = nextcord.ButtonStyle.red)
    async def next(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        channel = interaction.channel
        message = await channel.fetch_message( channel.last_message_id) #Берем последнее сообщение Юзера
        self.value = True
        self.stop()
        await descrition(interaction, message.content)
    @nextcord.ui.button(label='Продолжить без заголовка', style=nextcord.ButtonStyle.green)
    async def not_title(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await descrition(interaction)
        self.value = True
        self.stop()
    @nextcord.ui.button(label = 'Готово', style = nextcord.ButtonStyle.grey)
    async def done(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        pass # Включение скрипта создания сообщения