import nextcord,lavalink
# TODO repeat had update
async def repeat(self, Inter,type:int):
        player:lavalink.models.DefaultPlayer  = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=emed)
            return
        if not player.is_playing:
                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                return await Inter.send(embed=emed)
        player.set_loop(type)
        match type:
                case 0:emed.title = f'> 🔁 | loop : close'
                case 1:emed.title = f'> 🔁 | loop : {player.current.title}'
                case 2:emed.title = f'> 🔁 | loop : tracks'
        await Inter.send(embed=emed)