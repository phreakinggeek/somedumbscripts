#!/usr/bin/env python
#hex converter
#PhG and Sonny f'ing off.
import sys

def d2hchar(deccy):
	if deccy >= 0 and deccy <= 9:
		return str(deccy)
	else:
		return chr(ord("A")+(deccy-10))

def h2dchar(hexxy):
	if hexxy >= "0" and hexxy <= "9":
		return int(hexxy)
	else:
		return 10+(ord(hexxy)-ord("A"))

def d2hstr(deccy):
	digit = 0
	hx = ""
	while deccy > (16**digit):
		digit +=1
	while True:
		digit -=1
		if digit<0:
			break
		hx += d2hchar(deccy/(16**digit))
		deccy%=(16**digit)
	return hx

def h2dstr(hexxy):
	digit = 0
	var = 0
	hexxy = hexxy.upper()[::-1]
	for each in hexxy:
		var+=h2dchar(each)*(16**digit)
		digit+=1
	return var

def d2b64char(deccy):
	if deccy >= 0 and deccy < 26:
		return chr(ord("A")+deccy)
	elif deccy >=26 and deccy < 52:
		return chr(ord("a")+(deccy-26))
	elif deccy >=52 and deccy < 62:
		return chr(ord("0")+(deccy-52))
	elif deccy == 63:
		return chr("+")
	else:
		return chr("/")

def b642dchar(busey):
	if busey >="A" and busey <="Z":
		return (ord(busey)-ord("A"))
	elif busey >="a" and busey<="z":
		return (26+ord(busey)-ord("a"))
	elif busey >="0" and busey<="9":
		return (52+ord(busey)-ord("0"))
	elif busey == "+":
		return 62
	else:
		return 63

def d2b64str(deccy):
	digit = 0
	b64 = ""
	while deccy > (64**digit):
		digit +=1
	while True:
		digit -=1
		if digit<0:
			break
		b64 += d2b64char(deccy/(64**digit))
		deccy%=(64**digit)
	return b64

def b642dstr(busey):
	digit = 0
	var = 0
	busey = busey[::-1]
	for each in busey:
		var+=b642dchar(each)*(64**digit)
		digit+=1
	return var

def h2b64(hexxx):
	return d2b64str(h2dstr(hexxx))

def b642h(b64xxx):
	return d2hstr(b642dstr(b64xxx))

class fuckyou(Exception):
	pass

input=sys.argv[2]

if sys.argv[1]=="h":
	for each in input:
		if not ((each >= "0" and each <= "9") or (each >= "A" and each <= "F") or (each >= "a" and each <= "f")):
			print "FUCK YOU INVALID"
			sys.exit()
	print h2b64(input)
elif sys.argv[1]=="b":
	for each in input:
		if not ((each >= "0" and each <= "9") or (each >= "A" and each <= "Z") or (each >= "a" and each <= "z") or (each == "+") or (each == "/")):
			print "FUCK YOU INVALID"
			sys.exit()
	print b642h(input)
else:
	print "FUCK YOU INVALID"

