from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,math

timeout= nextcord.embeds.Embed(title='⏱ หมดเวลาแล้วนะคะหนูขอตัวไปก่อนนะคะ' ,description ='ถ้ามีอะไรใช้คำสั่งax!hนะคะ')
class _btn(nextcord.ui.View):
        message:nextcord.Message
        def __init__(self,player,Member: nextcord.Member):
            self.player=player
            self.page=1
            self.Member= Member
            super().__init__(timeout=300)
        def set_message(self,message:nextcord.Message):
            self.message=message
        
        @nextcord.ui.button(label='◀', style=nextcord.ButtonStyle.green ,custom_id='ghgh')
        async def b(self,button: nextcord.ui.Button, interaction: nextcord.Interaction ):
                        emed = nextcord.Embed(color=0xff470b) 
                        items_per_page = 10
                        pages = math.ceil(len(self.player.queue) / items_per_page)
                        self.page-=1
                        if self.page == 0:
                            self.page=pages
                        start = (self.page - 1) * items_per_page
                        end = start + items_per_page
                        
                        
                        queue_list = ''
                        for index, track in enumerate(self.player.queue[start:end], start=start):
                            queue_list += f'**{index + 1}** : [**{track.title}**]({track.uri})\n'

                        embed = nextcord.Embed(colour=0xff470b,
                                            description=f'คิวเพลงทั้งหมด **{len(self.player.queue)} tracks**\n\n{queue_list}')
                       
                        embed.set_footer(text=f'คุณอยู่หน้าที่ {self.page}/{pages}')
                        await interaction.response.edit_message(embed = embed)
        @nextcord.ui.button(label='▶', style=nextcord.ButtonStyle.green ,custom_id='re')
        async def bt3(self,button: nextcord.ui.Button, interaction: nextcord.Interaction ):
            items_per_page = 10
            pages = math.ceil(len(self.player.queue) / items_per_page)
            self.page+=1
            if self.page == pages :
                self.page=1
            start = (self.page - 1) * items_per_page
            end = start + items_per_page
            
            
            queue_list = ''
            for index, track in enumerate(self.player.queue[start:end], start=start):
                queue_list += f'**{index + 1}** : [**{track.title}**]({track.uri})\n'

            embed = nextcord.Embed(colour=0xff470b,
                                description=f'คิวเพลงทั้งหมด **{len(self.player.queue)} tracks**\n\n{queue_list}')
            
            embed.set_footer(text=f'คุณอยู่หน้าที่ {self.page}/{pages}')
           
            await interaction.response.edit_message(embed = embed)
        @nextcord.ui.button(label='close', style=nextcord.ButtonStyle.danger ,custom_id='c')
        async def bt2(self,button: nextcord.ui.Button, interaction: nextcord.Interaction ):
            end = nextcord.embeds.Embed(title='ปิดแล้วนะคะ', description ="ถ้ามีอะไรใช้คำสั่งax!hนะคะ")
            end.set_author(name='Ax46 No.1',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR33qS-gzRAU86dahwFr1h29xsBDvw_o7rLOA&usqp=CAU')

            await interaction.response.edit_message(embed = end,view=None)
            self.stop()
        async def on_timeout(self):
            await self.message.edit(embed=timeout, view=None)
        async def interaction_check(self,interaction: nextcord.Interaction):
            if interaction.user != self.Member:
                await interaction.send(f'{interaction.user.mention}ใช้ของตัวเองสิคะ',ephemeral=True)
            else:
                return True
                        
async def queue(self, ctx: Interaction | Context):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if not player.queue:
            embed.title =f'คิวว่างจ้า'
            await ctx.send(embed=embed)
            return
        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)
        page=1
        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'**{index + 1}** : [**{track.title }**]({track.uri})\n'
        embed = nextcord.Embed(colour=0xff470b,description=f'คิวเพลงทั้งหมด **{len(player.queue)} tracks**\n\n{queue_list}')
        embed.set_footer(text=f'คุณอยู่หน้าที่ {page}/{pages}')
        btn=_btn(player,ctx.user if type(ctx) is Interaction else ctx.author)
        a=await ctx.send(embed=embed,view=btn)
        btn.set_message(a)
        return