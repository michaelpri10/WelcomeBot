#!/usr/bin/env python

from excepthook import uncaught_exception, install_thread_excepthook
import sys
sys.excepthook = uncaught_exception
install_thread_excepthook()

import getpass
import logging
import logging.handlers
import os
import time
import requests
from threading import Thread

import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events
import ChatExchange.chatexchange.browser
import who_to_welcome
import image_search
import weather_search
import random

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    # Run `. setp.sh` to set the below testing environment variables

    global host_id
    def welcome_bot_host_options():
        print "Welcome Bot Host Site Options (select 1, 2, or 3)"
        print "  1. chat.stackexchange.com"
        print "  2. chat.meta.stackexchange.com"
        print "  3. chat.stackoverflow.com"
        print "What will be your Welcome Bot's host site?"
    if 'HostSite' in os.environ:
        host_id_choice = os.environ['HostSite']
        if host_id_choice == '1':
            print "You have chosen chat.stackexchange.com as your Welcome Bot's host site."
            host_id = 'stackexchange.com'
        elif host_id_choice == '2':
            print "You have chosen meta.chat.stackexchange.com as your Welcome Bot's host site."
            host_id = 'meta.stackexchange.com'
        elif host_id_choice == '3':
            print "You have chosen chat.stackoverflow.com as your Welcome Bot's host site."
            host_id = 'stackoverflow.com'
    else:
        welcome_bot_host_options()
        host_id_choice = raw_input()
        while host_id_choice not in ['1','2','3']:
            print "Invalid Choice"
            welcome_bot_host_options()
            host_id_choice = raw_input()
        if host_id_choice == '1':
            print "You have chosen chat.stackexchange.com as your Welcome Bot's host site."
            host_id = 'stackexchange.com'
        elif host_id_choice == '2':
            print "You have chosen meta.chat.stackexchange.com as your Welcome Bot's host site."
            host_id = 'meta.stackexchange.com'
        elif host_id_choice == '3':
            print "You have chosen chat.stackoverflow.com as your Welcome Bot's host site."
            host_id = 'stackoverflow.com'

    global room_id
    if 'RoomID' in os.environ:
        room_id = os.environ['RoomID']
    else:
        print "What is the room's ID?"
        room_id_choice = raw_input()
        while not room_id_choice.isdigit():
            print "Invalid Input, must be a number"
            room_id_choice = raw_input()
        room_id = room_id_choice  # Charcoal Chatbot Sandbox

    global welcome_message
    if 'WelcomeMessage' in os.environ:
        welcome_message = os.environ['WelcomeMessage']
    else:
        print "What would you like the welcome message to be?"
        welcome_message = raw_input()

    if 'ChatExchangeU' in os.environ:
        email = os.environ['ChatExchangeU']
    else:
        email = raw_input("Email: ")
    if 'ChatExchangeP' in os.environ:
        password = os.environ['ChatExchangeP']
    else:
        password = getpass.getpass("Password: ")

    client = ChatExchange.chatexchange.client.Client(host_id)
    client.login(email, password)

    global bot
    bot = client.get_me()

    global room
    room = client.get_room(room_id)
    room.join()
    room.watch(on_event)

    print "(You are now in room #%s on %s.)" % (room_id, host_id)
    if "first_start" in sys.argv:
        room.send_message("I'm alive :)")

    while True:
        message = raw_input("<< ")
        if message == "die":
            room.send_message("I'm dead :(")
            time.sleep(0.4)
            break
        else:
            pass

    os._exit(6)


def on_event(event, client):
    if isinstance(event, ChatExchange.chatexchange.events.UserEntered):
        on_enter(event)
    elif isinstance(event, ChatExchange.chatexchange.events.MessagePosted):
        on_command(event, client)


def on_enter(event):
    if event.user.id == bot.id or event.user.reputation < 20:
        pass
    else:
        if who_to_welcome.check_user(event.user.id, room_id, 'enter'):
            room.send_message("@" + event.user.name.replace(" ", "")+" "+ welcome_message)


