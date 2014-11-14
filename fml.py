#!/usr/bin/env python
#fml
#sonny and phg

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

def xor0(xora,xorb):
	strung = ""
	for each in range(0,len(xora)):
		strung += d2hchar(h2dchar(xora[each].upper())^h2dchar(xorb[each].upper()))
	return strung

print xor0("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
print ("746865206b696420646f6e277420706c6179".upper())