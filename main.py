"""
applikasi deteksi gempa
MODULARISASI dengan function
"""

# from gempa_terkini import ekstraksi_data,tampilkan_data
import gempa_terkini


if __name__ == '__main__':
    result = gempa_terkini.ekstraksi_data()
    gempa_terkini.tampilkan_data(result)

