from texttable import Texttable
table = Texttable ()
jawab = "y"
no = 0
nama = []
nim = []
n_tugas = []
n_uts = []
n_uas = []
while (jawab == "y"):
    nama.append(input("Nama :"))
    nim.append(input("NIM :"))
    n_tugas.append(input("Nilai Tugas :"))
    n_uts.append(input("Nilai UTS :"))
    n_uas.append(input("Nilai UAS :"))
    jawab = input ("Tambah data (y/t)?")
    no +=1
for i in range(no):
    nt = int(n_tugas[i])
    nu = int(n_uts[i])
    na = int(n_uas[i])
    akhir = (nt*30/100) + (nu*35/100) + (na*35/100)
    table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],
                    [i+1,nama[i],nim[i],n_tugas[i],n_uts[i],n_uas[i],akhir]])
print (table.draw())
