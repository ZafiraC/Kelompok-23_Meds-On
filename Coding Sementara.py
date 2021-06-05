import csv
import os.path
from os import path

total1=0
jenis1=""
jmlapd=0
jml_vit=0
jml_obat=0

dataAPD = []
dataVitamin = []
dataObat = []
dataKonsul = []

def menu():
    print("\n----------- Meds-On ------------")
    print("[1] APD")
    print("[2] Vitamin")
    print("[3] Obat Generik")
    print("[4] Konsultasi Dokter")

def APD():
    global total1
    global jmlapd
    global jenis1
    print ("\n---------- Daftar Menu APD -----------")
    print("1. Masker")
    print("2. Face Shield")
    print("3. Hand Sanitizer")
    nomor=int(input("Mau yang mana ? : "))

    if nomor==1:
        print("[1] Sensi N95        : Rp 150.000")
        print("[2] Sensi Duckbill   : Rp 140.000")
        print("[3] Sensi Headloop   : Rp 137.500")
        print("[4] Sensi Earloop    : Rp 115.000")

        masker = int(input("Pilih yang mana? : "))
        jmlapd = int(input("Jumlah : "))

        if masker==1:
            total1=jmlapd*150000
            print (jmlapd," box Sensi N95 : Rp", total1)
            jenis1=("Sensi N95")
        elif masker==2:
            total1 = jmlapd*140000
            print(jmlapd, " box Sensi Duckbill : Rp", total1)
            jenis1 = ("Sensi Duckbill")
        elif masker==3:
            total1 = jmlapd*137500
            print(jmlapd, " box Sensi Headloop : Rp", total1)
            jenis1 = ("Sensi Headloop")
        elif masker==4:
            total1 = jmlapd*115000
            print(jmlapd, " box Sensi Earloop : Rp", total1)
            jenis1 = ("Sensi Earloop")
        else:
            print("Maaf perintah yang Anda masukkan salah!")

    elif nomor==2:
        print("[1] Premium      : Rp 15.000")
        print("[2] Akrilik      : Rp 20.000")
        print("[3] Anak         : Rp 12.000")

        face = int(input("Pilih yang mana? : "))
        jmlapd = int(input("Jumlah : "))

        if face==1:
            total1=jmlapd*15000
            print (jmlapd, " Face Shield Premium : Rp", total1)
            jenis1=("Face Shield Premium")
        elif face==2:
            total1 = jmlapd*20000
            print(jmlapd, " Face Shield Anti Embun : Rp", total1)
            jenis1 = ("Face Shield Akrilik")
        elif face==3:
            total1 = jmlapd*12000
            print(jmlapd, " Face Shield Anti Embun : Rp", total1)
            jenis1 = ("Face Shield Anak-anak")
        else:
            print("Maaf perintah yang Anda masukkan salah!")

    elif nomor==3:
        print("[1] Antis Spray      : Rp 9.500")
        print("[2] Antis Gel        : Rp 7.000")
        print("[3] Nuvo Gel         : Rp 7.500")
        print("[4] Dettol Spray     : Rp 7.500")

        hand = int(input("Pilih yang mana? : "))
        jmlapd = int(input("Jumlah : "))

        if hand==1:
            total1=jmlapd*9500
            print (jmlapd, " Antis Spray : Rp", total1)
            jenis1=("Antis Spray")
        elif hand==2:
            total1 = jmlapd*7000
            print(jmlapd, " Antis Gel : Rp", total1)
            jenis1 = ("Antis Gel")
        elif hand==3:
            total1 = jmlapd*7500
            print(jmlapd, " Nuvo Gel : Rp", total1)
            jenis1 = ("Nuvo Gel")
        elif hand==4:
            total1 = jmlapd*7500
            print(jmlapd, " Dettol Spray : Rp", total1)
            jenis1 = ("Dettol Spray")
        else:
            print("Maaf perintah yang Anda masukkan salah!")
    else:
      print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
      APD()

    APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total1}
    dataAPD.append(APD.copy())

    keys = dataAPD[0].keys()
    with open('data.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataAPD)

total2=0
jenis2=""

def Vitamin():
    global total2
    global jenis2
    global jml_vit
    print("\n---------- Daftar Menu Vitamin ----------")
    print("1. Imboost Effervescent With Vitamin C: Rp 30.000")
    print("2. Redoxon Double Action Isi 10       : Rp 35.000")
    print("3. CDR Fortos isi 10                  : Rp 40.000")
    print("4. Enervon C Tablet Isi 30            : Rp 45.000")
    nomor=int(input("Pilih yang mana? : "))
    jml_vit = int(input("Mau beli berapa? : "))

    if nomor==1:
       total2=jml_vit*30000
       print (jml_vit," Imboost Effervescent With Vitamin C : Rp.", total2)
       jenis2=("Imboost Effervescent With Vitamin C")
    elif nomor==2:
       total2=jml_vit*35000
       print (jml_vit, " Redoxon Double Action Isi 10 : Rp.", total2)
       jenis2=("Redoxon Double Action Isi 10")
    elif nomor==3:
       total2=jml_vit*40000
       print (jml_vit, " CDR Fortos isi 10 : Rp.", total2)
       jenis2=("CDR Fortos isi 10")
    elif nomor==4:
       total2=jml_vit*45000
       print (jml_vit, " Enervon C Tablet : Rp.", total2)
       jenis2=("Enervon C Tablet")
    else:
      print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
      Vitamin()

    Vitamin = {"No": nomor, "Jenis": jenis2, "Jumlah": jml_vit, "Harga": total2}
    dataVitamin.append(Vitamin.copy())

    keys = dataVitamin[0].keys()
    with open('data.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataVitamin)

total3 = 0
jenis3 = ""

def Obat():
    global total3
    global jml_obat
    global jenis3
    print("\n---------- Daftar Menu Obat Generik -----------")
    print("1. Obat Penurun Panas")
    print("2. Obat Batuk")
    print("3. Obat Flu")
    print("4. Obat Pusing")
    print("5. Obat Maag")
    nomor = int(input("Mau yang mana ? : "))

    if nomor == 1:
        print("[1] Paracetamol Tablet 500mg Isi 10       : Rp 3000")
        print("[2] Sanmol Paracetamol Tablet 500mg Isi 4 : Rp 1500")
        print("[3] Ibuprofen Tablet 400 mg Isi 10        : Rp 4000")
        print("[4] Termorex Paracetamol Sirup Anak       : Rp 16000")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))

        if obat == 1:
            total3 = jml_obat * 3000
            print(jml_obat, "Paracetamol Tablet 500mg Isi 10 : Rp", total3)
            jenis3 = ("Paracetamol Tablet 500mg Isi 10")
        elif obat == 2:
            total3 = jml_obat * 1500
            print(jml_obat, "Sanmol Paracetamol Tablet 500mg Isi 4 : Rp", total3)
            jenis3 = ("Sanmol Paracetamol Tablet 500mg Isi 4")
        elif obat == 3:
            total3 = jml_obat * 4000
            print(jml_obat, "Ibuprofen Tablet 400 mg Isi 10 : Rp", total3)
            jenis3 = ("Ibuprofen Tablet 400 mg Isi 10")
        elif obat == 4:
            total3 = jml_obat * 16000
            print(jml_obat, "Termorex Paracetamol Sirup Anak : Rp", total3)
            jenis3 = ("Termorex Paracetamol Sirup Anak")
        else:
            print("Maaf perintah yang Anda masukkan salah!")

    elif nomor == 2:
        print("[1] Siladex ME 60 ml (batuk berdahak)                  : Rp 16000")
        print("[2] Vicks Formula 44 (batuk kering dan berdahak)       : Rp 22000")
        print("[3] Benadryl Original (batuk kering dengan rasa gatal) : Rp 25000")
        print("[4] Woods Antitussive 100 ml (batuk tidak berdahak)    : Rp 33000")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))

        if obat == 1:
            total3 = jml_obat * 16000
            print(jml_obat, "Siladex ME 60 ml : Rp", total3)
            jenis3 = ("Siladex ME 60 ml")
        elif obat == 2:
            total3 = jml_obat * 22000
            print(jml_obat, "Vicks Formula 44 : Rp", total3)
            jenis3 = ("Vicks Formula 44")
        elif obat == 3:
            total3 = jml_obat * 25000
            print(jml_obat, "Benadryl Original : Rp", total3)
            jenis3 = ("Benadryl Original")
        elif obat == 4:
            total3 = jml_obat * 33000
            print(jml_obat, "Woods Antitussive 100 ml : Rp", total3)
            jenis3 = ("Woods Antitussive 100 ml")

    elif nomor == 3:
        print("[1] Inza          : Rp 2000")
        print("[2] Mixagrip Flu  : Rp 3000")
        print("[3] Neozep Forte  : Rp 3000")
        print("[4] Decolgen Flu  : Rp 3000")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))

        if obat == 1:
            total3 = jml_obat * 2000
            print(jml_obat, " Inza : Rp", total3)
            jenis3 = ("Inza")
        elif obat == 2:
            total3 = jml_obat * 3000
            print(jml_obat, " Mixagrip Flu : Rp", total3)
            jenis3 = ("Mixagrip Flu")
        elif obat == 3:
            total3 = jml_obat * 3000
            print(jml_obat, " Neozep Forte : Rp", total3)
            jenis3 = ("Neozep Forte")
        elif obat == 4:
            total3 = jml_obat * 3000
            print(jml_obat, " Decolgen Flu : Rp", total3)
            jenis3 = ("Decolgen Flu")
        else:
            print("Maaf perintah yang Anda masukkan salah!")

    elif nomor == 4:
        print("[1] Bodrex Migra    : Rp 2500")
        print("[2] Konimex Paramex : Rp 3000")
        print("[3] Panadol Regular : Rp 9000")
        print("[4] Panadol Extra   : Rp 9000")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))

        if obat == 1:
            total3 = jml_obat * 2500
            print(jml_obat, " Bodrex Migra  : Rp", total3)
            jenis3 = ("Bodrex Migra ")
        elif obat == 2:
            total3 = jml_obat * 3000
            print(jml_obat, " Konimex Paramex : Rp", total3)
            jenis3 = ("Konimex Paramex")
        elif obat == 3:
            total3 = jml_obat * 9000
            print(jml_obat, " Panadol Regular : Rp", total3)
            jenis3 = ("Panadol Regular")
        elif obat == 4:
            total3 = jml_obat * 9000
            print(jml_obat, " Panadol Extra : Rp", total3)
            jenis3 = ("Panadol Extra")
        else:
            print("Maaf perintah yang Anda masukkan salah!")

    elif nomor == 5:
        print("[1] Mylanta Liquid    : Rp 45.000")
        print("[2] Promag Strip      : Rp 9.000")
        print("[3] Mylanta Tablet    : Rp 8.000")
        print("[4] Polysilane Strip  : Rp 6.800")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))

        if obat == 1:
            total3 = jml_obat * 45000
            print(jml_obat, " Mylanta Liquid  : Rp", total3)
            jenis3 = ("Mylanta Liquid")
        elif obat == 2:
            total3 = jml_obat * 9000
            print(jml_obat, " Promag Strip : Rp", total3)
            jenis3 = ("Promag Strip")
        elif obat == 3:
            total3 = jml_obat * 8000
            print(jml_obat, " Mylanta Tablet : Rp", total3)
            jenis3 = ("Mylanta Tablet")
        elif obat == 4:
            total3 = jml_obat * 6800
            print(jml_obat, " Polysilane Strip : Rp", total3)
            jenis3 = ("Polysilane Strip")
        else:
            print("Maaf perintah yang Anda masukkan salah!")
    else:
        print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
        Obat()

    Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total3}
    dataObat.append(Obat.copy())

    keys = dataObat[0].keys()
    with open('data.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataObat)

nama=""
def Dokter():
    global nama
    print("\n---------- Booking Konsultasi Dokter ----------")
    print("1. Dokter Umum")
    print("2. Dokter Anak")
    print("3. Dokter Gigi")
    print("4. Dokter Kandungan")
    print("5. Dokter Kulit & Kelamin")
    print("6. Dokter THT")
    dokter = int(input("Pilih dokter yang bersangkutan: "))

    if dokter == 1:
        print("[1] dr. Sulistyo Santoso")
        print("[2] dr. Olivia Dwimaswasti")
        print("[3] dr. Eka Selvia")
        no_dokter = int(input("Nama dokter: "))
        if no_dokter == 1:
            nama = "dr. Sulistyo Santoso"
        elif no_dokter == 2:
            nama = "dr. Olivia Dwimaswasti"
        elif no_dokter == 3:
            nama = "dr. Eka Selvia"

    elif dokter == 2:
        print("[1] dr. Yohnny Sugiarto, Sp.A")
        print("[2] dr. Rustam Siregar, Sp.A")
        no_dokter = int(input("Nama dokter: "))
        if no_dokter == 1:
            nama = "dr. Yohnny Sugiarto, Sp.A"
        elif no_dokter == 2:
            nama = "dr. Rustam Siregar, Sp.A"

    elif dokter == 3:
        print("[1] drg. Christine Windayani, Sp.KG")
        print("[2] drg. Benny Widianto, Sp.BM")
        no_dokter = int(input("Nama dokter: "))
        if no_dokter == 1:
            nama = "drg. Christine Windayani, Sp.KG"
        elif no_dokter == 2:
            nama = "drg. Benny Widianto, Sp.BM"
    elif dokter == 4:
        print("[1] dr. Tommy Febrianto, Sp.OG")
        print("[2] dr. Sandie Farina, Sp.OG")
        no_dokter = int(input("Nama dokter: "))
        if no_dokter == 1:
            nama = "dr. Tommy Febrianto, Sp.OG"
        elif no_dokter == 2:
            nama = "dr. Sandie Farina, Sp.OG"

    elif dokter == 5:
        print("[1] dr. Andreas Widiansyah, Sp.KK")
        print("[2] dr. Ratih Pramuningtyas, Sp.KK")
        no_dokter = int(input("Nama dokter: "))
        if no_dokter == 1:
            nama = "dr. Andreas Widiansyah, Sp.KK"
        elif no_dokter == 2:
            nama = "dr. Ratih Pramuningtyas, Sp.KK"

    elif dokter == 6:
        print("[1] dr. Ahmad Nurdiansyah, Sp.THT-KL")
        print("[2] dr. Dewi Pratiwi, Sp.THT-KL., M.Kes")
        no_dokter = int(input("Nama dokter: "))
        if no_dokter == 1:
            nama = "dr. Ahmad Nurdiansyah, Sp.THT-KL"
        elif no_dokter == 2:
            nama = "dr. Dewi Pratiwi, Sp.THT-KL., M.Kes"

    else:
        print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
        Dokter()

waktu = ""
def Jadwal():
    global waktu
    print("Silakan pilih jadwal konsultasi!")
    tanggal = int(input("Tanggal : "))
    bulan = int(input("Bulan    : "))
    print("Pilihan waktu konsultasi\n"
            "[1] 10.00 - 12.00\n"
            "[2] 13.00 - 15.00\n"
            "[3] 19.00 - 21.00\n")
    jam = int(input("Waktu    :"))
    if jam == 1:
        waktu = "10.00 - 12.00"
    elif jam == 2:
        waktu = "13.00 - 15.00"
    elif jam == 3:
        waktu = "19.00 - 21.00"

    Konsul = {"Nama Dokter": nama, "Tanggal": tanggal, "Bulan": bulan, "Waktu": waktu, "Uang Muka": "Rp 50.000"}
    dataKonsul.append(Konsul.copy())

    keys = dataKonsul[0].keys()
    with open('konsultasi.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataKonsul)


def lihatpesanan():
    print("----------------------------------------")
    print("-------------APD----------------")
    print("Nomor \tNama Pesanan \tJumlah \tHarga")
    for i in range(len(dataAPD)):
        print(str(i + 1), '\t', dataAPD[i]["Jenis"], '\t', dataAPD[i]["Jumlah"], '\t', dataAPD[i]["Harga"])

    print("\n-------------Vitamin----------------")
    print("Nomor \tNama Pesanan \tJumlah \tHarga")
    for i in range(len(dataVitamin)):
        print(str(i + 1), '\t', dataVitamin[i]["Jenis"], '\t', dataVitamin[i]["Jumlah"], '\t', dataVitamin[i]["Harga"])

    print("\n-------------Obat Generik----------------")
    print("Nomor \tNama Pesanan \tJumlah \tHarga")
    for i in range(len(dataObat)):
        print(str(i + 1), '\t', dataObat[i]["Jenis"], '\t', dataObat[i]["Jumlah"], '\t', dataObat[i]["Harga"])

    print("\n-------------Konsultasi Dokter----------------")
    print("Nomor \tNama Dokter \t\t\tTanggal Bulan \t\tWaktu \t\t\tUang Muka")
    for i in range(len(dataKonsul)):
        print(str(i + 1), '\t', dataKonsul[i]["Nama Dokter"], '\t', dataKonsul[i]["Tanggal"], ' \t ',
              dataKonsul[i]["Bulan"], '\t', dataKonsul[i]["Waktu"], '\t', dataKonsul[i]["Uang Muka"])

    print("---------------------------------")
    input("Tekan 'ENTER' untuk Melanjutkan")


kecamatan = ""
ongkir = ""
def ongkoskirim():
    global kecamatan
    global ongkir

    print("----------------------------------------")
    print("-------------Alamat Pengiriman----------------")
    print("Daftar Kecamatan \n"
          "[1] Banjarsari\n"
          "[2] Jebres\n"
          "[3] Laweyan\n"
          "[4] Pasar Kliwon\n"
          "[5] Serengan\n")
    no_kecamatan = int(input("Masukkan Kecamatan : "))
    if no_kecamatan == 1:
        kecamatan = "Banjarsari"
        ongkir = "Rp 9.000"
    elif no_kecamatan == 2:
        kecamatan = "Jebres"
        ongkir = "Rp 5.000"
    elif no_kecamatan == 3:
        kecamatan = "Laweyan"
        ongkir = "Rp 10.000"
    elif no_kecamatan == 4:
        kecamatan = "Pasar Kliwon"
        ongkir = "Rp 7.000"
    elif no_kecamatan == 5:
        kecamatan = "Serengan"
        ongkir = "Rp 10.000"

    alamat = input("Masukkan Alamat Lengkap : \n")

ulang = True

if __name__ == "main":
    cek = cekFile()
    print('Ada file? ', str(cek))

while ulang:
    print("------------ Program Meds-On  ------------")
    menu()
    print("------------------------------------------")
    pilihan = int(input("Masukkan Pilihan Anda : "))
    if pilihan == 1:
        APD()
        print("-----------------------------------")
        input("Tekan 'ENTER' untuk Melanjutkan")
        kondisi = input("Ingin pesan lagi? (Y/T) : ")
        if kondisi == "y":
            ulang = True
        elif kondisi == "t" or kondisi == "T":
            lihatpesanan()
            ongkoskirim()
            ulang = False
    elif pilihan == 2:
        Vitamin()
        print("-----------------------------------")
        input("Tekan 'ENTER' untuk Melanjutkan")
        kondisi = input("Ingin Pesan Lagi? (Y/T) : ")
        if kondisi == "y":
            ulang = True
        elif kondisi == "t" or kondisi == "T":
            lihatpesanan()
            ongkoskirim()
            ulang = False
    elif pilihan == 3:
        Obat()
        print("-----------------------------------")
        input("Tekan 'ENTER' untuk Melanjutkan")
        kondisi = input("Ingin Pesan Lagi? (Y/T) : ")
        if kondisi == "y":
            ulang = True
        elif kondisi == "t" or kondisi == "T":
            lihatpesanan()
            ongkoskirim()
            ulang = False
    elif pilihan == 4:
        Dokter()
        print("-----------------------------------")
        input("Tekan 'ENTER' untuk Melanjutkan")
        Jadwal()
        kondisi = input("Ingin Pesan Lagi? (Y/T) : ")
        if kondisi == "y":
            lihatpesanan()
            ongkoskirim()
            ulang = True
        elif kondisi == "t" or kondisi == "T":
            lihatpesanan()
            ulang = False
