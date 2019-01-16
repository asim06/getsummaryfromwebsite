import requests
from bs4 import BeautifulSoup

#Site tarafından bloklanmamak için gönderdiğimiz tarayıcı bilgileri
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


print("Lütfen bekleyin... Haberler çekiliyor...\n")

#isteğin yapılacağı adres
url= "https://www.tgrthaber.com.tr/ekonomi"
istek=requests.get(url,headers)

icerik=istek.content
soup = BeautifulSoup(icerik, "lxml")

print(" LİNKlER VE  HABERLER ŞU ŞEKİLDE:\n ------------------------------")


haberler = soup.find_all("div",{"class": "altmanset-alani-text"})

sayi = 1
for i in haberler:
    if sayi == 1:
        sayi += 1
        continue
    print(sayi, "-)", i.text)
    sayi += 1


say = 1
for i in haberler:

    #haberlinklerin bir değişkene atılması
    haberlerLink = i.a.get("href")
    #alınan linklerden yeni isteklerin oluşturulması
    istek2 = requests.get(haberlerLink,headers)
    istek_soup = BeautifulSoup(istek2.content,"lxml")
    metin = istek_soup.find_all("div",{"id":"detail-body"})
    print("\n************")
    for j in metin:
        print(say,".haber ---->  ",j.text)
        say+=1

    # aldığımız linklerin özeti çekebilmek için kontrol ediyoruz, 200 ise başarlı
    #print(istek2.status_code)














