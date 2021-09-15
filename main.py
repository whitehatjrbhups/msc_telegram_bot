import telegram.ext
import constants as keys
import responses as R
import data as d

print("bot started...")


def start_command(update, context):
    nm = update.message.chat.first_name
    if (nm == None):
        nm = update.message.from_user.first_name
    res = "Hey " + nm + ",\nbot is online!\ntype /help to get started."
    update.message.reply_text(res)


def help_command(update, context):
    nm = update.message.chat.first_name
    if (nm == None):
        nm = update.message.from_user.first_name
    update.message.reply_text("hey " + nm + ",\n" + """Please use following commands to get the info:
/syllabus
/contacts
/schedule
/classlink
/ebooks
/help""")


def syllabus_command(update, context):
    update.message.reply_text("""Select subject to get the syllabus:
/DAA
/AI
/Data_Mining
/ANN
/Image_P
/Parallel_Comp
/Blockchain
/Tech_Writing""")


def contacts_command(update, context):
    update.message.reply_text("""Select teacher to get the contact details:
/S_Karthikeyan
/P_K_Mishra
/V_K_Singh
/G_Baranwal
/Ankita_Vaish
/S_Suresh
/Anshul_Verma
/Marisha""")


def schedule_command(update, context):
    # update.message.reply_text("Class schedule is:\nUnder construction...")
    update.message.reply_photo(
        "AgACAgUAAxkBAAO1YFnansFP9wsPMWsYEAlULna60v8AAgatMRuT49FWL3X5sSx-rLWgJqVvdAADAQADAgADbQADe-QCAAEeBA",
        "---- Class Schedule ----")


def classlink_command(update, context):
    update.message.reply_text("""Class links are:

DAA: https://meet.google.com/agd-jnty-yyx

ImgPrcsng: http://meet.google.com/nja-doei-mmo""")


def ebooks_command(update, context):
    update.message.reply_text("eBooks are:\nNo ebooks available right now...")


# ------------------------------SYLLABUS---------------------------------
def DAA_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAO9YFneoIKUfkGMHqcx8bBWFeGYtUcAAgutMRuT49FW49GCRzPyZFs93dltdAADAQADAgADbQADu-EEAAEeBA",
        "Syllabus: Design and Analysis of Algorithms")


def AI_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAO-YFne-fTi86WmO3JjhhzGzT0REs8AAgytMRuT49FWlOK6wQ_Uc23FtTJvdAADAQADAgADbQADFuYCAAEeBA",
        "Syllabus: Artificial Intelligence")


def Data_Mining_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAO_YFnf2A7yjLXO9ln9Q1rmrBJCj-8AAg2tMRuT49FWRmMJo8fsOCWa_UpzdAADAQADAgADbQADRiYAAh4E",
        "Syllabus: Data Mining")


def ANN_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAO7YFncT_G_Qy1DEG_i70RKr8Y_7z4AAgitMRuT49FWcBIAAbwZHv7_HzwhbXQAAwEAAwIAA20AA6yeBAABHgQ",
        "Syllabus: Artificial Neural Networks")


def Image_P_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAO6YFnb1ThetuIlfyqcjMSL0CXktYQAAgetMRuT49FWv6bdidhkanRei2VsdAADAQADAgADbQADes0HAAEeBA",
        "Syllabus: Image Processing")


def Parallel_Comp_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAPAYFngYXXOGPN6gSfC7eoI9r2XLpYAAg6tMRuT49FWB9znx9PJWqZKnW9zdAADAQADAgADbQADsiIAAh4E",
        "Syllabus: Parallel Computing")


def Blockchain_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAPBYFniG8EEiw2ss46nWsMXSxI1f9sAAhKtMRuT49FWQW17PDyq3f7n77VvdAADAQADAgADbQADfg4CAAEeBA",
        "Syllabus: BLockchain Technologies")


def Tech_Writing_command(update, context):
    update.message.reply_photo(
        "AgACAgUAAxkBAAO8YFncyPZ9YytsTwEaAfLX09IVRDwAAgmtMRuT49FWGw018xVh4sv2Vx1vdAADAQADAgADbQADZSwDAAEeBA",
        "Syllabus: Technical Writing and Seminar")


