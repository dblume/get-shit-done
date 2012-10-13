# get-shit-done
get-shit-done is an easy to use command line program that blocks websites known to distract us from our work.

This clone is of an out-of-date version.  You're better off looking at [leftnode's version.](https://github.com/leftnode/get-shit-done)  The only thing that I like about this old version is that it doesn't take any parameters.  Just running the command toggles access to time-wasting sites.

After cloning this repository, put it in your $PATH and ensure it is executable.

Execute it as root because it modifies your hosts file and restarts your network daemon. Every time you run it, it'll toggle between work mode and play mode.

## To toggle between work and play mode, use the same command: 
`sudo get-shit-done`

### $siteList
Add or remove elements of this array for sites to block or unblock.

### ~/.get-shit-done.ini
As an alternative to above, add lines in format
sites[] = www.blah.com
to this file

### $restartNetworkingCommand
Update this variable with the path to your network daemon along with any parameters needed to restart it.

### $hostsFile
Update this variable to point to the location of your hosts file. Make sure it is an absolute path.

Vic Cherubini would really love it if anyone wanted to follow some of my other repositories, including [jolt](https://github.com/leftnode/jolt) or [dbmigrator](https://github.com/leftnode/dbmigrator). I think both are promising projects and I know I could use some help on them.

-David Blume
