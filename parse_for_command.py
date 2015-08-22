from Bot import Bot
import shelve

def parse_for_command(message):
    priv_users = shelve.open('priveleged_users.txt')
    possible_command = message.split()[0]
    if message in Bot.commands['all_commands']:
        return Bot.commands['all_commands'][possible_command](message)
    elif message in Bot.commands['priv_commands']:
         if (message.user.id == 121401 and host_id == 'stackexchange.com') or (message.user.id == 284141 and host_id == 'meta.stackexchange.com') or (message.user.id == 4087357 and host_id == 'stackoverflow.com') or (str(message.user.id) in priv_users[host_id + room_id]):
             return Bot.commands['priv_commands'][possible_command](message)
         else:
             return Bot.deny_command_message
         
