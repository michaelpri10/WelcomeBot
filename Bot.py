import os
from Commmands.image_search import image_search
from Commands.other_commands import choose, bot_info, is_alive, source_code, help_menu
from Commands.google_search import google_search
from Commands.weather_search import weather_search
from Commands.youtube_search import youtube_search

class Bot:
    paused = False
    welcome_message = None
    host_id = None
    room_id = None
    room = None
    me = None
    deny_command_message = ["You are not authorized to do that!", "message"]
    commands = {
               all_commands:
                   { 
                   '//image': image_search,
                   '//youtube': youtube_search,
                   '//choose': choose,
                   '//search': google_search,
                   '//weather': weather_search,
                   '//info': bot_info,
                   '//alive': is_alive, 
                   '//source': source_code, 
                   '//help': help_menu
                   }
               priv_commands:
                   {
                   '//pull': pull,
                   '//reset': reset,
                   '//die': die,
                   '//editmsg': edit_message,
                   '//priv': give_priv,
                   '//pause': pause_bot,
                   '//resume': resume_bot,
                   '//testenter': "@SkynetTestUser {}".format(BotProperties.welcome_message)
                   }
               }

