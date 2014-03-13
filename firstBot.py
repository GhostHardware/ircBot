'''
fork of fweakout's bot
keepin' it real, yo
'''

import socket
from bot_config import *

chanMsg = "PRIVMSG %s :" %channel

alive = True

def ping():
    irc.send("PONG :Pong\n")

def joinChan(chan):
    irc.send("JOIN %s\n" %chan)

def sendMsg(msg):
    irc.send("PRIVMSG %s :%s\n" %channel,msg)

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network,6667))
irc.send("USER %s %s %s :salty bot\n" %(nick,nick,nick))
irc.send("NICK %s\n" %nick)

joinChan(channel)

banana_count = 0

while alive:
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    print ircmsg

    if ircmsg.find(":Hello "+nick) != -1:
        irc.send(chanMsg+"Hello!\n")

    if ":!banan" in ircmsg:
        if (banana_count == 3):
            banana_count = 0
            irc.send(chanMsg+"Banana phone! https://www.youtube.com/watch?v=OpjGxq5uE3A \n")
        else:
            banana_count += 1
            irc.send(chanMsg+"ring ring ring ring ring ring ring \n")
    
    if ":!dog" in ircmsg:
        irc.send(chanMsg+"Woof woof woof WOOF! \n")

    if ":!help" in ircmsg:
        irc.send(chanMsg+"My commands are: !banan \n")

    if (":!die "+nick) in ircmsg:
        alive = False

    if ircmsg.find("PING :") != -1:
        ping()
