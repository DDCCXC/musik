import nextcord,asyncio
async def set_auto_play(self, Inter):
       
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=embed)
            return
        if not await self.vote_(Inter):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
        if not player.is_playing:
            embed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
            return await Inter.send(embed=embed)
        
        player.auto_play = not player.auto_play 
        embed.title = f' | auto play :' + ('เปิดใช้งาน' if player.auto_play else 'ปิดใช้งาาน')
        asyncio.create_task(auto_play(self,player))
        await Inter.send(embed=embed)
        
async def auto_play(self,player):
      cache=self.cache if player.current is None else player.current
      results = await player.node.get_tracks(f"https://www.youtube.com/watch?v={cache.identifier}&list=RD{cache.identifier}") 
      if results['tracks'][1] is not None:
          self.cache=results['tracks'][1] 
      else :
          results = await player.node.get_tracks(f"https://www.youtube.com/watch?v=WTZ5VSmPU9Q&list=RDWTZ5VSmPU9Q") 
          self.cache=results['tracks'][1] 
      player.add(requester=0, track=results['tracks'][1])