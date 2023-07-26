from pyrogram import Client, filters

# ->          [here]          <- #

Api = Api
Hash = Hash
Token = Token

ges = Client('ges', api_id=Api, api_hash=Hash, bot_token=Token)

@ges.on_message(filters.command("start"))
async def Start(ges, message):

    if message.from_user.first_name == 'reyan':
        await message.reply_text(
            f"reyan is smart and cool :)))",
        )

    else:
       await message.reply_text(
            f"{message.from_user.first_name} is,nt smart and cool ;(",
        ) 

ges.run()
