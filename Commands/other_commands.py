def choose(message):
    if len(message.split()) == 1:
        return ["No choices given", "message"]
    else:
        if " or " in message:
            choices = message[8:].split(" or ")
            return ["I choose {}".format(random.choice(choices)), "message"]
        else:
            return ["I'm not sure what your options are", "message"]
