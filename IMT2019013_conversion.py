def toBinary(n):
	s = ""
	sign = "0"
	if n < 0:
		sign = "1"
		n = abs(n)

	while(n > 0):
		s = str(n%2) + s
		n //= 2
	return sign + "0"*(39 - len(s)) + s

def toInteger(s):
	n = 0
	sign = 1
	if(s[0] == "1"):
		sign = -1
	for i in s[1:]:
		n *= 2
		n += int(i)
	return n * sign