import Pyro4
from Pyro4 import threadutil

class ChatClient(object):
	def __init__(self):
		self.ChatService = Pyro4.core.Proxy("PYRONAME:Chat.Service")
		self.abort = 0
		self.USERNAME = None
		self.PASSWORD = None
		

	@Pyro4.oneway
	def show_message(self, text):
		print text

	def start(self):
		print " * System: Hi, welcom!\nAre you new user? (Yes / No): "
		choice = raw_input()
		if choice == "yes":
			print " * System: Welcome, new user! Please register before chat!"
			self.USERNAME = raw_input(" * User name: ")
			self.PASSWORD = raw_input(" * Password: ")

			self.ChatService.register(self.USERNAME, self.PASSWORD)		
		
		elif choice == "no":
			self.USERNAME = raw_input(" * User name: ")
			self.PASSWORD = raw_input(" * Password: ")

		self.ChatService.login(self.USERNAME, self.PASSWORD, self)

		nicks = self.ChatService.list_nicks()
		if nicks:
			print " * The following people are on the server:"
			i = 1
			for n in nicks:
				print "%d. %s" % (i, n)
				i += 1

		groups = sorted(self.ChatService.list_groups())

		if groups:
			print "* The following groups already exist:"
			i = 1
			for g in groups:
				print "%d. %s" % (i, g)
				i += 1

			self.group = raw_input(" * Choose one group or create a new one: ")
		else:
			self.group = raw_input(" * No group, please create a new one: ")

		self.nick = raw_input(" * Input your nick: ")

		self.ChatService.join_group(self.group, self.nick, self)
		
		print " * System: Start chatting!\n * Note: Use '#help' command for more instructions."

		try:
			try:
				while not self.abort:
					line = raw_input('> ').strip()
					if line == '#quit':
						self.ChatService.logout()
						break
					elif line == '#help':
						print " * Help:\n * '#quit': quit chat\n * '#list nicks': list current users\n * 'list groups': list current groups"
					elif line == '#list nicks':
						nicks = self.ChatService.list_nicks()
						if nicks:
							print "* The following people are on the server:"
							i = 1
							for n in nicks:
								print "%d. %s" % (i, n)

					elif line == '#list groups':
						print "* The following groups already exist:"
						i = 1
						for g in sorted(self.ChatService.list_groups()):
							print "%d. %s" % (i, g)
							i += 1

					if line:
						self.ChatService.chat(self.group, self.nick, line)

			except EOFError:
				pass
		finally:
			self.abort = 1
			self._pyroDaemon.shutdown()

class DaemonThread(threadutil.Thread):
	def __init__(self, CC_obj):
		threadutil.Thread.__init__(self)
		self.CC_obj = CC_obj
		self.setDaemon(True)

	def run(self):
		with Pyro4.core.Daemon() as daemon:
			daemon.register(self.CC_obj)
			daemon.requestLoop(lambda: not self.CC_obj.abort)


if __name__ == '__main__':

	
	CC_obj = ChatClient()
	daemonthread = DaemonThread(CC_obj)
	daemonthread.start()
	CC_obj.start()
