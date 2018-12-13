import urllib
import urllib2
from bs4 import BeautifulSoup
import cookielib
import commands
from PIL import Image

def fillPix(x,y,color):
	for i in range(10):
		for j in range(10):
			X = x*10+j
			Y = y*10+i
			img.putpixel((X,Y),color)
	return 0

def perseNum(data):
	span = str(data.find_all("span"))
	span = span.split("<span>")[1:]
	num = ""
	for c in span:
		num += c.split("</span>")[0]
		num += ","
	return num[:-1]


URL="http://qrlogic.pwn.seccon.jp:10080/game/"

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
response= opener.open(URL)

for CNT in range(30):

	html = BeautifulSoup(response,"lxml")

	print str(html).split("<body>")[1].split("<br/>")[0]

	TATEs = html.find_all("tr")[0].find_all("th", class_="cols")
	YOKOs = html.find_all("tr")[1:]

	N = len(YOKOs)
	f=open("picross","w")

	f.write("width "+str(N)+"\n"+"height "+str(N)+"\n\n")

	f.write("rows\n\n")
	YOKO = [""]*N
	for i in range(N):
		YOKO[i] = perseNum( YOKOs[i].find_all("th",class_="rows")[0] )
		f.write(YOKO[i]+"\n\n")


	f.write("\n\ncolumns\n\n")
	TATE = [""]*N
	for i in range(N):
		TATE[i] = perseNum( TATEs[i] )
		f.write(TATE[i]+"\n\n")

	f.close()


	QRs = commands.getoutput("wine ./nonogram.exe -i picross")

	s = len(QRs)/N+1
	QRs = QRs.split("\n")

	#Bruteforce NONOGRAMs
	for i in range( s ):
		QR = QRs[ i*(N+1):(i+1)*(N+1) ]

		#Create QR image
		img = Image.new("RGB",(N*10,N*10),(255,255,255))
		for y in range(N):
			for x in range(N):
				if  QR[y][x] == "-":
					fillPix(x,y,(255,255,255))
				else:
					fillPix(x,y,(0,0,0))
		img.save("QR.bmp")

		ANS=commands.getoutput("zbarimg -q ./QR.bmp")

		if ":" in ANS:
			break

	ANS = ANS.split(":")[1]
	params = urllib.urlencode({'ans':ANS})
	response = opener.open(URL,params)


print ANS






