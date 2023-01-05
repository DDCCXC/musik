from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio
async def disconnect(self, Inter:Interaction|Context):
        """ Disconnects the player from the voice channel and clears its queue. """
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=embed)
            return
        if not await self.vote_(Inter):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
            return
        if not player.is_playing:
            embed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
            return await Inter.send(embed=embed)
        if not player.is_connected:
            embed.title = 'เฮ้นายน่ะยังไม่ได้เข้าห้องเลยนะ'
            return await Inter.send(embed=embed)

        if not Inter.user.voice or (player.is_connected and Inter.user.voice.channel.id if type(Inter) is Interaction else Inter.author.voice.channel.id != int(player.channel_id)):
            embed.title = 'เฮ้นายน่ะต้องเข้าห้องเดียวกันฉันสิ ลองใหม่ดู'
            return await Inter.send(embed=embed)

        player.queue.clear()
        await player.stop()
        asyncio.create_task(self.connect_to(Inter.guild.id, None))
        embed.title = 'อะเคออกไปก็ได้'
        await Inter.send(embed=embed)

