
import commands


FLAG="SECCON{"

WORD="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz-_{}0123456789"

f=open("encflag","rb")

ENC=f.read()

for i in range(25):
	for alph in WORD:

		ARG1 = FLAG+alph
		
		b = commands.getoutput('./cryptooo '+ARG1).split(": ")[1]

		idx = len(FLAG)

		if ENC[idx] == b.decode("base64")[idx]:
			FLAG += alph
			break

print FLAG









