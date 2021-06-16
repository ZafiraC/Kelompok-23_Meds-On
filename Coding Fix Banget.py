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
            print("Maaf perintah yang Anda masukkan salah!")
    else:
        print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
        APD()

    keys = dataAPD[0].keys()
    with open('data.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataAPD)

jenis2 = ""
def Vitamin():
    global total1
    global total2
    global total3
    global total4
    global jenis2
    global jml_vit
    global grand_total
    print("Daftar Vitamin".center(50, '-'))
    print("1. Imboost Effervescent With Vitamin C: Rp 30.000")
    print("2. Redoxon Double Action Isi 10       : Rp 35.000")
    print("3. CDR Fortos isi 10                  : Rp 40.000")
    print("4. Enervon C Tablet Isi 30            : Rp 45.000")
    nomor = int(input("Pilih yang mana? : "))
    jml_vit = int(input("Jumlah : "))
    print("-" * 50)

    if nomor == 1:
        total1 = jml_vit * 30000
        print(jml_vit, " Imboost Effervescent With Vitamin C : Rp", total1)
        jenis2 = ("Imboost Effervescent With Vitamin C")
        Vitamin = {"No": nomor, "Jenis": jenis2, "Jumlah": jml_vit, "Harga": total1}
        dataVitamin.append(Vitamin.copy())
        grand_total.append(total1)
    elif nomor == 2:
        total2 = jml_vit * 35000
        print(jml_vit, " Redoxon Double Action Isi 10 : Rp", total2)
        jenis2 = ("Redoxon Double Action Isi 10")
        Vitamin = {"No": nomor, "Jenis": jenis2, "Jumlah": jml_vit, "Harga": total2}
        dataVitamin.append(Vitamin.copy())
        grand_total.append(total2)
    elif nomor == 3:
        total3 = jml_vit * 40000
        print(jml_vit, " CDR Fortos isi 10 : Rp", total3)
        jenis2 = ("CDR Fortos isi 10")
        Vitamin = {"No": nomor, "Jenis": jenis2, "Jumlah": jml_vit, "Harga": total3}
        dataVitamin.append(Vitamin.copy())
        grand_total.append(total3)
    elif nomor == 4:
        total4 = jml_vit * 45000
        print(jml_vit, " Enervon C Tablet : Rp", total4)
        jenis2 = ("Enervon C Tablet")
        Vitamin = {"No": nomor, "Jenis": jenis2, "Jumlah": jml_vit, "Harga": total4}
        dataVitamin.append(Vitamin.copy())
        grand_total.append(total4)
    else:
        print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
        Vitamin()

    keys = dataVitamin[0].keys()
    with open('data.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataVitamin)

jenis3 = ""
def Obat():
    global total1
    global total2
    global total3
    global total4
    global jml_obat
    global jenis3
    global grand_total
    print("Daftar Obat Generik".center(50, '-'))
    print("1. Obat Penurun Panas")
    print("2. Obat Batuk")
    print("3. Obat Flu")
    print("4. Obat Pusing")
    nomor = int(input("Mau yang mana ? : "))
    print("-" * 50)

    if nomor == 1:
        print("[1] Paracetamol Tablet 500mg Isi 10       : Rp 3000")
        print("[2] Sanmol Paracetamol Tablet 500mg Isi 4 : Rp 1500")
        print("[3] Ibuprofen Tablet 400 mg Isi 10        : Rp 4000")
        print("[4] Termorex Paracetamol Sirup Anak       : Rp 16000")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))
        if obat == 1:
            total1 = jml_obat * 3000
            print(jml_obat, "Paracetamol Tablet 500mg Isi 10 : Rp", total1)
            jenis3 = ("Paracetamol Tablet 500mg Isi 10")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total1}
            dataObat.append(Obat.copy())
            grand_total.append(total1)
        elif obat == 2:
            total2 = jml_obat * 1500
            print(jml_obat, "Sanmol Paracetamol Tablet 500mg Isi 4 : Rp", total2)
            jenis3 = ("Sanmol Paracetamol Tablet 500mg Isi 4")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total2}
            dataObat.append(Obat.copy())
            grand_total.append(total2)
        elif obat == 3:
            total3 = jml_obat * 4000
            print(jml_obat, "Ibuprofen Tablet 400 mg Isi 10 : Rp", total3)
            jenis3 = ("Ibuprofen Tablet 400 mg Isi 10")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total3}
            dataObat.append(Obat.copy())
            grand_total.append(total3)
        elif obat == 4:
            total4 = jml_obat * 16000
            print(jml_obat, "Termorex Paracetamol Sirup Anak : Rp", total4)
            jenis3 = ("Termorex Paracetamol Sirup Anak")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total4}
            dataObat.append(Obat.copy())
            grand_total.append(total4)
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
            total1 = jml_obat * 16000
            print(jml_obat, "Siladex ME 60 ml : Rp", total1)
            jenis3 = ("Siladex ME 60 ml")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total1}
            dataObat.append(Obat.copy())
            grand_total.append(total1)
        elif obat == 2:
            total2 = jml_obat * 22000
            print(jml_obat, "Vicks Formula 44 : Rp", total2)
            jenis3 = ("Vicks Formula 44")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total2}
            dataObat.append(Obat.copy())
            grand_total.append(total2)
        elif obat == 3:
            total3 = jml_obat * 25000
            print(jml_obat, "Benadryl Original : Rp", total3)
            jenis3 = ("Benadryl Original")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total3}
            dataObat.append(Obat.copy())
            grand_total.append(total3)
        elif obat == 4:
            total4 = jml_obat * 33000
            print(jml_obat, "Woods Antitussive 100 ml : Rp", total4)
            jenis3 = ("Woods Antitussive 100 ml")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total4}
            dataObat.append(Obat.copy())
            grand_total.append(total4)

    elif nomor == 3:
        print("[1] Inza          : Rp 2000")
        print("[2] Mixagrip Flu  : Rp 3000")
        print("[3] Neozep Forte  : Rp 3000")
        print("[4] Decolgen Flu  : Rp 3000")

        obat = int(input("Pilih yang mana? : "))
        jml_obat = int(input("Jumlah : "))

        if obat == 1:
            total1 = jml_obat * 2000
            print(jml_obat, " Inza : Rp", total1)
            jenis3 = ("Inza")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total1}
            dataObat.append(Obat.copy())
            grand_total.append(total1)
        elif obat == 2:
            total2 = jml_obat * 3000
            print(jml_obat, " Mixagrip Flu : Rp", total2)
            jenis3 = ("Mixagrip Flu")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total2}
            dataObat.append(Obat.copy())
            grand_total.append(total2)
        elif obat == 3:
            total3 = jml_obat * 3000
            print(jml_obat, " Neozep Forte : Rp", total3)
            jenis3 = ("Neozep Forte")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total3}
            dataObat.append(Obat.copy())
            grand_total.append(total3)
        elif obat == 4:
            total4 = jml_obat * 3000
            print(jml_obat, " Decolgen Flu : Rp", total4)
            jenis3 = ("Decolgen Flu")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total4}
            dataObat.append(Obat.copy())
            grand_total.append(total4)
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
            total1 = jml_obat * 2500
            print(jml_obat, " Bodrex Migra  : Rp", total1)
            jenis3 = ("Bodrex Migra ")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total1}
            dataObat.append(Obat.copy())
            grand_total.append(total1)
        elif obat == 2:
            total2 = jml_obat * 3000
            print(jml_obat, " Konimex Paramex : Rp", total2)
            jenis3 = ("Konimex Paramex")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total2}
            dataObat.append(Obat.copy())
            grand_total.append(total2)
        elif obat == 3:
            total3 = jml_obat * 9000
            print(jml_obat, " Panadol Regular : Rp", total3)
            jenis3 = ("Panadol Regular")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total3}
            dataObat.append(Obat.copy())
            grand_total.append(total3)
        elif obat == 4:
            total4 = jml_obat * 9000
            print(jml_obat, " Panadol Extra : Rp", total4)
            jenis3 = ("Panadol Extra")
            Obat = {"No": nomor, "Jenis": jenis3, "Jumlah": jml_obat, "Harga": total4}
            dataObat.append(Obat.copy())
            grand_total.append(total4)
        else:
            print("Maaf perintah yang Anda masukkan salah!")
    else:
        print("Maaf permintaanmu saat ini tidak tersedia, silahkan pilih kembali !")
        Obat()

    keys = dataObat[0].keys()
    with open('data.csv', 'a', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dataObat)

