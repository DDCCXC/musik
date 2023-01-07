import os,asyncio
import motor.motor_asyncio
def chack_database(clinent):
    try:
        clinent.admin.command("ismaster")
        print("!error")
    except:
        print("error")

if __name__ != "__main__":
    CLINENT= motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGOURI"), serverSelectionTimeoutMS=5000)
    CLINENT.get_io_loop = asyncio.get_running_loop
    DATABASE=CLINENT.ngan_song_kru
    GUILD=DATABASE.Guild
    TONTON=DATABASE.tonton
