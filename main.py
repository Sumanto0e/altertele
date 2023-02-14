import time
import json
import telebot
from telebot import types

##TOKEN DETAILS
TOKEN = "ONS"

BOT_TOKEN = "6085237041:AAH5Ia9gk9W5WgNFpkYV7xX71q5MOUQFiTs"
OWNER_ID = 5458705482 #write owner's user id here.. get it from @MissRose_Bot by /id
CHANNELS = ["@ONSBASEE", "@onsbase_grub", "@menfesonsbase"] #add channels to be checked here in the format - ["Channel 1", "Channel 2"]
BASE = "@ONSBASEE"
LINKKEDDD = "https://t.me/ONSBASEE"
PANTAU = "@pantauaja1"
Daily_bonus = 3 #Put daily bonus amount here!
Mini_Withdraw = 1000  #remove 0 and add the minimum withdraw u want to set
Daily_bonuss = 1000000000000
ROLEL = 5000
TAG = ["#onsgirl", "#onsboy", "#onsrate"]
CEWE = ["#onsgirl"]
COWO = ["#onsboy"]
KATAAAA = ["link", "bio", "18+", "open", "tf", "pulsa", "order", "open", "op3nvcsss", "vcs", "vip", "v1p", "v!p", "vc$", "byo"]
COSTT = 1
COST = 5
BANNEDD = 1500
SANKSI = 150
ma = types.InlineKeyboardMarkup
bb = types.InlineKeyboardButton


bot = telebot.TeleBot(BOT_TOKEN)

def check(id):
    for i in CHANNELS:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True
bonus = {}

def cukis(id):
    for i in BASE:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True
bonus = {}

@bot.message_handler(commands=['start'])
def start(message):
   try:
    user = message.chat.id
    msg = message.text
    with open("lolot.db", "a+") as file:
		    file.seek(0)
		    value = str(user)
		    lines = file.read().splitlines()
		    if value in lines:
			    pass
		    else:
			    file.write(value + "\n")
    if msg == '/start':
        user = str(user)
        data = json.load(open('users.json', 'r'))
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['DailyQuiz']:
            data['DailyQuiz'][user] = "0"
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        if user not in data['id']:
            data['id'][user] = user
        if user not in data['pict']:
            data['pict'][user] = ""
        json.dump(data, open('users.json', 'w'))
        print(data)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
           text='🤼‍♂️ Joined', callback_data='check'))
        msg_start = "*🍔 To Use This Bot You Need To Join This Channel -"
        for i in CHANNELS:
            msg_start += f"\n\n➡️ {i}\n"
        msg_start += "*"
        bot.send_message(user, msg_start,
                         parse_mode="Markdown", reply_markup=markup)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
   try:
    ch = check(call.message.chat.id)
    if call.data == 'check':
        if ch == True:
            data = json.load(open('users.json', 'r'))
            user_id = call.message.chat.id
            user = str(user_id)
            bot.answer_callback_query(
                callback_query_id=call.id, text='✅ Wellcome to One Night Stand BASE')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            yamete = ma(row_width=1)
            rawri = bb(text="RULES", url="https://t.me/onsbasee/5366")
            yamete.add(rawri)
            bot.send_message(user_id, "!!!*Selamat datang di ONS BASE TELEGRAM*!!!\n\n➡️ Gunakan Hastag Untuk mengirim pesan\n\n#onsgirl\n#onsboy\n#onsrate\n\nDapatkan daily post harian untuk send promote = /ambilbonus", parse_mode="markdown", reply_markup=yamete)

        else:
            bot.answer_callback_query(
                callback_query_id=call.id, text='❌ You not Joined')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(
                text='🤼‍♂️ Joined', callback_data='check'))
            msg_start = "*🍔 To Use This Bot You Need To Join This Channel -\n\n➡️ @ONSBASEE\n\n➡️ @menfesonsbase\n\n➡️ @onsbase_grub*"
            bot.send_message(call.message.chat.id, msg_start,
                             parse_mode="Markdown", reply_markup=markup)
   except:
        bot.send_message(call.message.chat.id, "You must join channel the first")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+call.data)
        return

