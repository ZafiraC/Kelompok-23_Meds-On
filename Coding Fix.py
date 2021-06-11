import csv
import os.path
from os import path

total1 = 0
total2 = 0
total3 = 0
total4 = 0

jenis1 = ""
jmlapd = 0
jml_vit = 0
jml_obat = 0

dataAPD = []
dataVitamin = []
dataObat = []
dataKonsul = []

grand_total = []

def menu():
    print("Menu Utama".center(50,'-'))
    print("[1] APD")
    print("[2] Vitamin")
    print("[3] Obat Generik")
    print("[4] Konsultasi Dokter")

def APD():
    global total1
    global total2
    global total3
    global total4
    global jmlapd
    global jenis1
    global grand_total
    print ("Daftar APD".center(50,'-'))
    print("1. Masker")
    print("2. Face Shield")
    print("3. Hand Sanitizer")
    nomor=int(input("Mau yang mana ? : "))
    print("-" * 50)

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
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total1}
            dataAPD.append(APD.copy())
            grand_total.append(total1)
        elif masker==2:
            total2 = jmlapd*140000
            print(jmlapd, " box Sensi Duckbill : Rp", total2)
            jenis1 = ("Sensi Duckbill")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total2}
            dataAPD.append(APD.copy())
            grand_total.append(total2)
        elif masker==3:
            total3 = jmlapd*137500
            print(jmlapd, " box Sensi Headloop : Rp", total3)
            jenis1 = ("Sensi Headloop")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total3}
            dataAPD.append(APD.copy())
            grand_total.append(total3)
        elif masker==4:
            total4 = jmlapd*115000
            print(jmlapd, " box Sensi Earloop : Rp", total4)
            jenis1 = ("Sensi Earloop")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total4}
            dataAPD.append(APD.copy())
            grand_total.append(total4)
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
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total1}
            dataAPD.append(APD.copy())
            grand_total.append(total1)
        elif face==2:
            total2 = jmlapd*20000
            print(jmlapd, " Face Shield Anti Embun : Rp", total2)
            jenis1 = ("Face Shield Akrilik")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total2}
            dataAPD.append(APD.copy())
            grand_total.append(total2)
        elif face==3:
            total3 = jmlapd*12000
            print(jmlapd, " Face Shield Anti Embun : Rp", total3)
            jenis1 = ("Face Shield Anak-anak")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total3}
            dataAPD.append(APD.copy())
            grand_total.append(total3)
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
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total1}
            dataAPD.append(APD.copy())
            grand_total.append(total1)
        elif hand==2:
            total2 = jmlapd*7000
            print(jmlapd, " Antis Gel : Rp", total2)
            jenis1 = ("Antis Gel")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total2}
            dataAPD.append(APD.copy())
            grand_total.append(total2)
        elif hand==3:
            total3 = jmlapd*7500
            print(jmlapd, " Nuvo Gel : Rp", total3)
            jenis1 = ("Nuvo Gel")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total3}
            dataAPD.append(APD.copy())
            grand_total.append(total3)
        elif hand==4:
            total4 = jmlapd*7500
            print(jmlapd, " Dettol Spray : Rp", total4)
            jenis1 = ("Dettol Spray")
            APD = {"No": nomor, "Jenis": jenis1, "Jumlah": jmlapd, "Harga": total4}
            dataAPD.append(APD.copy())
            grand_total.append(total4)
        else:
