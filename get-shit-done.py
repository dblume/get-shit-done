#!/usr/bin/env python

import sys
import getpass
import subprocess
import os

def exit_error(error):
    print >> sys.stderr, error
    exit(1)

iniFile = os.path.expanduser(os.path.join("~", ".get-shit-done.ini"))

restartNetworkingCommand = ["/etc/init.d/networking", "restart"]
restartMacNetworkingCommand = ['ifconfig en0 down; ifconfig en0 up;']

# Windows users may have to set up an exception for write access
# to the hosts file in Windows Security Essentials.
hostsFile = '/etc/hosts'

startToken = '## start-gsd'
endToken = '## end-gsd'
siteList = ['reddit.com', 'forums.somethingawful.com',
            'somethingawful.com', 'digg.com', 'break.com',
            'news.ycombinator.com', 'infoq.com',
            'bebo.com', 'twitter.com', 'facebook.com',
            'blip.com', 'youtube.com', 'vimeo.com',
            'flickr.com', 'friendster.com', 'hi5.com',
            'linkedin.com', 'livejournal.com',
            'yourusername.livejournal.com', # TODO use your username
            'meetup.com', 'myspace.com', 'plurk.com',
            'stickam.com', 'stumbleupon.com', 'yelp.com',
            'slashdot.com', 'lifehacker.com',
            'plus.google.com', 'gizmodo.com',
            'thedailywtf.com', 'samachar.com', 
            'hindu.com', 'lifehack.org', 'slickdeals.net',
            'woot.com']

def loadIniFile():
    global siteList
    if os.path.exists(iniFile):
        with open(iniFile) as iniF:
            for line in iniF:
                key, value = map(str.strip, line.split("=", 1))
                if key == "sites":
                    siteList = [value]
                elif key == "sites[]":
                    siteList.append(value)

def rehash():
    if sys.platform == 'cygwin':
        return
    if sys.platform == 'darwin':
        subprocess.check_call(restartMacNetworkingCommand)
    else:
        subprocess.check_call(restartNetworkingCommand)

def work():
    with open(hostsFile, 'a') as hFile:
        print >> hFile, startToken
        for site in siteList:
            print >> hFile, "127.0.0.1\t" + site
            if site.count('.') == 1:
                print >> hFile, "127.0.0.1\twww." + site
        print >> hFile, endToken
    rehash()

def play(startIndex, endIndex, lines):
    with open(hostsFile, "w") as hFile:
        hFile.writelines(lines[0:startIndex])
        hFile.writelines(lines[endIndex+1:])
    rehash()

if __name__ == "__main__":
    if sys.platform != 'cygwin' and getpass.getuser() != 'root':
        exit_error('Please run script as root.')

    loadIniFile()

    # Determine if our siteList is already present.
    startIndex = -1
    endIndex = -1
    with open(hostsFile, "r") as hFile:
        lines = hFile.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if line == startToken:
                startIndex = i
            elif line == endToken:
                endIndex = i

    if startIndex > -1 and endIndex > -1:
        play(startIndex, endIndex, lines)
        print "Play mode activated."
    else:
        work()
        print "Get back to work."
