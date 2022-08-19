import telegram.ext
from googlesearch import search
import pandas_datareader as web


with open('key.txt','r') as f:
    key = f.read()
# print(key)

def google_search(a):
    query = a
    res=''
    count=1
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        res = res + '\n'+ str(count)+" "+j+"\n"
        count+=1
        if(count == 5):break
    return res

def start(update,context):
    update.message.reply_text('''Hello!! Welcome to the Classic World \n\n Here are the Available Commands
    
    /start -> Welcomes(This message)
    /help -> Discription + Commands
    /contact -> Contact Info''')

def help(update, context):
    update.message.reply_text('''Discription : 
Available Commands :

/start -> Welcomes
/help -> Commands Lists(This message)
/contact -> Contact Info
''')
def contact(update, context):
    update.message.reply_text('''You can contact me on Linkedin :
    
    "https://www.linkedin.com/in/naman-gupta-15baa1204?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BoQljD0%2F6TUeQPl0m2ll8mg%3D%3D"
    
    Email : namangupta78034@gmail.com
    ''')

def handlemessage(update, context):
    if (update.message.text == 'start') :
        start(update,"#")
    else:
        update.message.reply_text(f'''Googling .... ''')
        res= google_search(update.message.text)
        update.message.reply_text(f'''Top results :{res}''')

def stock(update,context) :
    try:
        ticker = context.args[0]
    except:
        update.message.reply_text("Please provide stock name in format '/stock stockname'")
        return
    try:
        data = web.DataReader(ticker,'yahoo')
        price = data.iloc[-1]['Close']
        print(data)
        update.message.reply_text(f'The current price of {ticker} is : {price} $ !!')
    except :
        update.message.reply_text('Something went wrong!! Please try again after some time \n\n Sorry for inconvienence')
    # ticker = context.args[0]
    # data = web.DataReader(ticker,'yahoo')
    # price = data.iloc[-1]['Close']
    # print(data)
    # update.message.reply_text(f'The current price of {ticker} is : {price} $ !!')
updater = telegram.ext.Updater(key, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handlemessage))

updater.start_polling()
updater.idle()