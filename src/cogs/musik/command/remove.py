import nextcord
async def remove(self, Inter, index: int):
        """ Removes an item from the player's queue with the given index. """
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if not await self.check_join(Inter,player):return 
        if not player.is_playing:
                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                return await Inter.send(embed=emed)
        

        if index > len(player.queue) or index < 1:
            emed.title = f'> **กรุณเลือกเพลงระหว่าง **between** 1 - {len(player.queue)}**'
            return await Inter.send(embed=emed)

        removed = player.queue.pop(index - 1)  # Account for 0-index.
        emed.title =f'> 🗑️ เพลง **{removed.title}** ได้ทำการถูกลบแล้ว'
        await  Inter.send(embed=emed)