# ------------TEACHER'S_CONTACTS-----------------------
def S_Karthikeyan_command(update, context):
    update.message.reply_text(d.S_Karthikeyan, "MarkdownV2")


def P_K_Mishra_command(update, context):
    update.message.reply_text(d.P_K_Mishra, "MarkdownV2")


def V_K_Singh_command(update, context):
    update.message.reply_text(d.V_K_Singh, "MarkdownV2")


def G_Baranwal_command(update, context):
    update.message.reply_text(d.G_Baranwal, "MarkdownV2")


def Ankita_Vaish_command(update, context):
    update.message.reply_text(d.Ankita_Vaish, "MarkdownV2")


def S_Suresh_command(update, context):
    update.message.reply_text(d.S_Suresh, "MarkdownV2")


def Anshul_Verma_command(update, context):
    update.message.reply_text(d.Anshul_Verma, "MarkdownV2")


def Marisha_command(update, context):
    update.message.reply_text(d.Marisha, "MarkdownV2")


def handle_message(update, context):
    # test=str(update)
    # update.message.reply_text(test)
    text = str(update.message.text).lower()
    response = "Hey " + str(update.message.chat.first_name) + ",\n" + R.sample_responses(text)
    if (R.sample_responses(text) != ""):
        update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updator = telegram.ext.Updater(keys.API_KEY, use_context=True)
    dp = updator.dispatcher
    # -----------MAIN_COMMANDS----------------
    dp.add_handler(telegram.ext.CommandHandler("start", start_command))
    dp.add_handler(telegram.ext.CommandHandler("help", help_command))
    dp.add_handler(telegram.ext.CommandHandler("syllabus", syllabus_command))
    dp.add_handler(telegram.ext.CommandHandler("contacts", contacts_command))
    dp.add_handler(telegram.ext.CommandHandler("schedule", schedule_command))
    dp.add_handler(telegram.ext.CommandHandler("classlink", classlink_command))
    dp.add_handler(telegram.ext.CommandHandler("ebooks", ebooks_command))
    # ------------SYLLABUS------------------
    dp.add_handler(telegram.ext.CommandHandler("DAA", DAA_command))
    dp.add_handler(telegram.ext.CommandHandler("AI", AI_command))
    dp.add_handler(telegram.ext.CommandHandler("Data_Mining", Data_Mining_command))
    dp.add_handler(telegram.ext.CommandHandler("ANN", ANN_command))
    dp.add_handler(telegram.ext.CommandHandler("Image_P", Image_P_command))
    dp.add_handler(telegram.ext.CommandHandler("Parallel_Comp", Parallel_Comp_command))
    dp.add_handler(telegram.ext.CommandHandler("Blockchain", Blockchain_command))
    dp.add_handler(telegram.ext.CommandHandler("Tech_Writing", Tech_Writing_command))
    # ------------TEACHER'S_CONTACTS-----------------------
    dp.add_handler(telegram.ext.CommandHandler("S_Karthikeyan", S_Karthikeyan_command))
    dp.add_handler(telegram.ext.CommandHandler("P_K_Mishra", P_K_Mishra_command))
    dp.add_handler(telegram.ext.CommandHandler("V_K_Singh", V_K_Singh_command))
    dp.add_handler(telegram.ext.CommandHandler("G_Baranwal", G_Baranwal_command))
    dp.add_handler(telegram.ext.CommandHandler("Ankita_Vaish", Ankita_Vaish_command))
    dp.add_handler(telegram.ext.CommandHandler("S_Suresh", S_Suresh_command))
    dp.add_handler(telegram.ext.CommandHandler("Anshul_Verma", Anshul_Verma_command))
    dp.add_handler(telegram.ext.CommandHandler("Marisha", Marisha_command))

    dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    dp.add_error_handler(error)

    updator.start_polling()
    updator.idle()


if __name__ == '__main__':
    main()
