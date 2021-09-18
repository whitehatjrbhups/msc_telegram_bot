from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import constants as keys
import responses as R
import data as d
import files

print("bot started...")


def start_command(update, context):
    nm = update.message.chat.first_name
    if (nm == None):
        nm = update.message.from_user.first_name
    res = "Hey " + nm + ",\nMSc Assistant is online and contents have been updated for semester 3😊.\nTap /main_menu to get started.\nor type 'help' anytime to initiate the bot."
    update.message.reply_text(res)


def syllabus_command(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Machine Learning", callback_data='Machine_Learning'),
            InlineKeyboardButton("Compiler Design", callback_data='Compiler_Design'),
        ],
        [
            InlineKeyboardButton("Cloud Computing", callback_data='Cloud_Computing'),
            InlineKeyboardButton("Deep Learning", callback_data='Deep_Learning'),
        ],
        [
            InlineKeyboardButton("Info Retrieval", callback_data='Information_Retrieval'),
            InlineKeyboardButton("Minor Project", callback_data='Minor_Project'),
        ],
        [
            InlineKeyboardButton("Goto Main Menu ↩", callback_data='Main_Menu')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select the subject:', reply_markup=reply_markup)


def contacts_command(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Dr. S. Karthikeyan", callback_data='S_Karthikeyan'),
            InlineKeyboardButton("Dr. P.K. Mishra", callback_data='P_K_Mishra'),
        ],
        [
            InlineKeyboardButton("Dr. V.K. Singh", callback_data='V_K_Singh'),
            InlineKeyboardButton("Dr. G. Baranwal", callback_data='G_Baranwal'),
        ],
        [
            InlineKeyboardButton("Dr. Ankita Vaish", callback_data='Ankita_Vaish'),
            InlineKeyboardButton("Dr. S. Suresh", callback_data='S_Suresh'),
        ],
        [
            InlineKeyboardButton("Dr. Anshul Verma", callback_data='Anshul_Verma'),
            InlineKeyboardButton("Dr. Marisha", callback_data='Marisha'),
        ],
        [
            InlineKeyboardButton("Dean of Institute of Science", callback_data='Dean')
        ],
        [
            InlineKeyboardButton("Goto Main Menu ↩", callback_data="Main_Menu")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select the staff:', reply_markup=reply_markup)


def classlinks_command(update, context):
    update.message.reply_text("""
Google meet links:

Compiler Design: https://meet.google.com/wgy-jvgx-mpe

""", disable_web_page_preview=True)


def ebooks_command(update, context):
    keyboard = [
        [
            InlineKeyboardButton("1. Compilers- Aho, Ullman 2e", callback_data='pdf_1')
        ],
        [
            InlineKeyboardButton("---will be added soon---", callback_data='pdf_2')
        ],
        [
            InlineKeyboardButton("---will be added soon---", callback_data='pdf_3')
        ],
        [
            InlineKeyboardButton("---will be added soon---", callback_data='pdf_4')
        ],
        [
            InlineKeyboardButton("Goto Main Menu ↩", callback_data='Main_Menu')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def handle_message(update, context):
    nm = update.message.chat.first_name
    if (nm == None):
        nm = update.message.from_user.first_name
    text = str(update.message.text).lower()
    if text == 'help':
        update.message.reply_text("Hey " + nm + " i'm here to help you.")
        main_menu_command(update, context)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


# ------------------------------------------------------------------------------------
def main_menu_command(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Syllabus", callback_data='Syllabus'),
            InlineKeyboardButton("Contacts", callback_data='Contacts'),
        ],
        [
            InlineKeyboardButton("Class Schedule", callback_data='Schedule'),
            InlineKeyboardButton("Class Links", callback_data='Class_Links'),
        ],
        [
            InlineKeyboardButton("Ebooks", callback_data='Ebooks')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select the option:', reply_markup=reply_markup)


def button(update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "Main_Menu":
        main_menu_command(query, context)


    elif query.data == "Syllabus":
        syllabus_command(query, context)
    elif query.data == "Contacts":
        contacts_command(query, context)
    elif query.data == "Schedule":
        query.message.reply_photo(files.schedule, "---- Class Schedule ----")
    elif query.data == "Class_Links":
        classlinks_command(query, context)
    elif query.data == "Ebooks":
        ebooks_command(query, context)


    elif query.data == "Machine_Learning":
        query.message.reply_photo(files.machine_learning, "Syllabus: Machine Learning")
    elif query.data == "Compiler_Design":
        query.message.reply_photo(files.compiler_design, "Syllabus: Compiler Design")
    elif query.data == "Cloud_Computing":
        query.message.reply_photo(files.cloud_computing, "Syllabus: Cloud Computing")
    elif query.data == "Deep_Learning":
        query.message.reply_photo(files.deep_learning, "Syllabus: Deep Learning")
    elif query.data == "Information_Retrieval":
        query.message.reply_photo(files.informatiom_retrieval, "Syllabus: Information Retrieval")
    elif query.data == "Minor_Project":
        query.message.reply_photo(files.minor_project, "Syllabus: Minor Project")


    elif query.data == "S_Karthikeyan":
        query.message.reply_text(d.S_Karthikeyan, "MarkdownV2")
    elif query.data == "P_K_Mishra":
        query.message.reply_text(d.P_K_Mishra, "MarkdownV2")
    elif query.data == "V_K_Singh":
        query.message.reply_text(d.V_K_Singh, "MarkdownV2")
    elif query.data == "G_Baranwal":
        query.message.reply_text(d.G_Baranwal, "MarkdownV2")
    elif query.data == "Ankita_Vaish":
        query.message.reply_text(d.Ankita_Vaish, "MarkdownV2")
    elif query.data == "S_Suresh":
        query.message.reply_text(d.S_Suresh, "MarkdownV2")
    elif query.data == "Anshul_Verma":
        query.message.reply_text(d.Anshul_Verma, "MarkdownV2")
    elif query.data == "Marisha":
        query.message.reply_text(d.Marisha, "MarkdownV2")
    elif query.data == "Dean":
        query.message.reply_text(d.Dean, "MarkdownV2")


    elif query.data == "pdf_1":
        query.message.reply_document(files.pdf_1, "Book for Compiler Design")
    elif query.data == "pdf_2":
        query.message.reply_document(files.meme)
    elif query.data == "pdf_3":
        query.message.reply_document(files.meme)
    elif query.data == "pdf_4":
        query.message.reply_document(files.meme)


    else:
        query.message.reply_text("Something error...")
        print("invalid request")
    query.message.delete()
    # query.edit_message_text('Goto: /main_menu')


def main():
    updator = Updater(keys.API_KEY, use_context=True)
    dp = updator.dispatcher

    # -----------MAIN_COMMANDS----------------
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("main_menu", main_menu_command))

    dp.add_handler(CommandHandler("syllabus", syllabus_command))
    dp.add_handler(CommandHandler("contacts", contacts_command))
    dp.add_handler(CommandHandler("classlinks", classlinks_command))
    dp.add_handler(CommandHandler("ebooks", ebooks_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_error_handler(error)

    updator.start_polling()
    updator.idle()


if __name__ == '__main__':
    main()
