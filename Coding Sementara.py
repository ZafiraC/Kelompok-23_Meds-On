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

      Vitamin = {"No": nomor, "Jenis": jenis2, "Jumlah Vitamin": jml_vit, "Harga": total2}
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
