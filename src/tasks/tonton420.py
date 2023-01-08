from aiohttp import request 
import asyncio
from nextcord.ext.commands import AutoShardedBot
import nextcord,xmltodict
from flask import Flask,request as req
from threading import Thread
from waitress import serve
app = Flask('subwebsub')
class tonton:
    def __init__(self,api_key:str,tonton,guildcollet,bot:AutoShardedBot) -> None:
        self.ApiKey=api_key
        self.tonton=tonton
        self.guildcollet=guildcollet
        self.bot=bot
        self.embed=nextcord.Embed(color=0xdc4700).set_author(
            name="เฮ้ยไอต้นลงคลิปใหม่วะ"
        )
        @app.route("/callback", methods=['POST', 'GET'])
        async def callback():
            print("req")
            if req.method == 'POST':
                data = xmltodict.parse(req.data)
                if data['feed'].get('entry',None) is not None:
                    send_fut = asyncio.run_coroutine_threadsafe(self.send_to_guild_rised_tonton(data['feed']['entry']['yt:videoId']), self.bot.loop)
                    # wait for the coroutine to finish
                    send_fut.result()
                        
                return str(data)
            else:
                return str(req.args.get('hub.challenge'))
        
        server = Thread(target=self.run)
        server.start()
    def run(self):
        # app.run(host="0.0.0.0", port=8080)
        serve(app, host='0.0.0.0', port=80)
    # https://pubsubhubbub.appspot.com/
    # https://www.youtube.com/xml/feeds/videos.xml?channel_id=UC4PJv575xLDDwhlkWxai6_Q
    # รอของฟรี รอก็เหี้ยละกูมาแล้ว
    async def send_to_guild_rised_tonton(self,id):
        channel_rised_by_ton = self.guildcollet.find({"2tonton420.id_channel": { "$exists": True }})
        async with request('GET', f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={self.ApiKey}') as res:
            if res.status !=200:
                return None
            video= await res.json()
            founddata= await self.tonton.find_one({"id_video":id})
            if founddata is not None:
                if id ==founddata["id_video"]:
                    return None
            await self.tonton.insert_one({"id_video":id})
            
        async for i in channel_rised_by_ton:
            if (guild:=self.bot.get_guild(i["guild"])) is None:
                continue
            if (channel:=guild.get_channel(i["2tonton420"]["id_channel"])) is None:
                continue
            if len(video['items'])==0:
                return
            self.embed.title=f'{video["items"][0]["snippet"]["title"]}'
            self.embed.url=f"https://www.youtube.com/watch?v={id}"
            self.embed.description=video["items"][0]["snippet"]["description"]
            self.embed.set_image(f"https://i.ytimg.com/vi/{id}/hqdefault.jpg")
            self.embed.set_thumbnail("https://yt3.googleusercontent.com/GxhUzacPoU-7Kr_vmS38V59IuqgMZ9uhvhY7IcKqI35jwcRui1FwvlP12au9VJu8TTMku-ee=s176-c-k-c0x00ffffff-no-rj")
            self.embed.set_footer(
                text=video["items"][0]["snippet"]["publishedAt"],
                icon_url="https://www.youtube.com/s/desktop/a98f809d/img/favicon_144x144.png"
            )
            await channel.send(embed=self.embed)

