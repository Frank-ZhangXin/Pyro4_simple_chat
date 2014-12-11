# Pyro4 Simple Chat System
----

## About this project:
* This program is a simple chat system based Python 2.7.x also with using Pyro4 RPC object.
* About : [Pyro4](https://pythonhosted.org/Pyro4/)
* Also thanks to my professor [Dakai Zhu](http://www.cs.utsa.edu/~dzhu/) and co-author Che-wei Chen. 
----
## Instructions:
1. Start the name server first. Single prompt window type: *'pyro4-ns'*.
2. Run the chat server in another prompt window with command: *'python server.py'*.
3. Begin the chat client. Open a new prompt window and type: *'python client.py'*.
----
## Chat system commands:
1. *#help*:     list all the commands and explaination.
2. *#user*:     *'#user user_nick'* check the user's group with that nick
3. *#group*:    Format *'#group group_name'*, check the group's members
4. *#list group*:   show all the groups alive currently.
5. *#list nicks*:   show all the users alive currently.
6. *#join group*:   Format *'#join group group_name'*, join in the *'group_name'* group, if it doesn't exist, then automatically create it as new one.
7. *#quit group*:   quit the group you in
8. *#dialogue*:     Format *'dialogue user_nick message'*, speak to someone individually whose name is user_name, and content is message.
9. Anyone in the group can simply send message to every member of it. New member coming will notice other ones in the group. Quit group, vice versa.
10. **Offline message** feature added. If you dialogue with some one not login, these messages will be kept till he/she next time login, and show up in the beginning.
