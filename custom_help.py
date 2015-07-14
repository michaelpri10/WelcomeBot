 # line 226 in welcomebot.py
 elif message.content.startswith("//help"):
        print "Is help request"
        if (message.user.id == 121401 and host_id == 'stackexchange.com') or (message.user.id == 284141 and host_id == 'meta.stackexchange.com') or (message.user.id == 4087357 and host_id == 'stackoverflow.com') or (str(message.user.id) in priv_users[host_id + room_id]):
                message.message.reply("""My Commands
                                     - //image (image search term)
                                     - //choose (choice) or (choice) [or choice...]
                                     - //weather (city)[, country/state]
                                     - //youtube (youtube search term)
                                     - //source
                                     - //pull *
                                     - //pause *
                                     - //start *
                                     - //die *
                                     * = Only Privileged Users
                                  """)
        else:
                message.message.reply("""My Commands
                             - //image (image search term)
                             - //choose (choice) or (choice) [or choice...]
                             - //weather (city)[, country/state]
                             - //youtube (youtube search term)
                             - //source
                          """)
