from twitchio.ext import commands
from playsound import playsound
from random import randint

saludos=('¡Hola','¡Buenas','¡Saludos')

class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(token='uqwt7hzqp8lvqu5telzn06hwysvwn7', prefix='!', initial_channels=['iamkauz'])
        
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print(f'¡Conectado a Twitch como {self.nick}!')
        
        for channel in self.initial_channels:
            await self.send_welcome_message(channel)
    
    async def event_message(self, message):
        if message.echo:
            return
        author = message.author.name
        content = message.content
        print(f"{author}: {content}")
        await self.handle_commands(message)

    

    async def event_join(self, channel, user):
        try:
            await channel.send(saludos[randint(0,2)]+ f" {user.name}, bienvenido al canal!")
        except Exception as e:
            print(f"Error al enviar mensaje de bienvenida: {e}")


    async def send_welcome_message(self, channel):
        await self.get_channel(channel).send(f"¡Bienvenido al canal, @{self.nick} está aquí para ayudarte!")
    



    
    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello, {ctx.author.display_name}!")
        
    @commands.command(name="gg")
    async def gg(self, ctx: commands.Context):
        await ctx.send(f"GG activado por: {ctx.author.display_name}!")
        playsound('GG.mp3')
    
    @commands.command(name="f")
    async def f(self, ctx: commands.Context):
        await ctx.send(f"F activado por: {ctx.author.display_name}!")
        playsound('ReZeroSound.ogg')

bot = Bot()
bot.run()
