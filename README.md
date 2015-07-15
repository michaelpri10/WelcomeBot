#WelcomeBot

A Stack Exchange chatbot written in Python that uses [ChatExchange](https://github.com/Manishearth/ChatExchange). Many parts of this were modeled after [SmokeDetector](https://github.com/Charcoal-SE/SmokeDetector), another Stack Exchange chatbot.

---

##Features

- Welcomes new users entering chatrooms on [chat.stackexchange](http://chat.stackexchange.com), [chat.meta.stackexchange](http://chat.meta.stackexchange.com), and [chat.stackoverflow](http://chat.stackoverflow.com) with a custom welcome command made by you
- Many different chatroom commands:
 - `//image (image search term)` - searches for and posts images of or relating to the image search term
 - `//choose (choice) or (choice) [or choice...]` - makes decisions for you so you don't have to. Can accept more than two choices as long as they are separated by `' or '`
 - `//weather (city)[, country/state]` - gets the weather for whatever location you would like
 - `//youtube (youtube search term)` - search [Youtube](https://www.youtube.com/) for and returns a video of or relating to your search term
 - `//source` - gives you a link to WelcomeBot's source code on Github
 - `//info` - tells you the host site, room id, and welcome message
 - `//help` - tells you all of the commands listed above in case you forget
- Commands for privileged users:
 - `//die` - kills the bot if it is acting up
 - `//reset` - resets the bot just in case
 - `//pull` - updates the bot with the latest commit on Github
 - `//pause` - pauses the bot temporarily
 - `//start` - resumes the bot when it is paused
 - `//editmsg [new welcome message]` - edit the welcome message
 - `//priv [user id]` - gives a user the ability to use this command and the six commands listed above

---

To setup run:

    git clone https://github.com/michaelpri10/WelcomeBot.git
    cd WelcomeBot
    git submodule init
    git subodule update
    sudo pip install beautifulsoup4
    sudo pip install requests --upgrade
    sudo pip install websocket-client --upgrade

Or you can just run the `setup.sh` file.

---

To run WelcomeBot, run `nocrash.sh` and log in with your Stack Exchange OpenID credentials.

---

##Why use WelcomeBot?

- Make new users feel welcome in your chatroom
- Have fun in your chatroom

---

##Source Code

- WelcomeBot is an open source project and all of its code is available on [Github.](https://github.com/michaelpri10/WelcomeBot)
- WelcomeBot is constantly being updated; luckily the `//pull` commands makes it easy to keep up
- If you want to see WelcomeBot in action check out the [Teenage Programmers Chatroom](http://chat.stackoverflow.com/rooms/22091/teenage-programmers-chatroom), the current home for WelcomeBot
- WelcomeBot was created by michaelpri ([Github](https://github.com/michaelpri10), [Stack Exhange](http://stackexchange.com/users/4642421/michaelpri)), ProgramFOX ([Github](https://github.com/programfox), [Stack Exchange](http://stackexchange.com/users/3094403/programfox)), and Jacob Gray ([Github](https://github.com/Jacob-Gray), [Stack Exchange](http://stackexchange.com/users/3984803/jacob-gray))
