import nextcord, lavalink
async def now(self, Inter):
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=emed)
            return
        if not player.is_playing:
            emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
            return await Inter.send(embed=emed)
        position = lavalink.utils.format_time(player.position)
        if player.current.stream:
            duration = '🔴 ไลฟ์'
        else:
            duration = lavalink.utils.format_time(player.current.duration)
        embed = nextcord.Embed(color=0xff470b,title='▶️ กำลังเล่นเพลง')
        embed.add_field(name='ชื่อเพลง',value=f'[{player.current.title}]({player.current.uri})',inline=False)
        embed.add_field(name='ศิลปิน',value=f'{player.current.author}',inline=False)
        embed.add_field(name='ระยะเวลา',value=f'{position} / {duration}',inline=False)
        embed.add_field(name='ผู้ขอเพลง',value=f'<@{self.bot.user.id if player.current.requester ==0 else player.current.requester}>',inline=False)
        embed.add_field(name='แหล่งที่มา',value=f'{player.current.source_name}',inline=False)
        if player.current.source_name== 'youtube':
            embed.set_thumbnail(url="https://img.youtube.com/vi/{}/maxresdefault.jpg".format(player.current.identifier))
        await Inter.send(embed=embed)