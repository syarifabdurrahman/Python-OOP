"""
    tanggal: 03 Oktober 2022, 19:11:59 WIB
    magnitudo: 4.1
    kedalaman: 2 km
    lokasi: 5.35 LS - 102.57 BT
    pusat gempa: Pusat gempa berada di laut 33 km tenggara Enggano
    dirasakan: Dirasakan (Skala MMI): II Enggano
"""

from turtle import title
import requests
import bs4 


def ekstraksi_data():
    try:
        content=requests.get('https://www.bmkg.go.id')
    except Exception:
        print(Exception)
        return None

    if content.status_code==200:
        soup = bs4.BeautifulSoup(content.text,'html.parser')

        result= soup.find('span',{'class':'waktu'})
        result= result.text.split(',')
        tanggal= result[0]
        waktu= result[1]
    
        result = soup.find('div',{'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result =result.findChildren('li')
        i=0
        magnitudo=None
        kedalaman=None
        ls=None
        bt=None
        pusat=None
        dirasakan=None

        for rest in result:
            if i == 1:
                magnitudo = rest.text
            elif i == 2:
                kedalaman = rest.text
            elif i == 3:
                koordinat = rest.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                pusat = rest.text
            elif i == 5:
                dirasakan = rest.text
            i+=1

        hasil = dict ()
        hasil["tanggal"] = tanggal
        hasil["waktu"] = waktu
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["lokasi"] = {"ls": ls,"bt" : bt }
        hasil["pusat"] = pusat
        hasil["dirasakan"] = dirasakan
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak menemukan data")
        return

    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal:  {result['tanggal']}")
    print(f"Waktu:  {result['waktu']}")
    print(f"magnitudo:  {result['magnitudo']}")
    print(f"kedalaman:  {result['kedalaman']}")
    print(f"lokasi:  ls= {result['lokasi']['ls']}  bt= {result['lokasi']['bt']}")
    print(f"pusat:  {result['pusat']}")
    print(f"dirasakan:  {result['dirasakan']}")

if __name__ == '__main__':
    print("haio")