import subprocess

def main():

	for i in range(1000):
		amida=setAmida()
		#print amida
		amida=amida.split("\n")
		
		if amida[1][1]=="-":
			amida=rotateAmida(amida)
			
		if "*" in amida[1]:
			amida=reverseAmida(amida)
		
		ans=str(solve(amida))
		p.stdin.write(ans+"\n")
		
		print str(i+1)+":"+ans
	
	print p.stdout.read(100)


def solve(amida):

	pos=amida[len(amida)-2].index("*")
	
	for j in reversed(range(1,21)):
		
		if pos!=len(amida[j])-1 and amida[j][pos+1]=="-":
			while True:
				pos+=1
				if amida[j][pos]=="|":
					break
		
		elif pos!=0 and amida[j][pos-1]=="-":
			while True:
				pos-=1
				if amida[j][pos]=="|":
					break
					
	return amida[1][pos]


def setAmida():
	amida=""
	temp1=""
	
	while True:
		temp=p.stdout.read(1)
		
		if temp=="?":
			return amida
		elif temp=="W":
			print "Wrong"
			return 0
		elif temp=="\x00":
			continue
		
		amida+=temp


def reverseAmida(amida):
		ramida=amida[::-1]
		return ramida


def rotateAmida(amida):
	rtamida=""
	rtamida+=amida[0]+"\n"
	length=len(amida)-1
	
	for x in range(21):
		for y in reversed(range(1,length)):
			if amida[y][x]=="|":
				rtamida+="-"
			elif amida[y][x]=="-":
				rtamida+="|"
			else :
				rtamida+=amida[y][x]
		rtamida+="\n"
	
	rtamida=rtamida.split("\n")
	return rtamida

if __name__ == "__main__":
	p = subprocess.Popen(["./amida"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	main()
