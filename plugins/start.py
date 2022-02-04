from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
# I Can See You !!
    do = requests.get(
        f"https://api.telegram.org/bot2087689939:AAFpKyW4R-UzwtR8sF0wp_DnKyxaStJyxQ8/getChatMember?chat_id=@animeeven&user_id={message.from_user.id}").text
    if do.count("left") or do.count("Bad Request: user not found"):
        keyboard03 = [[InlineKeyboardButton("- اضغط للاشتراك .", url='https://t.me/animeeven')]]
        reply_markup03 = InlineKeyboardMarkup(keyboard03)
        await message.reply_text('- اشترك بقناة البوت لتستطيع تشغيل الاغاني  .',
                                 reply_markup=reply_markup03)
    else:
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