nama=""
def Dokter():
    global nama
    print("Booking Konsultasi Dokter".center(50,'-'))
    print("1. Dokter Umum")
    print("2. Dokter Anak")
    print("3. Dokter Gigi")
    print("4. Dokter Kandungan")
    print("5. Dokter Kulit & Kelamin")
    print("6. Dokter THT")
    dokter = int(input("Pilih dokter yang bersangkutan: "))
    print("-" * 50)

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

    uangmuka = 0
    waktu = ""

    def Jadwal():
        global waktu
        global uangmuka

        print("Silakan pilih jadwal konsultasi!")
        tanggal = int(input("Tanggal : "))
        bulan = int(input("Bulan   : "))
        print("Pilihan waktu konsultasi\n"
              "[1] 10.00 - 12.00\n"
              "[2] 13.00 - 15.00\n"
              "[3] 19.00 - 21.00\n")
        jam = int(input("Waktu   : "))
        if jam == 1:
            waktu = "10.00 - 12.00"
        elif jam == 2:
            waktu = "13.00 - 15.00"
        elif jam == 3:
            waktu = "19.00 - 21.00"
        uangmuka = 50000

        Konsul = {"Nama Dokter": nama, "Tanggal": tanggal, "Bulan": bulan, "Waktu": waktu, "Uang Muka": "Rp 50.000"}
        dataKonsul.append(Konsul.copy())

        keys = dataKonsul[0].keys()
        with open('konsultasi.csv', 'a', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dataKonsul)

    def lihatpesanan():
        print("Pembelian".center(80, '='))
        print("Jumlah \tNama Pesanan \tHarga")
        for i in range(len(dataAPD)):
            print(" APD ".center(80, '*'))
            print(dataAPD[i]["Jumlah"], '\t', dataAPD[i]["Jenis"], '\n', '\t' * 6, 'Rp', dataAPD[i]["Harga"])
        for i in range(len(dataVitamin)):
            print(" Vitamin ".center(80, '*'))
            print(dataVitamin[i]["Jumlah"], '\t', dataVitamin[i]["Jenis"], '\n', '\t' * 6, 'Rp',
                  dataVitamin[i]["Harga"])
        for i in range(len(dataObat)):
            print(" Obat Generik ".center(80, '*'))
            print(dataObat[i]["Jumlah"], '\t', dataObat[i]["Jenis"], '\n', '\t' * 6, 'Rp', dataObat[i]["Harga"])

        print("Konsultasi Dokter".center(80, '='))
        print("Nomor \tNama Dokter \t\t\tTanggal Bulan \t\tWaktu \t\t\tUang Muka")
        for i in range(len(dataKonsul)):
            print(str(i + 1), '\t', dataKonsul[i]["Nama Dokter"], '\t', dataKonsul[i]["Tanggal"], ' \t ',
                  dataKonsul[i]["Bulan"], '\t', dataKonsul[i]["Waktu"], '\t', dataKonsul[i]["Uang Muka"])

        print("-" * 80)

    totalsemua = 0

    def pembayaran():
        print('-' * 50)
        if jmlapd > 0 or jml_obat > 0 or jml_vit > 0:
            ongkoskirim()
            pembayaran_semua()
        else:
            pembayaran_konsul()

    def pembayaran_semua():
        global alamat
        global totalsemua
        totalsemua = sum(grand_total) + ongkos + uangmuka
        print("Daftar Pesanan".center(50, '='))
        for i in range(len(dataAPD)):
            print(dataAPD[i]["Jumlah"], '\t', dataAPD[i]["Jenis"], '\n', '\t' * 6, '  Rp', dataAPD[i]["Harga"])
        for i in range(len(dataVitamin)):
            print(dataVitamin[i]["Jumlah"], '\t', dataVitamin[i]["Jenis"], '\n', '\t' * 6, '  Rp',
                  dataVitamin[i]["Harga"])
        for i in range(len(dataObat)):
            print(dataObat[i]["Jumlah"], '\t', dataObat[i]["Jenis"], '\n', '\t' * 6, '  Rp', dataObat[i]["Harga"])
        for i in range(len(dataKonsul)):
            print(dataKonsul[i]["Nama Dokter"], '\t', dataKonsul[i]["Tanggal"], ' \t ',
                  dataKonsul[i]["Bulan"], '\t', dataKonsul[i]["Waktu"], '\t', dataKonsul[i]["Uang Muka"])
        print("\nOngkos Kirim             : Rp", ongkos)
        print("Total yang harus Dibayar : Rp", totalsemua)
        print("Alamat pengiriman        :", alamat[0])
        print('-' * 50)
        benar = input("Apakah total sudah benar? (Y/T) : ")
        print('-' * 50)
        if benar == 'y' or benar == 'Y':
            print("Pilih metode pembayaran!\n"
                  "[1] Transfer\n"
                  "[2] COD")
            metode = int(input("Masukkan pilihan Anda : "))
            if metode == 1 and totalsemua >= 10000:
                nota_trf()
            elif metode == 1 and totalsemua < 10000:
                print("Maaf, minimal transaksi tidak mencukupi!")
                beli = input("Apakah ingin menambah pembelian? (Y/T) : ")
                if beli == 'y':
                    utama()
                elif beli == 't':
                    print("Mohon ganti metode pembayaran!")
                    pembayaran()
            elif metode == 2:
                nota_cod()
        else:
            welcome()
            return False

    def pembayaran_konsul():
        global totalsemua
        totalsemua = uangmuka
        print('-' * 50)
        print("Total yang harus Dibayar : Rp", totalsemua)
        print('-' * 50)
        print("Pilih metode pembayaran!\n"
              "[1] Transfer\n"
              "[2] COD")
        metode = int(input("Masukkan pilihan Anda : "))
        if metode == 1 and totalsemua >= 10000:
            nota_trf()
        elif metode == 1 and totalsemua < 10000:
            print("Maaf, minimal transaksi tidak mencukupi!")
            beli = input("Apakah ingin menambah pembelian? (Y/T) : ")
            if beli == 'y' or beli == 'Y':
                utama()
            elif beli == 't' or beli == 'T':
                print("Mohon ganti metode pembayaran!")
                pembayaran()
        elif metode == 2:
            nota_cod()

    def nota_trf():
        global totalsemua
        print("\n")
        print("-" * 80)
        print("NOTA PEMBAYARAN".center(80, '-'))
        lihatpesanan()
        print(" Total Tagihan Anda   : Rp", totalsemua)
        print(" Silakan transfer ke rekening berikut!\n"
              " BCA : 015883291\n"
              " a.n. Meds-On")
        print("Transaksi Selesai".center(80, '-'))
        print("TERIMA KASIH".center(80, '-'))

    def nota_cod():
        global totalsemua
        print("\n")
        print("-" * 80)
        print("NOTA PEMBAYARAN".center(80, '-'))
        lihatpesanan()