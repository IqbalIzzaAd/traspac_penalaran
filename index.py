# Artikel (disederhanakan untuk contoh)
artikel = """
Dalam kehidupan suatu negara, pendidikan memegang peranan yang amat penting untuk menjamin kelangsungan hidup negara dan bangsa, karena pendidikan merupakan wahana untuk meningkatkan dan mengembangkan kualitas sumber daya manusia. Seiring dengan perkembangan teknologi komputer dan teknologi informasi, sekolah-sekolah di Indonesia sudah waktunya mengembangkan Sistem Informasi manajemennya agar mampu mengikuti perubahan jaman. 
SISKO mampu memberikan kemudahan pihak pengelola menjalankan kegiatannya dan meningkatkan kredibilitas dan akuntabilitas sekolah dimata siswa, orang tua siswa, dan masyakat umumnya.Penerapan teknologi informasi untuk menunjang proses pendidikan telah menjadi kebutuhan bagi lembaga pendidikan di Indonesia. Pemanfaatan teknologi informasi ini sangat dibutuhkan untuk meningkatkan efisiensi dan produktivitas bagi manajemen pendidikan. Keberhasilan dalam peningkatan efisiensi dan produktivitas bagi manajemen pendidikan akan ikut menentukan kelangsungan hidup lembaga pendidikan itu sendiri. Dengan kata lain menunda penerapan teknologi informasi dalam lembaga pendidikan berarti menunda kelancaran pendidikan dalam menghadapi persaingan global. 
Pemanfaatan teknologi informasi diperuntukkan bagi peningkatan kinerja lembaga pendidikan dalam upayanya meningkatkan kualitas Sumber Daya Manusia Indonesia. Guru dan pengurus sekolah tidak lagi disibukkan oleh pekerjaan-pekerjaan operasional, yang sesungguhnya dapat digantikan oleh komputer. Dengan demikian dapat memberikan keuntungan dalam efisien waktu dan tenaga. 
Penghematan waktu dan kecepatan penyajian informasi akibat penerapan teknologi informasi tersebut akan memberikan kesempatan kepada guru dan pengurus sekolah untuk meningkatkan kualitas komunikasi dan pembinaan kepada siswa. Dengan demikian siswa akan merasa lebih dimanusiakan dalam upaya mengembangkan kepribadian dan pengetahuannya. 
Sebagai contoh yang paling utama adalah sistem penjadwalan yang harus dilakukan setiap awal semester. Biasanya membutuhkan waktu lama untuk menyusunpenjadwalan, Dengan SISKO dapat selesai dalam waktu singkat. Untuk mempermudah bagian administrasi kurikulum sekolah, SISKO menyediakan fasilitas istimewa yang merupakan inti dari sistem kurikulum sekolah yaitu membantu dalam pembuatan penjadwalan mata pelajaran sekolah yang dapat diproses tidak lebih lama dari 10 menit. Administrator hanya akan memasukkan kondisi dari masing-masing guru yang akan mengajar baik itu dalam 1 minggu seorang guru dapat mengajar berapa jam, selain itu dapat juga melakukan pemesanan tempat dan penempatan hari libur masing-masing guru dalam 1 minggu masa mengajar. Setelah semua kondisi dimasukkan, sistem akan memproses semua data tersebut sehingga menghasilkan jadwal yang optimal dan dapat langsung dipakai karena sistem akan mendeteksi sehingga tidak akan ada jadwal yang bertumpukan satu dengan yang lainnya. 
Setelah semua kondisi dimasukkan, sistem akan memproses semua data tersebut sehingga menghasilkan jadwal yang optimal dan dapat langsung dipakai karena sistem akan mendeteksi sehingga tidak akan ada jadwal yang bertumpukan satu dengan yang lainnya. Setelah permasalahan penjadwalan dapat ditangani dengan baik, hal yang tidak kalah pentingnya adalah memasukkan data siswa. 
Program SISKO telah menyediakan fasilitas untuk penanganan penilaian siswa yang secara langsung memasukkan nilai ke dalam raport dan siap dicetak. Untuk sistem penilaian siswa, yang dapat melakukan pengisian hanya Guru yang mengajar mata pelajaran. Sistem penilaian telah disesuaikan dengan KBK sehingga masing masing guru dapat memasukkan deskripsi narasi dari mata pelajaran. Untuk menampilkan data penilaian dapat disesuaikan kembali dengan kebijaksanaan dari masing-masing lembaga pendidikan apakah ingin menampilkan data nilai akhir siswa maupun menampilkan data nilai siswa setiap kali mengadakan test ataupun tugas tertentu. 
Selain Modul untuk penjadwalan dan Modul Penilaian siswa, SISKO juga memberikan fasilitas untuk bagian administrasi keuangan sekolah dalam hal pembayaran SPP siswa. Bagian administrasi dapat langsung mengecek siapa siswa yang mempunyai tunggakan SPP dan untuk detail histori pembayaran SPP dari masing-masing siswa dapat dicetak seperti mencetak buku tabungan di bank sehingga mempermudah pekerjaan pihak administrasi keuangan. Administrasi keuangan dapat langsung melakukan pengaturan data pembayaran masing-masing siswa sesuai dengan kebutuhan dan dapat diubah sewaktu-waktu apabila ada kenaikan pembayaranSPP. Apabila siswa tersebut akan melakukan pembayaran, petugas dapat langsung memasukkan data. Hal sama juga dapat dilakukan untuk Data pembayaran Sumbangan Sukarela dan Tabungan Karyawisata.
"""

# 1. PENCARIAN KATA
def cari_kata(artikel, kata):
    kata_kecil = kata.lower()
    artikel_kecil = artikel.lower()
    jumlah = artikel_kecil.split().count(kata_kecil)
    return jumlah

# 2. PENGGANTIAN KATA (REPLACE)
def ganti_kata(artikel, kata_lama, kata_baru):
    return artikel.replace(kata_lama, kata_baru)

# 3. PENGURUTAN KATA BERDASARKAN ABJAD
def urutkan_kata(artikel):
    kata_list = artikel.lower().split()
    kata_unik = sorted(set(kata_list))
    return kata_unik



# --- TEST PROGRAM ---
kata_dicari = "teknologi"
print(f"Kata '{kata_dicari}' ditemukan {cari_kata(artikel, kata_dicari)} kali.\n")

artikel_baru = ganti_kata(artikel, "adalah", "ialah")
print("Artikel setelah penggantian kata:\n", artikel_baru, "\n")

print("Kata-kata yang telah diurutkan:\n", urutkan_kata(artikel))
