# (C) 2021 VeezMusic-Project

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π­ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music on groups through the new Telegram's voice chats!**

π‘ **Find out all the Bot's commands and how they work by clicking on the Β» π Commands button!**

β **To know how to use this bot, please click on the Β» β Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Add me to your Group β",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("β Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("π Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("π Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "π₯ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "π£ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "πDeveloper", url="https://t.me/charmyanime"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Hello !**

Β» **press the button below to read the explanation and see the list of available commands !**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("π Advanced Cmd", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("π Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("π Sudo Cmd", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("π Owner Cmd", callback_data="cbowner")],
                [InlineKeyboardButton("π Go Back", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the basic commands**

π§ [ VOICE CHAT PLAY CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the admin commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the owner commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **HOW TO USE THIS BOT:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the voice chat first before start to play music.**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("π Command List", callback_data="cbhelp")],
                [InlineKeyboardButton("π Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**π‘ here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("βΈ pause", callback_data="cbpause"),
                    InlineKeyboardButton("βΆοΈ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("β© skip", callback_data="cbskip"),
                    InlineKeyboardButton("βΉ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("β anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("π Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π **this is the feature information:**
        
**π‘ Feature:** delete every commands sent by users to avoid spam in groups !

β usage:**

 1οΈβ£ to turn on feature:
     Β» type `/delcmd on`
    
 2οΈβ£ to turn off feature:
     Β» type `/delcmd off`
      
β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

Β» **press the button below to read the explanation and see the list of available commands !**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π Basic Cmd", callback_data="cblocal"),
                    InlineKeyboardButton("π Advanced Cmd", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("π Admin Cmd", callback_data="cblamp"),
                    InlineKeyboardButton("π Sudo Cmd", callback_data="cblab"),
                ],
                [InlineKeyboardButton("π Owner Cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("π Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **HOW TO USE THIS BOT:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the voice chat first before start to play music.**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the basic commands**

π§ [ VOICE CHAT PLAY CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the admin commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π? **here is the owner commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Command Syntax", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("π Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "π **couldn't find song you requested**\n\nΒ» **please provide the correct song name or include the artist's name as well**"
    
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command Syntax** to play music on **Voice Chat:**

β’ `/play (query)` - for playing music via youtube
β’ `/ytp (query)` - for playing music directly via youtube

β‘ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cmdhome")]]
        ),
    )
