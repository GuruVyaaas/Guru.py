from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# बॉट टोकन
TOKEN = "7592523174:AAFPC-beyH5FodveealqM-7l70OttvsX1nE"

# "/start" कमांड का हैंडलर
async def start(update: Update, context: CallbackContext) -> None:
    message = (
        "🚀 *नमस्ते! मैं आपका Telegram Bot हूँ।*\n\n"
        "📊 *Stock Market से जुड़ी जानकारी और इन्वेस्टमेंट टिप्स के लिए मुझसे जुड़ें!*\n\n"
        "🔹 WhatsApp चैनल: [क्लिक करें](https://whatsapp.com/channel/0029VaxZVN0InlqRqAtMdE3V)\n"
        "🔹 Instagram प्रोफाइल: [यहाँ देखें](https://shorturl.at/kbdbW)\n"
        "🔹 Demat अकाउंट खोलें: [यहाँ क्लिक करें](https://instakyc.plindia.com/?RMCode=A534M1)\n\n"
        "📞 संपर्क करें: *गुरुबक्श व्यास* \n📍 स्थान: *बीकानेर, राजस्थान*\n📱 *मोबाइल:* 8209740180"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

# ऑटो-रिप्लाई हैंडलर
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()

    replies = {
        "stock market": "📈 *स्टॉक मार्केट अपडेट्स के लिए:* [WhatsApp चैनल](https://whatsapp.com/channel/0029VaxZVN0InlqRqAtMdE3V)",
        "investment tips": "💰 *इन्वेस्टमेंट टिप्स:* \n1️⃣ लंबी अवधि के लिए निवेश करें।\n2️⃣ हमेशा रिसर्च करें।\n3️⃣ रिस्क मैनेजमेंट का ध्यान रखें।",
        "whatsapp": "📢 *WhatsApp चैनल से जुड़ें:* [यहाँ क्लिक करें](https://whatsapp.com/channel/0029VaxZVN0InlqRqAtMdE3V)",
        "instagram": "📸 *मेरे Instagram प्रोफाइल पर विजिट करें:* [यहाँ देखें](https://shorturl.at/kbdbW)",
        "demat account": "📊 *Demat अकाउंट खोलें और ट्रेडिंग शुरू करें:* [अभी खोलें](https://instakyc.plindia.com/?RMCode=A534M1)",
        "market update": "📊 *आज का मार्केट अपडेट:* \n🔹 सेंसेक्स: 74,200 (-0.5%)\n🔹 निफ्टी 50: 22,300 (-0.3%)\n🔹 टॉप गेनर: रिलायंस, TCS\n🔹 टॉप लूजर: HDFC Bank, Infosys",
        "yes": "✅ *कृपया बताएं, आपको किस बारे में जानकारी चाहिए?* \n- Stock Market 📈\n- Investment Tips 💰\n- Market Update 📊\n- Demat Account 📑"
    }

    for keyword, reply in replies.items():
        if keyword in text:
            await update.message.reply_text(reply, parse_mode="Markdown")
            return

    # डिफ़ॉल्ट रिप्लाई (अगर कुछ समझ न आए)
    await update.message.reply_text("🤖 *मुझे समझ नहीं आया! क्या आप स्टॉक मार्केट, इन्वेस्टमेंट टिप्स, या मार्केट अपडेट के बारे में जानना चाहते हैं?*", parse_mode="Markdown")

# बॉट सेटअप और रन करने का फंक्शन
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
