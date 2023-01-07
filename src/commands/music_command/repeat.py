import nextcord,lavalink
# TODO repeat had update
async def repeat(self, Inter,type:int):
        player:lavalink.models.DefaultPlayer  = self.bot.lavalink.player_manager.get(Inter.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=embed)
            return
        if await self.vote_(Inter):
            embed.title =f'ไม่เอิ้กๆ'
            await Inter.send(embed=embed)
            return
        if not player.is_playing:
                embed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                return await Inter.send(embed=embed)
        player.set_loop(type)
        match type:
                case 0:embed.title = f'> 🔁 | loop : close'
                case 1:embed.title = f'> 🔁 | loop : {player.current.title}'
                case 2:embed.title = f'> 🔁 | loop : tracks'
        await Inter.send(embed=embed)