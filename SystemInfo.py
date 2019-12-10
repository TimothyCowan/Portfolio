import re, uuid, socket

HOSTNAME = socket.gethostname()
ipadd = socket.gethostbyname(HOSTNAME)
mac_add = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
print('[Hostname]>>' + HOSTNAME + ' [Ipv4 Address]>>' + ipadd, " [Mac Address]>>" + mac_add)
