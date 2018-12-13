import hashlib

S=[[]*28]*28
S[0]  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{}"
S[1]  = "BCDEFGHIJKLMNOPQRSTUVWXYZ{}A"
S[2]  = "CDEFGHIJKLMNOPQRSTUVWXYZ{}AB"
S[3]  = "DEFGHIJKLMNOPQRSTUVWXYZ{}ABC"
S[4]  = "EFGHIJKLMNOPQRSTUVWXYZ{}ABCD"
S[5]  = "FGHIJKLMNOPQRSTUVWXYZ{}ABCDE"
S[6]  = "GHIJKLMNOPQRSTUVWXYZ{}ABCDEF"
S[7]  = "HIJKLMNOPQRSTUVWXYZ{}ABCDEFG"
S[8]  = "IJKLMNOPQRSTUVWXYZ{}ABCDEFGH"
S[9]  = "JKLMNOPQRSTUVWXYZ{}ABCDEFGHI"
S[10] = "KLMNOPQRSTUVWXYZ{}ABCDEFGHIJ"
S[11] = "LMNOPQRSTUVWXYZ{}ABCDEFGHIJK"
S[12] = "MNOPQRSTUVWXYZ{}ABCDEFGHIJKL"
S[13] = "NOPQRSTUVWXYZ{}ABCDEFGHIJKLM"
S[14] = "OPQRSTUVWXYZ{}ABCDEFGHIJKLMN"
S[15] = "PQRSTUVWXYZ{}ABCDEFGHIJKLMNO"
S[16] = "QRSTUVWXYZ{}ABCDEFGHIJKLMNOP"
S[17] = "RSTUVWXYZ{}ABCDEFGHIJKLMNOPQ"
S[18] = "STUVWXYZ{}ABCDEFGHIJKLMNOPQR"
S[19] = "TUVWXYZ{}ABCDEFGHIJKLMNOPQRS"
S[20] = "UVWXYZ{}ABCDEFGHIJKLMNOPQRST"
S[21] = "VWXYZ{}ABCDEFGHIJKLMNOPQRSTU"
S[22] = "WXYZ{}ABCDEFGHIJKLMNOPQRSTUV"
S[23] = "XYZ{}ABCDEFGHIJKLMNOPQRSTUVW"
S[24] = "YZ{}ABCDEFGHIJKLMNOPQRSTUVWX"
S[25] = "Z{}ABCDEFGHIJKLMNOPQRSTUVWXY"
S[26] = "{}ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S[27] = "}ABCDEFGHIJKLMNOPQRSTUVWXYZ{"


K  = "????????????"
P  = "SECCON{???????????????????????????????????}"
C  = "LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ"
K1 = ""

for i in range(7):
	IDX = S[0].find(P[i])
	for j in range(len(S)):
		if C[i] == S[j][IDX]:
			K1 += S[0][j]
			break
print K1
K2 = K1
K1+="?????"
P1=""

for i in range(len(P)):
	if K1[i%12] == "?":
		P1 += "?,"
		continue
	P1+=S[0][S[S[0].find(K1[i%12])].find(C[i])]+","
print "".join(P1.split(",")[:-1])

P2 = P1.split(",")[:-1]
HASH= "f528a6ab914c1ecf856a1d93103948fe"
for a in S[0]:
	for b in S[0]:
		for c in S[0]:
			for d in S[0]:
				for e in S[0]:
					WORD = a+b+c+d+e
					WORD = K2+WORD
 					for i in range(len(P)):
 						if K1[i%12] == "?":
							P2[i] = S[0][S[S[0].find(WORD[i%12])].find(C[i])]
					P2="".join(P2)
					if HASH == hashlib.md5(P2).hexdigest():
						print WORD
						print P2
						exit()
					P2 = P1.split(",")[:-1]

print "FAILED ;("

