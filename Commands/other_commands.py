from Bot import Bot

def choose(message):
    if len(message.split()) == 1:
        return ["No choices given", "message"]
    else:
        if " or " in message:
            choices = message[8:].split(" or ")
            return ["I choose {}".format(random.choice(choices)), "message"]
        else:
            return ["I'm not sure what your options are", "message"]

def bot_info(message):
    return ["Host ID: {0}\nRoom ID: {1}\nWelcome Message:\n{2}".format(Bot.host_id, Bot.room_id, Bot.welcome_message), "message"]

def is_alive(message):
    return ["I'm alive :) (running on commit: ({})".format(os.popen('git log --pretty=format:"%h" -n 1').read()), "message"] 

def source_code(message):
    return ["My source code can be found on [GitHub](https://github.com/michaelpri10/WelcomeBot)", "message"] 

def help_menu(message):
    return ["""My Commands
               - //image (search term)
               - //choose (choice) or (choice) [or choice...]
               - //weather (city)[, country/state]
               - //youtube (search term)
               - //source
               - //info
               - //search (search term)
            """, "message"]
