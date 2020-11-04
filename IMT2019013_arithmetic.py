from IMT2019013_conversion import *

def ADDMX(memory):
#	print("ADD MX is being performed")
	tmp = toBinary(toInteger(memory["memory"][memory["X"]]) + toInteger(memory["AC"]))
	if len(tmp) < 41:
		memory["AC"] = tmp
		return
	memory["AC"] = tmp[0:1] + tmp[-39:]

def ADDMX_MOD(memory):
#	print("ADD |MX| is being performed")
	tmp = toBinary(abs(toInteger(memory["memory"][memory["X"]])) + toInteger(memory["AC"]))
	if len(tmp) < 41:
		memory["AC"] = tmp
		return
	memory["AC"] = tmp[0:1] + tmp[-39:]

def SUBMX(memory):
#	print("SUB MX is being performed")
	tmp = toBinary(toInteger(memory["AC"]) - toInteger(memory["memory"][memory["X"]]))
	if len(tmp) < 41:
		memory["AC"] = tmp
		return
	memory["AC"] = tmp[0:1] + tmp[-39:]

def SUBMX_MOD(memory):
#	print("SUB |MX| is being performed")
	tmp = toBinary(toInteger(memory["AC"]) - abs(toInteger(memory["memory"][memory["X"]])))
	if len(tmp) < 41:
		memory["AC"] = tmp
		return
	memory["AC"] = tmp[0:1] + tmp[-39:]

def MULMX(memory):
#	print("MUL MX is being performed")
	mx = toInteger(memory["memory"][memory["X"]])
	mq = toInteger(memory["MQ"])
	prod = toBinary(mx * mq)
	if len(prod <= 40):
		memory["AC"] = prod
		return
	memory["AC"] = prod[:40]
	memory["MQ"] = prod[40:]

def DIVMX(memory):
#	print("DIV MX is being performed")
	ac = toInteger(memory["AC"])
	mx = toInteger(memory["memory"][memory["X"]])
	memory["MQ"] = toBinary(ac // mx)
	memory["AC"] = toBinary(ac % mx)

def LSH(memory):
#	print("LSH MX is being performed")
	memory["AC"] = memory["AC"][1:] + "0"

def RSH(memory):
#	print("RSH MX is being performed")
	memory["AC"] = "0" + memory["AC"][:-1]