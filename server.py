import Pyro4

CLIENT_DB = {
	# username : password
	"client1" : "000",
	"client2" : "000"
}



class ChatService(object):
	def __init__(self):
		self.nicks = []
		self.groups = {}

	def login(self, username, password, CC_obj):
		global CLIENT_DB
		if username in CLIENT_DB and password == CLIENT_DB[username]:
			print "Client login!"

		else:
			raise ValueError(" * Error: Wrong username or password.")
			

	def logout(self):
		pass

	def register(self, username, password):
		global CLIENT_DB
		if username not in CLIENT_DB:
			CLIENT_DB.update(map(username, password))
			print "Client register!"
		else: 
			raise ValueError(" * Error: User already exists.")

	def join_group(self, group, nick, CC_obj):
		if not group or not nick:
			raise ValueError(" * Error: Invalid group or nick.")
		if nick in self.nicks:
			raise ValueError(" * Error: Nick is already used.")
		if group not in self.groups:
			print "Client created new a group."
			self.groups[group] = []

		self.groups[group].append((nick, CC_obj))
		self.nicks.append(nick)
		print "%s joined group %s" % (nick, group)

	def list_nicks(self):
		return self.nicks
			

	def list_groups(self):
		return self.groups.keys()

	def make_group(self, members):

		pass

		

	#@Pyro4.oneway
	def chat(self, group, nick, text):
		for (n, c) in self.groups[group][:]:
			if n != nick:
				c.show_message(" [%s]: " % nick + text)


if __name__ == '__main__':
	
	with Pyro4.core.Daemon() as daemon:
		with Pyro4.naming.locateNS() as ns:
			CS_obj = ChatService()
			uri = daemon.register(CS_obj)
			ns.register("Chat.Service", uri)
		print "Server ready."
		daemon.requestLoop()