@bot.message_handler(commands=['banned'], chat_types=["private"])
def banned(message):
   try:
    if message.text == '/banned':
        user_id = message.chat.id
        if (user_id == OWNER_ID):
            anjim = bot.send_message(user_id, "Siapa yang mau diban ? ")

            bot.register_next_step_handler(
                anjim, banned)
        else:
            bot.send_message(
                message.chat.id, "❌*You not admin!*",parse_mode="markdown")
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)

@bot.message_handler(commands=['getcoin'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/getcoin':
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        #bot.send_message(user_id, "*🎁 Bonus Button is Under Maintainance*", parse_mode="Markdown")
        if (user_id == OWNER_ID):
            data['balance'][(user)] += Daily_bonuss
            bot.send_message(
                user_id, f"Congrats you just received {Daily_bonuss} {TOKEN}")
            json.dump(data, open('users.json', 'w'))
        else:
            bot.send_message(
                message.chat.id, "❌*You not admin!*",parse_mode="markdown")

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return
@bot.message_handler(commands=['topup'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/topup':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=1)
        rawr = bb(text="BELI COIN", url="https://trakteer.id/nazhak-tv-dfbf2/tip?open=true")
        yamete.add(rawr)

        bot.send_message(
                user_id, "Format untuk pembelian Coin ONS ini *ID* dan *USERNAME* anda dikolom *'pesan dukungan'*.\n\nCost ⦂ 1000 ONS = Rp.1000\n\nKami akan mengirimkan coin sesuai dengan jumlah unit yang anda berikan\n\nnote: bila *ID* dan *USERNAME* tidak dicantumkan kami anggap sebagai *DONASI*\n\n      ⬇️ CLICK BOTTON DIBAWAH ⬇️", parse_mode="markdown", reply_markup=yamete)


   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['paidpromote'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/paidpromote':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=1)
        rawr = bb(text="CONTACT", url="https://t.me/lolot0")
        rawri = bb(text="CALENDER", url="https://t.me/ratemyonspartner/14")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "Format untuk Paid Promote\nCost ⦂ 1k/24jam\n\n•────────𓆩𓆩𓆪────────•\n\n◝.🍑 𓄹 ࣪. Username    ⦂\n◝.🍑 𓄹 ࣪. Tanggal        ⦂\n◝.🍑 𓄹 ࣪. Payment      ⦂\n◝.🍑 𓄹 ࣪. Berapa Jam ⦂\n◝.🍑 𓄹 ࣪. Di LPM          ⦂\n\n•────────𓆩𓆩𓆪────────•\n\n             ⬇️ Kirim Ke ⬇️", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['model'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/model':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=2)
        rawr = bb(text="VOTE", url="https://t.me/donasionsbot")
        rawri = bb(text="LIST VOTE", url="https://t.me/onsbasee/5429")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "*Belum ada yang mendaftar, daftarkan diri anda ke @lolot0*", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return


@bot.message_handler(commands=['comedy'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/comedy':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=2)
        rawr = bb(text="VOTE", url="https://t.me/donasionsbot")
        rawri = bb(text="LIST VOTE", url="https://t.me/onsbasee/6777")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "*Belum ada yang mendaftar, daftarkan diri anda ke @lolot0*", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['singer'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/singer':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=2)
        rawr = bb(text="VOTE", url="https://t.me/donasionsbot")
        rawri = bb(text="LIST VOTE", url="https://t.me/onsbasee/5374")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "*Belum ada yang mendaftar, daftarkan diri anda ke @lolot0*", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['puitis'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/puitis':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=2)
        rawr = bb(text="VOTE", url="https://t.me/donasionsbot")
        rawri = bb(text="LIST VOTE", url="https://t.me/onsbasee/5374")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "*Belum ada yang mendaftar, daftarkan diri anda ke @lolot0*", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and tezt /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['donasi'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/donasi':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=2)
        rawr = bb(text="TRAKTEER", url="https://trakteer.id/nazhak-tv-dfbf2/post/ons-base-vOVbB")
        rawri = bb(text="SAWERIA", url="https://saweria.co/nazhak")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "⬇️ Berikan tips di sini ⬇️", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

@bot.message_handler(commands=['pengaturan'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/pengaturan':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=2)
        rawr = bb(text="HELP", url="https://t.me/menfesonsbase/284")
        rawri = bb(text="RULES", url="https://t.me/onsbasee/5366")
        yamete.add(rawr, rawri)

        bot.send_message(
                user_id, "👉 /setpict - untuk set/menganti profil akun kamu\n👉 /setrole - untuk set/mengati role kamu\n👉 /transfer - untuk transfer koin kamu ke penguna lain\n👉 /ambilbonus - untuk dapatkan koin harian gratis", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return


@bot.message_handler(commands=['profil'], chat_types=["private"])
def start(message):
   try:
    if message.text == '/profil':
        user_id = message.chat.id
        user = str(user_id)
        yamete = ma(row_width=1)
        rawri = bb(text="RULES", url="https://t.me/onsbasee/5366")
        yamete.add(rawri)

        bot.send_message(
                user_id, "👉 /account - untuk cek profil akun kamu\n👉 /setpict - untuk set/menganti profil akun kamu\n👉 /setrole - untuk set/mengati role kamu\n👉 /transfer - untuk transfer koin kamu ke penguna lain\n👉 /ambilbonus - untuk dapatkan koin harian gratis", parse_mode="markdown", reply_markup=yamete)

   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return


@bot.message_handler(commands= ["bc"])
def cast(message):
    idu = message.from_user.id
    t = message.text.replace("/bc", "")
    f = open("lolot.db", "r")
    for idu in f:
        bot.send_message(idu, text="{}".format(t))

@bot.message_handler(commands=['ping'], chat_types=["private"])
def ping(message):
   try:
    if message.text == '/ping':
        user_id = message.chat.id
        total = len(open("lolot.db", "r").readlines())
        pong = f"Bot Aktif !!!!\nTotal Pengguna Bot : {total}"
        bot.send_message(
                user_id, pong)
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)

@bot.message_handler(commands=['account', 'setrole', 'transfer', 'ambilbonus', 'setpict'], chat_types=["private"])
def ping(message):
    if message.text == '/account':
        data = json.load(open('users.json', 'r'))
        accmsg = '*👮 User : *`{}`*\n\n🆔 ID : *`{}`*\n\n👑 Role : *`{}`*\n\n💸 Coin : *`{}`* {}\n\n📆 Daily Post : *`{}`**'
        user_id = message.chat.id
        user = str(user_id)
        ID = int(user_id)

        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        if user not in data['pict']:
            data['pict'][user] = ""
        if user not in data['checkin']:
            data['checkin'][user] = 0
        json.dump(data, open('users.json', 'w'))

        balance = data['balance'][user]
        wallet = data['wallet'][user]
        pict = data['pict'][user]
        bounuz = data['checkin'][user]

        msg = accmsg.format(message.from_user.first_name, user,
                            wallet, balance, TOKEN, bounuz)
        if len(pict) == 0:
                bot.send_message(message.chat.id, msg, parse_mode="Markdown")

        if len(pict) >= 3:
                bot.send_photo(message.chat.id, ""+data['pict'][user]+f"", msg, parse_mode="Markdown")


    if message.text == "/setrole":
        user_id = message.chat.id
        user = str(user_id)

        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= ROLEL:
            bot.send_message(user_id, "_⚠️Set role anda. Tolong jangan tambahkan karakter apapun misal (#,@,!,$)!!! cukup dengan text dan emot saja⚠️_",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, lol_address)
        else:
            bot.send_message(
                user_id, f"_❌Koin anda kurang, setidaknya memiliki {ROLEL} {TOKEN} untuk transfer_", parse_mode="Markdown")

    if message.text == "/setpict":
        user_id = message.chat.id
        user = str(user_id)

        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        if bal >= ROLEL:
            bot.send_message(user_id, "_⚠️Set pict anda. Kirim berupa url, chat @lolot0 untuk konfirmasi pict terlebih dahulu ⚠️_",
                             parse_mode="Markdown", reply_markup=keyboard)
            bot.register_next_step_handler(message, suman_pict)
        else:
            bot.send_message(
                user_id, f"_❌Koin anda kurang, setidaknya memiliki {ROLEL} {TOKEN} untuk transfer_", parse_mode="Markdown")

    if message.text == "/transfer":
        user_id = message.chat.id
        user = str(user_id)


        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['wallet']:
            data['wallet'][user] = "none"
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        wall = data['wallet'][user]
        if wall == "none":
            bot.send_message(user_id, "_❌ Set role terlebih dahulu_",
                             parse_mode="Markdown")

        if bal >= Mini_Withdraw:
            bot.send_message(user_id, "_masukan jumlahnya!!_",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, amo_with)

        else:
            bot.send_message(
                user_id, f"_❌Koin kamu kurang setidaknya memiliki {Mini_Withdraw} {TOKEN} untuk transfer_", parse_mode="Markdown")

    if message.text == "/ambilbonus":
        user_id = message.chat.id
        user = str(user_id)
        cur_time = int((time.time()))
        data = json.load(open('users.json', 'r'))
        #bot.send_message(user_id, "*🎁 Bonus Button is Under Maintainance*", parse_mode="Markdown")

        if user not in data['wallet']:
            data['wallet'][user] = "none"

        wallet = data['wallet'][user]

        if data['checkin'][user] > (Daily_bonus) :
            bot.send_message(
                user_id, "Daily send anda full")
            return

        if (user_id not in bonus.keys()) or (cur_time - bonus[user_id] > 60*60*24):
            if wallet == "none":
                data['checkin'][(user)] += (Daily_bonus)
                bot_name = bot.get_me().username
                bot.send_message(
                    user_id, f"Selamat kamu mendapatkan {Daily_bonus} Daily send, bila kamu sudah set role maka akan mendapastkan 5 daily send")
                bonus[user_id] = cur_time
                json.dump(data, open('users.json', 'w'))
            return

        if (user_id not in bonus.keys()) or (cur_time - bonus[user_id] > 60*60*24):
            data['checkin'][(user)] += (COST)
            bot_name = bot.get_me().username
            bot.send_message(
                    user_id, f"Selamat kamu mendapatkan {COST} Daily send")
            bonus[user_id] = cur_time
            json.dump(data, open('users.json', 'w'))
            return

        else:
            bot.send_message(
                message.chat.id, "❌*Anda hanya bisa mengambil bonus sekali dalam 24 jam !*",parse_mode="markdown")

@bot.message_handler(content_types=['text'], chat_types=["private"])
def send_text(message):
   try:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        lalo = message.text
        ah = tegar(lalo)
        klai = check(user)
        kuku =  saloi(lalo)
        ohm = itil(lalo)
        kon = peler(lalo)
        ih = len(lalo.split(" "))

        data = json.load(open('users.json', 'r'))
        if user not in data['balance']:
            data['balance'][user] = 0
        if user not in data['checkin']:
            data['checkin'][user] = 0
        if user not in data['pict']:
            data['pict'][user] = ""
        json.dump(data, open('users.json', 'w'))

        bal = data['balance'][user]
        kul = data['checkin'][user]
        pulu = data['pict'][user]

        if kuku == True:
            bot.send_message(user_id, "*Anda mengunakan kata terlarang*",
                             parse_mode="Markdown")
            return

        if klai == False:
            bot.send_message(user_id, "*🍔 To Use This Bot You Need To Join This Channel -\n\n➡️ @ONSBASEE\n\n➡️ @menfesonsbase\n\n➡️ @onsbase_grub*",
                             parse_mode="Markdown")
            return

        if ah == False:
            tag = '\n\n'.join(map(str, TAG))
            bot.send_message(user_id, f"gagal mengirim!!\n\nharap gunakan tag dibawah ini : \n\n{tag}",
                             parse_mode="Markdown")
            return

        if ih < 3:
            bot.send_message(user_id, "❌ *Pesan anda gagal terkirim!!! Tidak boleh kurang dari 3 kata!!*", parse_mode="markdown")
            return

        if kul == 0:
            if bal == 0:
                bot.send_message(
                    user_id, f"_❌Daily send anda habis dan Koin anda kurang, setidaknya memiliki {COSTT} {TOKEN} untuk mengirim pesan.\n\nJangan lupa!!! /ambilbonus dan check akun anda /account_", parse_mode="Markdown")
                return

        if kul < 0:
            if bal < 0:
                bot.send_message(
                    user_id, f"_❌Daily send anda habis dan Koin anda kurang, setidaknya memiliki {COSTT} {TOKEN} untuk mengirim pesan.\n\nJangan lupa!!! /ambilbonus_", parse_mode="Markdown")
                return

        if len(pulu) >= 3:
            if ah == True:
                if data['checkin'][user] >= 1:
                    pesan = bot.send_photo(BASE, ""+data['pict'][user]+f"", f"{lalo}")
                    links = LINKKEDDD + "/" + str(pesan.id)
                    linksk = links + "?comment=" + str(pesan.id)
                    bot.send_message(user_id, "✅ BERHASIL DI POSTING!!!\n\nsuport our partner:\n├❥ @AlterFWB2\n⬇️ Check in HERE!! ⬇️", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))

                    data['checkin'][user] -= 1
                    bot_name = bot.get_me().username
                    json.dump(data, open('users.json', 'w'))

                    bot.send_message(PANTAU, ""+data['id'][user]+f"\n\n{lalo}\n\nusename :".format(
                        message.from_user.username))

        if len(pulu) >= 3:
            if ah == True:
                if data['checkin'][user] == 0 and data['balance'][user] > COSTT:
                    pesan = bot.send_photo(BASE, ""+data['pict'][user]+f"", f"{lalo}")
                    links = LINKKEDDD + "/" + str(pesan.id)
                    linksk = links + "?comment=" + str(pesan.id)
                    bot.send_message(user_id, "✅ BERHASIL DI POSTING!!!\n\nsuport our partner:\n├❥ @AlterFWB2\n⬇️ Check in HERE!! ⬇️", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))

                    data['balance'][user] -= (COSTT)
                    bot_name = bot.get_me().username
                    json.dump(data, open('users.json', 'w'))

                    bot.send_message(PANTAU, ""+data['id'][user]+f"\n\n{lalo}\n\nusename :".format(
                        message.from_user.username))

        if len(pulu) == 0:
            if ah == True:
                if data['checkin'][user] >= 1:
                    if ohm == True:
                        pesan = bot.send_photo(BASE, "https://t.me/URLFOTO/11", f"{lalo}")
                        links = LINKKEDDD + "/" + str(pesan.id)
                        linksk = links + "?comment=" + str(pesan.id)
                        bot.send_message(user_id, "✅ BERHASIL DI POSTING!!!\n\nsuport our partner:\n├❥ @AlterFWB2\n⬇️ Check in HERE!! ⬇️", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))

                        data['checkin'][user] -= 1
                        bot_name = bot.get_me().username
                        json.dump(data, open('users.json', 'w'))

                        bot.send_message(PANTAU, ""+data['id'][user]+f"\n\n{lalo}\n\nusename :".format(
                            message.from_user.username))
        if len(pulu) == 0:
            if ah == True:
                if data['checkin'][user] >= 1:
                    if kon == True:
                        pesan = bot.send_photo(BASE, "https://t.me/URLFOTO/12", f"{lalo}")
                        links = LINKKEDDD + "/" + str(pesan.id)
                        linksk = links + "?comment=" + str(pesan.id)
                        bot.send_message(user_id, "✅ BERHASIL DI POSTING!!!\n\nsuport our partner:\n├❥ @AlterFWB2\n⬇️ Check in HERE!! ⬇️", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))

                        data['checkin'][user] -= 1
                        bot_name = bot.get_me().username
                        json.dump(data, open('users.json', 'w'))

                        bot.send_message(PANTAU, ""+data['id'][user]+f"\n\n{lalo}\n\nusename :".format(
                            message.from_user.username))

        if len(pulu) == 0:
            if ah == True:
                if data['checkin'][user] == 0 and data['balance'][user] > COSTT:
                    if ohm == True:
                        pesan = bot.send_photo(BASE, "https://t.me/URLFOTO/11", f"{lalo}")
                        links = LINKKEDDD + "/" + str(pesan.id)
                        linksk = links + "?comment=" + str(pesan.id)
                        bot.send_message(user_id, "✅ BERHASIL DI POSTING!!!\n\nsuport our partner:\n├❥ @AlterFWB2\n⬇️ Check in HERE!! ⬇️", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))

                        data['balance'][user] -= (COSTT)
                        bot_name = bot.get_me().username
                        json.dump(data, open('users.json', 'w'))

                        bot.send_message(PANTAU, ""+data['id'][user]+f"\n\n{lalo}\n\nusename :".format(
                            message.from_user.username))
        if len(pulu) == 0:
            if ah == True:
                if data['checkin'][user] == 0 and data['balance'][user] > COSTT:
                    if kon== True:
                        pesan = bot.send_photo(BASE, "https://t.me/URLFOTO/12", f"{lalo}")
                        links = LINKKEDDD + "/" + str(pesan.id)
                        linksk = links + "?comment=" + str(pesan.id)
                        bot.send_message(user_id, "✅ BERHASIL DI POSTING!!!\n\n⬇️ Check in HERE!! ⬇️", parse_mode="markdown", reply_markup=awikwokbanget(links, linksk))

                        data['balance'][user] -= (COSTT)
                        bot_name = bot.get_me().username
                        json.dump(data, open('users.json', 'w'))

                        bot.send_message(PANTAU, ""+data['id'][user]+f"\n\n{lalo}\n\nusename :".format(
                            message.from_user.username))
        return
   except:
        yamete = ma(row_width=1)
        rawri = bb(text="RULES", url="https://t.me/onsbasee/5366")
        yamete.add(rawri)
        bot.send_message(message.chat.id, "@{} pesan anda gagal terkirim, silahkan coba ulang kembali".format(message.from_user.username), parse_mode="markdown", reply_markup=yamete)
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)

@bot.message_handler(content_types=['photo', "video", "voice"], chat_types=["private"])
def send(message):
    if message:
        user_id = message.chat.id
        user = str(user_id)
        kulon = message.text

        data = json.load(open('users.json', 'r'))
        if data['checkin'][user] >= 1:
            data['checkin'][user] -= 1
            bot_name = bot.get_me().username
            json.dump(data, open('users.json', 'w'))

        if data['checkin'][user] == 0 and data['balance'][user] >=COSTT:
            data['balance'][user] -= (COSTT)
            bot_name = bot.get_me().username
            json.dump(data, open('users.json', 'w'))


        bot.send_message(message.chat.id,"✅ Post!! Check in @ONSBASEE")
        bot.copy_message(BASE,message.chat.id,message.message_id)
        bot.copy_message(PANTAU,message.chat.id,message.message_id, "username : @{}\n\nid : {}".format(
            message.from_user.username, user))
        return

def banned(message):
   try:
    if len(message.text) >= 10:
        banned = message.text
        user_id = message.text
        user = str(user_id)
        data = json.load(open('users.json', 'r'))

        data['balance'][banned] -= (BANNEDD)
        data['checkin'][banned] -= (SANKSI)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(user_id, f"🙅‍♀* Selamat bajingan!\n\nKamu mendapatkan sanksi, koin kamu berkurang - {BANNEDD} {TOKEN} secara automatis*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
    else:
        bot.send_message(
            message.chat.id, "*⚠️ Username ID Not Found!*", parse_mode="Markdown")
   except:
        bot.send_message(message.chat.id, "⚠️ Username ID Not Found!")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def amo_with(message):
   try:
    user_id = message.chat.id
    user = str(user_id)
    data = json.load(open('users.json', 'r'))
    data['DailyQuiz'][user] = message.text
    amo = data['DailyQuiz'][user]

    if user not in data['balance']:
        data['balance'][user] = 0
    json.dump(data, open('users.json', 'w'))

    bal = data['balance'][user]
    msg = message.text
    if msg.isdigit() == False:
        bot.send_message(
            user_id, "_📛 Invaild value. Hanya masukan angka. Coba lagi_", parse_mode="Markdown")

    if int(message.text) < Mini_Withdraw:
        bot.send_message(
            user_id, f"_❌ Minimum transfer {Mini_Withdraw} {TOKEN}_", parse_mode="Markdown")

    if int(message.text) > bal:
        bot.send_message(
            user_id, "_❌ Anda tidak bisa transfer meleibihi koin anda_", parse_mode="Markdown")

    json.dump(data, open('users.json', 'w'))
    bot.send_message(user_id, "_Masukan Id yang dituju_", parse_mode="Markdown")
    bot.register_next_step_handler(message, lero_susu)
    return

   except:
        bot.send_message(message.chat.id, "⚠️ Username ID Not Found!")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def tegar(data):
	for x in data.split(" "):
		yow = x
		for i in TAG:
			yaw = i
			if yaw in yow:
				data = 1
	if data == 1:
		return True
	else:
		return False

def itil(data):
	for x in data.split(" "):
		yow = x
		for i in CEWE:
			yaw = i
			if yaw in yow:
				data = 1
	if data == 1:
		return True
	else:
		return False

def peler(data):
	for x in data.split(" "):
		yow = x
		for i in COWO:
			yaw = i
			if yaw in yow:
				data = 1
	if data == 1:
		return True
	else:
		return False

def saloi(data):
	for x in data.split(" "):
		yow = x
		for i in KATAAAA:
			yaw = i
			if yaw in yow:
				data = 1
	if data == 1:
		return True
	else:
		return False

def lero_susu(message):
   try:
    if len(message.text) >= 8:
        user_id = message.chat.id
        user = str(user_id)
        lero_id = message.text
        suman = str(lero_id)

        data = json.load(open('users.json', 'r'))
        amo = data['DailyQuiz'][user]

        amo = int(amo)
        data['balance'][user] -= int(amo)
        data['balance'][user] -= 100
        bot_name = bot.get_me().username

        data['balance'][suman] += int(amo)
        bot_name = bot.get_me().username

        bot.send_message(user_id, "✅*Selamat!\n\n📉Anda berhasil mengirim {} {} kepada {}*".format(amo, TOKEN, suman), parse_mode="Markdown")

        bot.send_message(lero_id, "✅* Selamat!\n\n💹Anda mendapatkan : {} {} dari {}*".format(amo, TOKEN, message.from_user.first_name), parse_mode="Markdown")

        bot.send_message(PANTAU, "transaksi dari {} ke {} sebanyak {}".format(user_id, lero_id, amo))

        json.dump(data, open('users.json', 'w'))

    else:
        bot.send_message(
            message.chat.id, "*⚠️ Kata-kata terlalu pendek*", parse_mode="Markdown")

   except:
        bot.send_message(message.chat.id, "⚠️ Username ID Not Found!")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return


def lol_address(message):
   try:
    if len(message.text) >= 3:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        data['wallet'][user] = message.text

        data['balance'][user] -= (ROLEL)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(message.chat.id, "*💹Role anda telah diset " +
                         data['wallet'][user]+"*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
    else:
        bot.send_message(
            message.chat.id, "*⚠️Kata-kata terlalu pendek!*", parse_mode="Markdown")
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def suman_pict(message):
   try:
    if len(message.text) >= 3:
        user_id = message.chat.id
        user = str(user_id)
        data = json.load(open('users.json', 'r'))
        data['pict'][user] = message.text

        data['balance'][user] -= (ROLEL)
        bot_name = bot.get_me().username
        json.dump(data, open('users.json', 'w'))

        bot.send_message(message.chat.id, "*💹Role anda telah diset " +
                         data['pict'][user]+"*", parse_mode="Markdown")
        json.dump(data, open('users.json', 'w'))
    else:
        bot.send_message(
            message.chat.id, "*⚠️Kata-kata terlalu pendek!*", parse_mode="Markdown")
   except:
        bot.send_message(message.chat.id, "This command having error pls wait and text /start to restart bot")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: "+message.text)
        return

def awikwokbanget(cek, cekin):
	miaw = ma(row_width=2)
	b1 = bb(text="Cek Postingan", url=cek)
	b2 = bb(text="Cek Komentar", url=cekin)
	miaw.add(b1, b2)
	return miaw

if __name__ == '__main__':
    bot.polling(none_stop=True)
