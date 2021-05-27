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