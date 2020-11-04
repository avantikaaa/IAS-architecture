def STOR_LHS(memory):
	memory["memory"][memory["X"]] = memory["memory"][memory["X"]][:8] + memory["AC"][-12:] + memory["memory"][memory["X"]][20:]

def STOR_RHS(memory):
	memory["memory"][memory["X"]] = memory["memory"][memory["X"]][:28] + memory["AC"][-12:]