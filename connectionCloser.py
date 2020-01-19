#! /bin/python3 -B

import vici


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class connectionCloser:
	def __init__(self):
		self.session=vici.Session()

	def main(self):
		# get all configurations
		configurations = self.session.get_conns()
		# unload all configurations
		for i in configurations["conns"]:
			self.session.unload_conn({"name" : i })
		# get all connections
		connections=[]
		for i in self.session.list_sas():
			connections.append(i)
		# terminate all IKE SAs
		for i in connections:
			for j in i.keys():
				print("Terminating SA {}".format(i[j]["uniqueid"]))
				terminatingSession = self.session.terminate({
				"ike-id" : i[j]["uniqueid"],
				"force" : True,
				"timeout" : 0,
				"loglevel" : -1
				})
				for k in terminatingSession:
					print(k)
if __name__ == '__main__':
	closer = connectionCloser()
	closer.main()