def on_command(message, client):
    print "watchCalled"
    print "Message Posted"
    if message.content.startswith("//image"):
        print "Is image request"
        if len(message.content.split()) == 1:
            room.send_message("No search term given")
            pass
        else:
            def perform_search():
                search_term = "-".join(message.content.split()[1:])
                image = image_search.search_image(search_term)
                print image
                if image is False:
                    print "No Image"
                    room.send_message("@"+message.user.name.replace(" ", "") + " No image was found for " + search_term)
                else:
                    print message.content
                    print search_term
                    room.send_message(image)
            t = Thread(target=perform_search)
            t.start()
    elif message.content.startswith("//die"):
        if (message.user.id == 121401 and host_id == 'stackexchange.com') or (message.user.id == 284141 and host_id == 'meta.stackexchange.com') or (message.user.id in [4087357, 3285730, 2619912] and host_id == 'stackoverflow.com'):
            room.send_message("I'm dead :(")
            time.sleep(0.4)
            os._exit(6)
        else:
            room.send_message("@" + message.user.name.replace(" ", "") + " You are not authorized kill me!!! Muahaha!!!! Please ping `@michaelpri` if I am acting up")
    elif message.content.startswith("//reset"):
        if (message.user.id == 121401 and host_id == 'stackexchange.com') or (message.user.id == 284141 and host_id == 'meta.stackexchange.com') or (message.user.id in [4087357, 3285730, 2619912] and host_id == 'stackoverflow.com'):
            room.send_message("Resetting...")
            time.sleep(0.4)
            os._exit(5)
        else:
            room.send_message("@" + message.user.name.replace(" ", "") + " You are not authorized reset me. Please ping `@michaelpri` if I am acting need resetting")
    elif message.content.startswith("//pull"):
        if (message.user.id == 121401 and host_id == 'stackexchange.com') or (message.user.id == 284141 and host_id == 'meta.stackexchange.com') or (message.user.id in [4087357, 3285730, 2619912] and host_id == 'stackoverflow.com'):
            r = requests.get('https://api.github.com/repos/michaelpri10/WelcomeBot/git/refs/heads/master')
            latest_sha = r.json()["object"]["sha"]
            r = requests.get('https://api.github.com/repos/michaelpri10/WelcomeBot/commits/' + latest_sha + '/statuses')
            states = []
            for status in r.json():
                state = status["state"]
                states.append(state)
            if "success" in states:
                os._exit(3)
            elif "error" in states or "failure" in states:
                room.send_message("@" + message.user.name.replace(" ", "") + " Failed :( Please check your commit.")
            elif "pending" in states or not states:
                room.send_message("@" + message.user.name.replace(" ", "") + " Still pending. Try again in a little")


    elif message.content.startswith("//choose"):
        print "Is choose request"
        if len(message.content.split()) == 1:
            room.send_message("No choices given")
            pass
        else:
            if " or " in message.content:
                choices = message.content[8:].split(" or ")
                room.send_message("@" + message.user.name.replace(" ", "") + " I choose "+random.choice(choices))
            else:
                room.send_message("@"+message.user.name.replace(" ","")+" I'm not sure what your options are")
    elif message.content.startswith("//help"):
        print "Is help request"
        room.send_message("""My Commands
                             //image (image search term) - searches for and posts images of or relating to the image search term
                             //choose (choice) or (choice) [or choice...] - makes decisions for you so you don't have to. Can accept more than two choices as long as they are separated by ' or '
                             //weather (city)[, country/state] - gets the weather for whatever location you would like
                          """)
    elif (message.content.startswith("//weather")):
        print "Is weather request"
        if len(message.content.split()) == 1:
            room.send_message("City and country/state not given")
            pass
        else:
            city_and_country = [i.replace(" ", "%20") for i in message.content[10:].split(",")]
            city = city_and_country[0]
            if len(city_and_country) == 2:
                country_state = city_and_country[1]
                print city, country_state
                try:
                    room.send_message(weather_search.weather_search(city, country_state))
                except:
                    room.send_message("Couldn't find weather info for "+ city + ", " + country_state)
            elif len(city_and_country) == 1:
                try:
                    room.send_message(weather_search.weather_search(city, ""))
                except:
                    room.send_message("Couldn't find weather info for " + city)


def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger.setLevel(logging.DEBUG)

    # In addition to the basic stderr logging configured globally
    # above, we'll use a log file for chatexchange.client.
    wrapper_logger = logging.getLogger('ChatExchange.chatexchange.client')
    wrapper_handler = logging.handlers.TimedRotatingFileHandler(
        filename='client.log',
        when='midnight', delay=True, utc=True, backupCount=7,
    )
    wrapper_handler.setFormatter(logging.Formatter(
        "%(asctime)s: %(levelname)s: %(threadName)s: %(message)s"
    ))
    wrapper_logger.addHandler(wrapper_handler)

if __name__ == '__main__':
    main()
