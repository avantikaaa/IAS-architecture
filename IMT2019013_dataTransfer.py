from IMT2019013_conversion import *

def LOADMQ(memory):
#	print("LOAD MQ is being performed")
	memory["AC"] = memory["MQ"]

def LOADMX_MQ(memory):
#	print("LOAD MQ MX is being performed")
	memory["MQ"] = memory["memory"][memory["X"]]

def STORMX(memory):
#	print("STOR MX is being performed")
	memory["memory"][memory["X"]] = memory["AC"]

def LOADMX(memory):
#	print("LOAD MX is being performed")
	memory["AC"] = memory["memory"][memory["X"]]

def LOADMX_NEG(memory):
#	print("LOAD -MX is being performed")
	memory["AC"] = toBinary(toInteger(memory["memory"][memory["X"]])*(-1))

def LOADMX_MOD(memory):
#	print("LOAD |MX| is being performed")
	memory["AC"] = toBinary(abs(toInteger(memory["memory"][memory["X"]])))

def LOADMX_MOD_NEG(memory):
#	print("LOAD -|MX| is being performed")
	memory["AC"] = toBinary(abs(toInteger(memory["memory"][memory["X"]]))*(-1))

