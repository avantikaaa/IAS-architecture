#for decoding
from IMT2019013_instruction import *


#MEMORY
memory = {"MAR": "0"*12, "MBR": "0"*20, "IBR": "", "IR":"0"*8, "AC": "0"*40, "PC": 0, "MQ": "0"*40, "X": 0, "memory": [], "halt": 0}

if __name__ == "__main__":
	#do something
	#get memory from somewhere
	f = open("IMT2019013_memory_input.txt", "r")

	
	memory["memory"] = [i[:-1] for i in f.readlines()]		#to remove the "\n" character

	while not memory["halt"]:		
		if memory["memory"][memory["PC"]][:20] == "1"*20:
			memory["IBR"] = ""
			memory["MBR"] = memory["memory"][memory["PC"]][20:]
		else:
			memory["IBR"] = memory["memory"][memory["PC"]][20:]
			memory["MBR"] = memory["memory"][memory["PC"]][:20]
		memory["IR"] = memory["MBR"][:8]		#opcode
		memory["MAR"] = memory["MBR"][8:]		#address
		memory["X"] = toInteger(memory["MAR"])
		
		instruction(memory["IR"])(memory)

		if(memory["IBR"]):
			memory["MBR"] = memory["IBR"][:]
			memory["IR"] = memory["MBR"][:8]
			memory["MAR"] = memory["MBR"][8:]
			memory["X"] = toInteger(memory["MAR"])
			instruction(memory["IR"])(memory)

		memory["PC"] += 1

	f.close()
	f = open("IMT2019013_memory_output.txt", "w")
	for i in memory["memory"]:
		f.write(i + "\n")
	f.close()
