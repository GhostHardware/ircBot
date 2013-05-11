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

chan_msg = "PRIVMSG %s :" %channel

alive = True

def ping(): 
    irc.send("PONG :Pong\n")

def join_chan(chan):
    irc.send("JOIN %s\n" %chan)

def send_msg(msg):
    irc.send("PRIVMSG %s :%s\n" %channel,msg)

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network,6667))
irc.send("USER %s %s %s :fweakout bot\n" %(nick,nick,nick))
irc.send("NICK %s\n" %nick)

join_chan(channel)

while alive:
    irc_msg = irc.recv(2048)
    irc_msg = irc_msg.strip('\n\r')
    print irc_msg

    if irc_msg.find(":Hello "+nick) != -1:
        irc.send(chan_msg+"Hello!\n")

    if ":!git" in irc_msg:
        irc.send(chan_msg+"https://github.com/fnurk/studypython \n")

    if "!g+" in irc_msg:
        irc.send(chan_msg+"https://plus.google.com/communities/116969234888661099943 \n")

    if ":!curr" in irc_msg:
        irc.send(chan_msg+"https://moot.it/learnpython \n")
    
    if ":!dog" in irc_msg:
        irc.send(chan_msg+"Woof woof woof WOOF! \n")

    if ":!help" in irc_msg:
        irc.send(chan_msg+"My commands are: !git, !g+, !curr, !lib, !dog and !help \n")

    if (":!die "+nick) in irc_msg:
        alive = False

    if ":!wut" in irc_msg:
        irc.send(chan_msg+"tecn1c0 doesn't understand \n")
    if "!lib"in irc_msg:
        irc.send(chan_msg+"http://www.lfd.uci.edu/~gohlke/pythonlibs/ \n")

    if irc_msg.find("PING :") != -1:
        ping()
