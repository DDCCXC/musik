from .. import player as pyer
from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord
async def join(self,ctx:Interaction|Context):
    if ctx.guild is  None:
        return False
    embed = nextcord.Embed(colour=0xdc4700)
        
    embed.title =f'joined'
    player = self.bot.lavalink.player_manager.create(ctx.guild.id)
    typeofctx=type(ctx) is Interaction
    author = ctx.user if typeofctx else ctx.author
    if not author.voice or not author.voice.channel:
            return False

    v_client =  ctx.guild.voice_client if ctx.guild.voice_client else None if typeofctx else ctx.voice_client 
    
    if not v_client:
        permissions = author.voice.channel.permissions_for((ctx.guild.me if ctx.guild is not None else self.bot.user)if typeofctx else ctx.me )
        if not permissions.connect or not permissions.speak:  # Check user limit too?
                return False
        player.store('channel', ctx.channel.id)
        ca=await author.voice.channel.connect(cls=pyer)
        await ctx.channel.guild.change_voice_state(channel=ca.channel, self_deaf=True)
        await ctx.send(embed=embed)
        return True
    else:
        if v_client.channel.id != author.voice.channel.id:
            return False

