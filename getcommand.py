#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import api
from lxml import etree
from api import Data
from subprocess import call
import time
import subprocess
import urllib2
import wikipedia
from random import randint
import getpass
import os
import ConfigParser

def command(speech_object):
	previous_command = ""
	while(True):
		
		line = speech_object.readline()
		if(line.startswith("sentence1: ")):
			com = line[15:-6]
			#if (previous_command == com):
			#	continue
			print com

                	Config = ConfigParser.ConfigParser()
                	Config.read("config.ini")
                	user_prefix = Config.get("BasicUserData","Prefix")

			if (com == "DRAGON FIRE"):
				tts_kill()
				userin = Data([" "]," ")
				words_dragonfire = {
					0 : "Yes, " + user_prefix + ".",
					1 : "Yes. I'm waiting.",
					2 : "What is your orders?"
				}
				userin.say(words_dragonfire[randint(0,2)])
			elif (com == "ENOUGH" or com == "OKAY"):
				tts_kill()
			elif (com == "WHO AM I" or com == "WHAT IS MY NAME"):
                                tts_kill()
				user_full_name = os.popen("getent passwd $LOGNAME | cut -d: -f5 | cut -d, -f1").read()
				user_full_name = user_full_name[:-1]
                                userin = Data(["echo"], user_full_name)
                                userin.say("Your name is " + user_full_name + "," + user_prefix + ".")
				userin.interact(0)
                                previous_command = com
			elif (com == "I'M A WOMAN" or com == "I'M A GIRL" or com == "I'M A LADY"):
				tts_kill()
				cfgfile = open("config.ini",'w')
				Config.set("BasicUserData","Prefix","My Lady")
				Config.write(cfgfile)
				cfgfile.close()
				userin = Data([" "]," ")
				userin.say("Pardon, My Lady.")
                        elif (com == "I'M A MAN" or com == "I'M A BOY"):
                                tts_kill()
                                cfgfile = open("config.ini",'w')
                                Config.set("BasicUserData","Prefix","Sir")
                                Config.write(cfgfile)
                                cfgfile.close()
                                userin = Data([" "]," ")
                                userin.say("Pardon, Sir.")
			elif (com == "WHAT IS YOUR NAME"):
				tts_kill()
				userin = Data([" "]," ")
				userin.say("My name is Dragon Fire.")
				previous_command = com
			elif (com == "WHAT IS YOUR GENDER"):
				tts_kill()
                                userin = Data([" "]," ")
                                userin.say("I have a female voice but I don't have a gender identity. I'm a computer program, " + user_prefix + ".")
                                previous_command = com
        		elif (com == "OPEN FILE MANAGER"):
				tts_kill()
				userin = Data(["pantheon-files"],"File Manager")
				userin.say("File Manager")
				userin.interact(0)
				previous_command = com
			elif (com == "OPEN WEB BROWSER"):
				tts_kill()
				userin = Data(["sensible-browser"],"Web Browser")
				userin.say("Web Browser")
				userin.interact(0)
				previous_command = com
			elif (com == "SHUT DOWN THE COMPUTER"):
				tts_kill()
                                userin = Data(["sudo","poweroff"],"Shutting down")
                                userin.say("Shutting down")
				userin.interact(3)
                                previous_command = com
			elif (com.startswith("WIKI PEDIA SEARCH FOR")):
				tts_kill()
				userin = Data(["sensible-browser","http://en.wikipedia.org/wiki/"+com[22:].lower()],com[22:])
				userin.interact(0)
				try:
					wikipage = wikipedia.page(com[22:].lower())
					wikicontent = "".join([i if ord(i) < 128 else ' ' for i in wikipage.content])
					userin.say(wikicontent)
            				previous_command = com
				except:
					pass
			else:
				tts_kill()
                                userin = Data(["echo"],com + " ?")
                                userin.say("Unrecognized command.")
                                userin.interact(0)
                                previous_command = com

def tts_kill():
	call(["pkill", "audsp"])
	call(["pkill", "aplay"])

if __name__ == '__main__':
	try:
		command(sys.stdin)
	except KeyboardInterrupt:
		sys.exit(1)
