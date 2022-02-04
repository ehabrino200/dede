from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
                         
                                , parse_mode='markdown', reply_markup=markup_help)
            else:
                bot.send_message(message.chat.id, text=f'*اشترك(@{ch}) واضغط (/start)*', parse_mode='markdown')
        else:
            bot.send_message(message.chat.id, text=f'*اشترك (@{req_channel}) واضغط (/start)*', parse_mode='markdown')

    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
