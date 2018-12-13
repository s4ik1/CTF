import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib
import commands
from PIL import Image
import itertools

def EXEC(data):
	return commands.getoutput(data)

def download(urls):
	for i in range( len(urls) ):
		url = urls[i].get('src')[:-1]

		src = urllib2.urlopen(url)
		dst = open("QR/"+str(i)+".png", 'wb')
		dst.write(src.read())
		src.close()
		dst.close()


def readQR():

	TOPs	= [ TOP[0],TOP[1]       ]
	BOTTOMs = [ BOTTOM[0],BOTTOM[1] ]
	LEFTs	= [ LEFT[0],LEFT[1]     ]
	RIGHTs	= [ RIGHT[0],RIGHT[1]   ]
	CENTERs	= [ CENTER[0],CENTER[1],CENTER[2],CENTER[3] ]

	P1 = list( itertools.permutations( TOPs    ,2) )
	P2 = list( itertools.permutations( LEFTs   ,2) )
	P3 = list( itertools.permutations( RIGHTs  ,2) )
	P4 = list( itertools.permutations( BOTTOMs ,2) )
	P5 = list( itertools.permutations( CENTERs ,4) )

	# KOKO DAME
	for T in P1:
		for L in P2:
			for R in P3:
				for B in P4:
					for C in P5:

						LINE1 =  CORNER[0].filename+" "
						LINE1 += T[0].filename+" "
						LINE1 += T[1].filename+" "
						LINE1 += CORNER[1].filename


						CMD = "convert +append "+ LINE1 +" LINE1.png"
						EXEC(CMD)

						LINE2 =  L[0].filename+" "
						LINE2 += C[0].filename+" "
						LINE2 += C[1].filename+" "
						LINE2 += R[0].filename

						CMD = "convert +append "+ LINE2 +" LINE2.png"
						EXEC(CMD)
						LINE3 =  L[1].filename+" "
						LINE3 += C[2].filename+" "
						LINE3 += C[3].filename+" "
						LINE3 += R[1].filename

						CMD="convert +append "+ LINE3 +" LINE3.png"
						EXEC(CMD)
						LINE4 =  CORNER[2].filename+" "
						LINE4 += B[0].filename+" "
						LINE4 += B[1].filename+" "
						LINE4 += CORNER[3].filename


						CMD = "convert +append "+ LINE4 +" LINE4.png"
						EXEC(CMD)

						EXEC("convert -append LINE1.png LINE2.png LINE3.png LINE4.png ./QR.png")
						ANS=EXEC("zbarimg -q ./QR.png")

						if ":" in ANS:
								return ANS.split(":")[1]
	return False





URL="http://puzzle.quals.seccon.jp:42213/slidepuzzle"

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
response= opener.open(URL)

f = Image.new("RGB",(53,53),(255,255,255))
f.save("block.png")

BLOCK = Image.open("block.png")

BLACK = 0
WHITE = 255

for CNT in range(50):

	html = BeautifulSoup(response,"lxml")

	ACTION = html.find("form").get("action")

	print str(html).split("<body>")[1].split("<br/>")[0],

	Imgs = html.find_all('img')

	download(Imgs)

	TOP    = []
	BOTTOM = []
	LEFT   = []
	RIGHT  = []
	CENTER = []
	CORNER = ["NULL"]*4

	size 	= 52
	padding = 10

	for j in range( len(Imgs) ):
		img = Image.open("QR/"+str(j)+".png")

		for k in range(size):
			if  not (img.getpixel((k,padding))   == WHITE and \
					 img.getpixel((padding,k))   == WHITE and \
					 img.getpixel((k,padding+3)) == WHITE and \
					 img.getpixel((padding+3,k)) == WHITE ):
				break
		else:
			CORNER[0] = img
			continue

		for l in range(size):
			if  not (img.getpixel((l,padding)) 		  == WHITE and \
					 img.getpixel((size-padding,l))   == WHITE and \
					 img.getpixel((l,padding+3)) 	  == WHITE and \
					 img.getpixel((size-padding+3,l)) == WHITE ):
				break
		else:
			CORNER[1] = img
			continue

		for m in range(size):
			if  not (img.getpixel((m,size-padding))   == WHITE and \
					 img.getpixel((padding,m))   	  == WHITE and \
					 img.getpixel((m,size-padding+3)) == WHITE and \
					 img.getpixel((padding+3,m)) 	  == WHITE ):
				break
		else:
			CORNER[2] = img
			continue

		for n in range(53):
			if  not (img.getpixel((n,size-padding))   == WHITE and \
					 img.getpixel((size-padding,n))   == WHITE and \
					 img.getpixel((n,size-padding+3)) == WHITE and \
					 img.getpixel((size-padding+3,n)) == WHITE ):
				break
		else:
			CORNER[3] = img
			continue


		for o in range(53):
			if not (img.getpixel((o,padding)) == WHITE and img.getpixel((o,padding+3)) == WHITE):
				break
		else:
			TOP.append(img)
			continue

		for p in range(53):
			if not (img.getpixel((padding,p)) == WHITE and img.getpixel((padding+3,p)) == WHITE):
				break
		else:
			LEFT.append(img)
			continue

		for q in range(53):
			if not (img.getpixel((size-padding,q)) == WHITE and img.getpixel((size-padding+3,q)) == WHITE):
				break
		else:
			RIGHT.append(img)
			continue

		for r in range(53):
			if not (img.getpixel((r,size-padding)) == WHITE and img.getpixel((r,size-padding+3)) == WHITE):
				break
		else:
			BOTTOM.append(img)
			continue

		for s in range(53):
			if img.getpixel((s,s)) == (0,0,0):
					break
		else:
			CENTER.append(img)
		
	for A in [TOP,LEFT,RIGHT,BOTTOM]:
		if not len(A) == 2:
			A.append(BLOCK)
			break
	if not len(CENTER) == 4:
			CENTER.append(BLOCK)

	if "NULL" in CORNER:
		if CORNER[3] == "NULL":
			CORNER[3] = BLOCK
		else:
			idx = CORNER.index("NULL")
			CORNER[idx] = Image.open("CORNER"+str(idx)+".png")

	ANS = readQR()

	if ANS:
		params = urllib.urlencode({'text':ANS})
		URL = "http://puzzle.quals.seccon.jp:42213/" + ACTION
		response = opener.open(URL,params)
	else:
		print "Connot Reaing ;("
		exit()

print BeautifulSoup(response,"lxml")














