from baseclass import Plugin
import atexit
import json
import os

class ToDo(Plugin):
    def __init__(self, skype):
        super(ToDo, self).__init__(skype)
        self.command = "todo"
        self.todoList = []
        if "todo" not in os.listdir():
            os.mkdir("todo")
        self.loadList()

    def message_received(self, args, status, msg):
        if not args:
            msg.Chat.SendMessage(str(self.todoList))
        if args[0] == "add":
            self.todoList.append(" ".join(args[1:]))
            msg.Chat.SendMessage('"{}" added'.format(" ".join(self.todoList)))
        elif args[0] == "remove":
            try:
                del self.todoList[args[1]]
            except:
                pass


    def loadList(self):
        with open("/todo/todo.json") as fp:
            self.todoList = json.load(fp)

    @atexit.register
    def dumpList(self):
        with open("todo.json", "w") as fp:
            fp.write(json.dumps(self.todoList))