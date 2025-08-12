**Transportation Rental Management System (TRMS)**

Projek ini adalah mini aplikasi Sistem Informasi Rental Kendaraan yang dibuat menggunakan basic Python function.
Projek ini bertujuan supaya kita bisa latihan CRUD (Create, Read, Update, Delete) + tambahan fitur Rent & Return seperti sistem rental pada umumnya.

**Bayangkan anda punya usaha rental mobil/motor/bus, kamu butuh sistem yang bisa:**

1. Lihat daftar kendaraan yang ada (View)

2. Tambah kendaraan baru ke sistem (Add)

3. Edit/update data kendaraan (Update)

4. Hapus kendaraan (Delete)

5. Sewakan kendaraan ke pelanggan (Rent)

6. Terima pengembalian kendaraan (Return)

**File example.py berisikan:**

1. Data awal (dataRental) → 5 kendaraan dengan detail:

2. Vehicle ID (unik)

3. Type (Car/Motorbike/Bicycle/Van/Bus)

5. Brand (merek)

6. License Plate (plat nomor)

7. Rental Price Per Day (harga sewa/hari)

8. Availability (Available / Rented)

9. Last Service Date (tanggal service terakhir)

10. Odometer (kilometer)

**Menu utama (mainMenu) → pilihan keinginan user**

Fungsi-fungsi CRUD:

1. viewVehicles() → Lihat semua kendaraan, cari by ID, filter available/type

2. addVehicle() → Tambah kendaraan baru dengan validasi unik & input wajib

3. updateVehicle() → Edit data kendaraan via submenu

4. deleteVehicle() → Hapus kendaraan (nggak boleh kalau lagi disewa)

Fungsi tambahan:

1. rentVehicle() → Catat penyewaan, ubah status ke Rented, simpan ke rentalHistory

2. returnVehicle() → Catat pengembalian, hitung total harga, update status kembali Available

**Penampilan & Cara Pakai**

1. Jalankan program: python example.py

2. Akan muncul Main Menu: View Vehicles (1), Add New Vehicle (2), Update Vehicle Information (3), Delete Vehicle (4), Rent a Vehicle (5), Return a Vehicle (6), Exit (7)

3. Ketik angka sesuai menu yang mau dipakai → Tekan Enter

4. Ikuti petunjuk input di setiap menu (contoh: masukin Vehicle ID, tanggal, jumlah hari sewa, dll).

5. Program akan loop balik ke Main Menu sampai pilih Exit (7)

**Notes:**
1. Vehicle ID harus unik, sama juga untuk License Plate (kecuali kendaraan tanpa plat, pakai -).

2. Kendaraan yang sedang disewa nggak bisa dihapus.
