def fix_teen(n):
	if n not in[13,14,17,18,19]:
		return n
	return 0
def sum(m,n,o):
 return fix_teen(m)+fix_teen(n)+fix_teen(o)

a,b,c=eval(input("Enter three numbers..."))
print(sum(a,b,c))
