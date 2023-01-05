import os,asyncio
import motor.motor_asyncio
def chack_database(clinent):
    try:
        clinent.admin.command("ismaster")
        print("!error")
    except:
        print("error")

if __name__ != "__main__":
    clinent= motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGOURI"), serverSelectionTimeoutMS=5000)
    database=clinent.ngan_song_kru
    guild=database.Guild
    lang=database.Language
    ll=database.lavalink