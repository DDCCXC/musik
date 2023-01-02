from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord
async def disconnect(self, Inter:Interaction|Context):
        """ Disconnects the player from the voice channel and clears its queue. """
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=emed)
            return
        if not player.is_playing:
            emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
            return await Inter.send(embed=emed)
        if not player.is_connected:
            emed.title = 'เฮ้นายน่ะยังไม่ได้เข้าห้องเลยนะ'
            return await Inter.send(embed=emed)

        if not Inter.user.voice or (player.is_connected and Inter.user.voice.channel.id if type(Inter) is Interaction else Inter.author.voice.channel.id != int(player.channel_id)):
            emed.title = 'เฮ้นายน่ะต้องเข้าห้องเดียวกันฉันสิ ลองใหม่ดู'
            return await Inter.send(embed=emed)

        player.queue.clear()
        await player.stop()
        await self.connect_to(Inter.guild.id, None)
        emed.title = 'อะเคออกไปก็ได้'
        await Inter.send(embed=emed)

