## EXECUTION OF THE PROGRAM
	- run "IMT2019013_ias_computer.py" in the terminal
## ASSUMPTIONS:
	- "0000000" is the opcode for the halt instruction
	- The input will be VALID:
		-- If there is some data stored before the halt instruction, then there MUST be a jump instruction before the data.
		-- An instruction will always have a valid opcode


## INPUT: "IMT2019013_memory_input.txt"
	- The given opcode for each instruction should be valid, or else the program will give an error
	- The sample file contains:
		5 - Number of instructions
		[0] [No instruction][LOAD M(5)]
		[1] [ADD M(6)] [STOR M(6)]
		[2] [JUMP(3)] [SUB M(5)]
		[3] [SUB M(7)] [STOR M(7)]
		[4] [LSH] [STOR M(5)]
		[5] [HALT]
		[5] 40 bit binary value of 1
		[6] 40 bit binary value of 2
		[7] 40 bit binary value of 1
	- Alterations done by the sample input:
		-- M(7) = M(7) + M(6)
		-- M(8) = M(7) - M(8)
		-- M(6) = RSH(M(7)) (or) M(8) * 2
		* Each line uses updated memory values


##OUTPUT: "IMT2019013_memory_output.txt"
	- The file contains the altered memory after the given set of instructions are executed
