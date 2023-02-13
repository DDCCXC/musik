from nextcord import Interaction,Embed,File
from random import choice
from string import ascii_letters
import nextcord
from captcha.image import ImageCaptcha
def random_char(y):
    return ''.join(choice(ascii_letters) for x in range(y))
class _btn(nextcord.ui.View):
    def __init__(self,db):
        super().__init__(timeout=None)
        self.database=db
        ...
    @nextcord.ui.button(label='hooman?', style=nextcord.ButtonStyle.green ,custom_id='hooman')
    async def b(self,button: nextcord.ui.Button, interaction: nextcord.Interaction ):
        captchaimg=ImageCaptcha(width=300,height=100)
        c=random_char(6)
        self.database.update_one({"guild": interaction.guild.id}, {"$set": {f"user.{interaction.user.id}":c}})
        embed=Embed(color=0xdc4700,title=f"พิมพ์อักษรที่เห็น")
        file_img=File(captchaimg.generate(c),filename=f"captcha.png")
        embed.set_image(url="attachment://captcha.png")
        await interaction.user.send(embed=embed,file=file_img)
        ...
async def set_room(type_channel:str,inter: Interaction,channel:nextcord.TextChannel|None,guild):
    if channel is None:
        channel_id= inter.channel_id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {type_channel:{"id_channel":channel_id}}})
    else:
        channel_id= channel.id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {type_channel:{"id_channel":channel_id}}})
    
    embed=Embed(color=0xdc4700,description=f"<#{channel_id}> set {type_channel} แล้วจ้า")
    await inter.send(embed=embed)
    
async def set_captcha(type_channel:str,inter: Interaction,channel:nextcord.TextChannel|None,captcha,guild):
    if channel is None:
        channel_id= inter.channel_id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {type_channel:{"id_channel":channel_id}}})
    else:
        channel_id= channel.id
        await guild.update_one({"guild": inter.guild.id}, {"$set": {type_channel:{"id_channel":channel_id}}})
    if await captcha.find_one({"guild": inter.guild.id}) is None:
            await captcha.insert_one({"guild":inter.guild.id})
    embed=Embed(color=0xdc4700,description=f"click ปุ่มถ้านายเป็นมนุยษ์")
    await inter.send(embed=embed,view=_btn(captcha))