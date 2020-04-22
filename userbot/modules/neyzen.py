# Copyright (C) 2020 TeamDerUntergang
#
# Licensed under the TeamDerUntergang Public License;
# you may not use this file except in compliance with the License.
""" Neyzem module for having some fun with people. """
""" Powered by EmreCan """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time

from collections import deque

import requests

from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
NEYZEN_STRINGS = [
    "yürü bre ehli deve endamını göreyim",
    "sensiz geçen gecelerin ecdadını sikeyim.",
    "mecnun gibi top muyum bir am için öleyim?.",
    "leyla'yı da sikeyim mecnun'u da sikeyim..",
    "bana yar olmayan karının izzetini itibarini sikeyim....",
    "yansın karıların alayı, su veren itfaiyenin hortumunu sikeyim.",
    "düşmüşüz bir orospunun belasına",
    "koymadık diye taaa amının ortasına",
    "kader böyle yazmış hatırasına...",
    "ben böyle hatıranın hikayesini sikeyim!",
    "kerem dağları deler bir amcık uğruna, aslı gitsin de ona buna vurdura....",
    "bir karı için değer mi hiç bütün bunlara, her taraf amcık dolu mala iyi vurana.",
    "fuzuli am peşine düştün gurbete, am serindir am derindir şifa verir millete,",
    "ye kebabı iç şarabı vur karpuz göte, bu gidişle yarrağımı gidersin cennete.
",
]


@register(outgoing=True, pattern="^.neyzen$")
async def neyzen(e):
    """ Neyzen is dictionary """
    await e.edit(choice(NEYZEN_STRINGS))
    
    
CMD_HELP.update({
    "neyzen":
    ".neyzen or reply to someones text with .neyzen\
    \nUsage: neyzen quotes."
})
