'''
IRC bot made for the #studypython channel
Current contributors: 
- fnurk
- fweakout
'''

import socket

network = 'irc.freenode.net'
channel = '#studypython'
nick = 'StudyBot'

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
irc.send("USER %s %s %s :fweakout bot\n" %(nick,nick,nick))
irc.send("NICK %s\n" %nick)

joinChan(channel)

while alive:
    ircmsg = irc.recv(2048)
    ircmsg = ircmsg.strip('\n\r')
    print ircmsg

    if ircmsg.find(":Hello "+nick) != -1:
        irc.send(chanMsg+"Hello!\n")

    if ":!git" in ircmsg:
        irc.send(chanMsg+"https://github.com/fnurk/studypython \n")

    if "!g+" in ircmsg:
        irc.send(chanMsg+"https://plus.google.com/communities/116969234888661099943 \n")

    if ":!curr" in ircmsg:
        irc.send(chanMsg+"https://moot.it/learnpython \n")
    
    if ":!dog" in ircmsg:
        irc.send(chanMsg+"Woof woof woof WOOF! \n")

    if ":!help" in ircmsg:
        irc.send(chanMsg+"My commands are: !git, !g+, !curr, !lib, !dog and !help \n")

    if (":!die "+nick) in ircmsg:
        alive = False

    if ":!wut" in ircmsg:
        irc.send(chanMsg+"tecn1c0 doesn't understand \n")
    if "!lib"in ircmsg:
        irc.send(chanMsg+"http://www.lfd.uci.edu/~gohlke/pythonlibs/ \n")

    if ircmsg.find("PING :") != -1:
        ping()
