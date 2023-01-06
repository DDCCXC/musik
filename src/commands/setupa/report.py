from nextcord import Interaction
import nextcord


class _btn(nextcord.ui.View):
        message:nextcord.Message
        def __init__(self,link):
            super().__init__()
            self.add_item(nextcord.ui.Button(label="This is the message", url=link))
async def report(self,inter: Interaction, message: nextcord.Message,guild):
    found_guild=await guild.find_one({"guild": inter.guild.id})
    embed=nextcord.Embed(color=0xdc4700)
    if message.author.id ==self.bot.user.id:
        embed.title="😾"
        await inter.send(embed=embed,ephemeral=True)
        return
    if message.author.id ==inter.user.id:
        embed.title="หำเล็ก?"
        await inter.send(embed=embed,ephemeral=True)
        return
    if found_guild.get("report",None) is None:
        embed.title="server นี้ยังไม่สร้างห้องreport"
        await inter.send(embed=embed,ephemeral=True)
        return
    
    if (channel:=inter.guild.get_channel(found_guild["report"]["id_channel"])) is  None:
        embed.title="ลบห้องหาแม่มึงอะ"
        return await inter.send(embed=embed,ephemeral=True)
    
    embed.title="Reported Message"
    embed.description=f"{message.content}"
    embed.set_author(
                icon_url=inter.user.avatar.url,
                name=inter.user.name
            )
    await channel.send(embed=embed,view=_btn(message.jump_url))