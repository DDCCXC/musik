import nextcord
import lavalink
async def check(self, ctx):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        med = nextcord.Embed(color=0xff470b)
        med.title = 'check'
        '''print(f'player:{dir(player)}')'''
        #med.add_field(name='player',value=f'player:{dir(player)}')
        med.add_field(name='volume', value=f'{player.volume}')
        med.add_field(name='bassboost', value=f'{player.filters}',inline=False)

        # med.add_field(name='speed', value=f'{player.speed}',inline=False)
        # med.add_field(name='pitch', value=f'{player.pitch}',inline=False)
        # med.add_field(name='rate', value=f'{player.rate}',inline=False)

        # med.add_field(name='level', value=f'{player.level}',inline=False)
        # med.add_field(name='monoLevel', value=f'{player.monoLevel}',inline=False)
        # med.add_field(name='filterBand', value=f'{player.filterBand}',inline=False)
        # med.add_field(name='filterWidth', value=f'{player.filterWidth}',inline=False)

        # #self.smoothing =20.0
        # med.add_field(name='depth', value=f'{player.depth}',inline=False)
        # med.add_field(name='frequency', value=f'{player.frequency}',inline=False)
        # med.add_field(name='smoothing', value=f'{player.smoothing}',inline=False)
        await ctx.send(embed=med)