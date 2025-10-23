nama = input("Nama Karyawan : ")
gol = input("Golongan Jabatan : [1/2/3] ")
pen = input("Pendidikan : [SMA/D1/D3/S1] ")
jam = int(input("Jumlah Jam Kerja : "))
gaji = 300000

if gol == "3":
    hasilJ = (15 / 100) * gaji          #45000
    if pen == "s1" or pen == "S1":
        hasilP = (30 / 100) * gaji      #90000
    elif pen == "D3" or pen == "d3":
        hasilP = (20 / 100) * gaji      #60000
    elif pen == "D1" or pen == "d1":
        hasilP = (5 / 100) * gaji       #15000
    elif pen == "SMA" or pen == "sma":
        hasilP = (2.5 / 100) * gaji     #7500
    else :
        hasilP = 0
elif gol == "2":
    hasilJ = (10 / 100) * gaji          #30000
    if pen == "s1" or pen == "S1":  
        hasilP = (30 / 100) * gaji
    elif pen == "D3" or pen == "d3":
        hasilP = (20 / 100) * gaji
    elif pen == "D1" or pen == "d1":
        hasilP = (5 / 100) * gaji
    elif pen == "SMA" or pen == "sma":
        hasilP = (2.5 / 100) * gaji
    else :
        hasilP = 0
elif gol == "1":
    hasilJ = (5 / 100) * gaji           #15000
    if pen == "s1" or pen == "S1":
        hasilP = (30 / 100) * gaji
    elif pen == "D3" or pen == "d3":
        hasilP = (20 / 100) * gaji
    elif pen == "D1" or pen == "d1":
        hasilP = (5 / 100) * gaji
    elif pen == "SMA" or pen == "sma":
        hasilP = (2.5 / 100) * gaji
    else :
        hasilP = 0
else :
    hasilJ = 0
    hasilP = 0
    
Lembur = (jam - 8) * 3500 if jam > 8 else 0

print("Karyawan Bernama : ", nama)
print("Honor yang di terima : ")
print("Gaji Pokok : ", gaji)
print("Tunjangan Jabatan : ",+int (hasilJ))
print("Tunjangan Pendidikan : ",+int (hasilP))
print("Honor Lembur : ",+int (Lembur))
print("Total Gaji : ",+int(gaji + hasilJ + hasilP +Lembur))