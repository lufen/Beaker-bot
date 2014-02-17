Beaker-bot
==========

Skype Python bot

Currently only has But-to-cloud functionality and repsonds to "@nsfw" with a random nsfw subreddit

========
Plugins:

The new plugin system allows easy creation of plugins for beaker bot. A plugins has to manage it's own state and handling of user input.
To create a plugin, create a new module in the plugins folder which contains a class that inherits the "plugin" class from the baseclass module.
The newly created class must implement the "message received" function. This is where the received message is processed. The function receives the chat
object that is was received from and teh message. Plase see the Skype4py documentation for more information http://skype4py.sourceforge.net/doc/html/frames.html


