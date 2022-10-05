"""
    tanggal: 03 Oktober 2022, 19:11:59 WIB
    magnitudo: 4.1
    kedalaman: 2 km
    lokasi: 5.35 LS - 102.57 BT
    pusat gempa: Pusat gempa berada di laut 33 km tenggara Enggano
    dirasakan: Dirasakan (Skala MMI): II Enggano
"""

# Method = fungsi
# field / attribut = variabel

import requests
import bs4


class GempaTerkini:
    def __init__(self):
        self.description='To get the latest earthquake information in indonesia form BMKG.go.id\n'
        self.result=None

    def ekstraksi_data(self):
        try:
            content = requests.get('https://www.bmkg.go.id')
        except Exception:
            print(Exception)
            return None

        if content.status_code == 200:
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
            self.result = hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print("Tidak menemukan data")
            return

        print("Gempa terakhir berdasarkan BMKG")
        print(f"Tanggal:  {self.result['tanggal']}")
        print(f"Waktu:  {self.result['waktu']}")
        print(f"magnitudo:  {self.result['magnitudo']}")
        print(f"kedalaman:  {self.result['kedalaman']}")
        print(f"lokasi:  ls= {self.result['lokasi']['ls']}  bt= {self.result['lokasi']['bt']}")
        print(f"pusat:  {self.result['pusat']}")
        print(f"dirasakan:  {self.result['dirasakan']}")

if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini()
    print('Deskripsi class ', gempa_di_indonesia.description)
    gempa_di_indonesia.ekstraksi_data()
    gempa_di_indonesia.tampilkan_data()