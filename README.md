#WelcomeBot

A Stack Exchange chatbot written in Python that uses [ChatExchange](https://github.com/Manishearth/ChatExchange). Many parts of this were modeled after [SmokeDetector](https://github.com/Charcoal-SE/SmokeDetector), another Stack Exchange chatbot. 

---

##Features

- Welcomes new users entering chatrooms on [chat.stackexchange](http://chat.stackexchange.com), [chat.meta.stackexchange](http://chat.meta.stackexchange.com), and [chat.stackoverflow](http://chat.stackoverflow.com)
- Many different chatroom commands:
 - `//image (image search term)` - searches for and posts images of or relating to the image search term
 - `//choose (choice) or (choice) [or choice...]` - makes decisions for you so you don't have to. Can accept more than two choices as long as they are separated by `' or '`
 - `//weather (city)[, country/state]` - gets the weather for whatever location you would like
 - `//youtube (youtube search term)` - search [Youtube](https://www.youtube.com/) for and returns a video of or relating to your search term

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
