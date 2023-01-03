import nextcord
async def set_auto_play(self, Inter):
       
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=emed)
            return
        if not player.is_playing:
            emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
            return await Inter.send(embed=emed)
        
        player.auto_play = not player.auto_play 
        emed.title = f' | auto play :' + ('เปิดใช้งาน' if player.auto_play else 'ปิดใช้งาาน')
        await auto_play(self,player)
        await Inter.send(embed=emed)
        
async def auto_play(self,player):
      cache=self.cache if player.current is None else player.current
      results = await player.node.get_tracks(f"https://www.youtube.com/watch?v={cache.identifier}&list=RD{cache.identifier}") 
      self.cache=results['tracks'][1]
      player.add(requester=0, track=results['tracks'][1])