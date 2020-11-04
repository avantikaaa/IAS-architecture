from IMT2019013_conversion import *
from IMT2019013_instruction import *

def printMemory(memory):
	for i in memory:
		if i == "memory":
			print("data:")
			for j in memory[i]:
				print(j)
			print("\n\n")
		else:
			print(i, memory[i])

def JUMP_LHS(memory):
	memory["PC"] = memory["X"] - 1
	memory["IBR"] = ""

#	printMemory(memory)

def JUMP_RHS(memory):
#	print("right hand side jump is being performed")
	memory["PC"] = memory["X"]
	memory["IBR"] = memory["memory"][memory["X"]][20:]

def JUMP_CON_LHS(memory):
#	print("conditonal", end=" ")
	if toInteger(memory["AC"]) > -1:
		JUMP_LHS(memory)
#	else:
#		print("jump was not performed as AC < 0")

def JUMP_CON_RHS(memory):
#	print("conditonal", end=" ")
	if toInteger(memory["AC"]) > -1:
		JUMP_RHS(memory)
#	else:
#		print("jump was not performed as AC < 0")