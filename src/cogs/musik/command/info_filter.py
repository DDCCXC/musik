import nextcord
import lavalink
async def check(self, ctx):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
       
        med = nextcord.Embed(color=0xff470b)
        if player is None:
            med.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=med)
            return
        med.title = 'check'
       
        med.add_field(name='volume', value=f'{player.volume}')
        for i,f in player.filters.items():
                v=''
                
                (_, filter), *_=f.serialize().items()
                
                
                if type(filter) == dict:
                        for x,y in  filter.items() :
                                v+=f"{x}: {y} "
                else:
                        for x in  filter:
                                v+=f"{x['band']}: {x['gain']} ,"
                med.add_field(name=i, value=f'{v}',inline=False)
        return await ctx.followup.send(embed=med)
        