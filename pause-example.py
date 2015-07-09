#line 136 of welcomebot.py
dead = false
def on_command(message, client):
    priv_users = shelve.open("privileged_users.txt")
    print "watchCalled"
    print "Message Posted"
    if message.content.startswith("//pause"):
    	dead = true
    	message.message.reply("I'm paused :/")
    if dead === false:
    	if message.content.startswith("//image"):
    		#whatever it does
    	#etc...
    else:
    	if message.content.startswith("//start"):
    	    dead = false
    	    message.message.reply("I'm started! :D")
