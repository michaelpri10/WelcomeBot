dead = false
def on_command(message, client):
    priv_users = shelve.open("privileged_users.txt")
    print "watchCalled"
    print "Message Posted"
    if message.content.startswith("//pause"):
    	dead = true
    if dead === false:
    	if message.content.startswith("//image"):
    		...
    	...
    else:
    	if message.content.startswith("//start"):
    		dead = false
