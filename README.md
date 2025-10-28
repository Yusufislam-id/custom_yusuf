## Test Technical Odoo

### Requirement 1:
- ✅ Tambahkan 1 Field Request Vendor (res.partner) posisi seperti yg ditunjukkan kotak merah no 1
- ✅ Tambahkan 1 Field No Kontrak (Char) posisi seperti yg ditunjukkan kotak merah no 2
- ✅ Tambahkan 1 Field With PO (Boolean) posisi seperti yang ditunjukkan kotak merah no 3
- ✅ Tambahkan Tab/Notebook Baru “Purchase Orders” setelah Tab Order Lines seperti yang ditunjukkan kotak merah no 4
- ✅ Tambahkan 1 Field PO (One2many) dan tempatkan field tersebut di dalam Tab “Purchase Orders” yang baru dibuat tadi.

### Requirement 2:
- ✅ Tambahkan 1 Button Create PO posisi seperti yg ditunjukkan kotak merah no 5
  - [ ] Ketika Button Create PO di klik maka Otomatis akan membuat PO dengan isian:
    - ✅ Nama Vendor di PO ambil dari field Request Vendor yang sudah ditambahkan di SO (requirement 1)
    - ✅ Vendor Reference di PO ambil dari field No SO
    - [ ] Po Line ambil dari So Line/Order Line
- ✅ Tambahkan attribute pada Button Create PO dengan kondisi sebagai berikut:
  - Ketika field With PO bernilai True, button Create PO muncul
  - Ketika field With PO bernilai False Button Create PO akan invisible.
- [ ] Modifikasi Tombol Confirm di SO untuk validasi No Kontrak (requirement 1) seperti yg ditunjukkan kotak merah no 6
  - [ ] Ketika klik Tombol Confirm SO diklik maka akan cek field No Kontrak yg ada SO dengan kondisi apakah No Kontrak sudah pernah diinputkan sebelumnya
  - [ ] jika sudah pernah diinputkan sebelumnya maka akan ada validasi/ pesan “No Kontrak sudah pernah diinputkan sebelumnya…!”
  - [ ] jika belum pernah diinputkan maka proses confirm akan berlanjut

### Requirement 3:
- [ ] Tambahkan 1 Button Import SO Lines posisi seperti yg ditunjukkan kotak merah no 7
  - [ ] Ketika Button Import SO Lines di-klik, akan muncul pop up wizard untuk import SO Lines dari file excel.
  - [ ] Template File Excel:
  - [ ] Ketika Button Import di-klik, SO Lines akan langsung bertambah sesuai dengan file excel yang diupload. Informasi SO Line yang di-import dari file excel adalah product, quantity dan unit price. Sistem akan otomatis mencari product sesuai dengan kode product yang dibaca dari file excel.
  - [ ] Button Download Template (tidak wajib dikerjakan)
    - [ ] Ketika Button Download Template di-klik akan langsung otomatis download file excel berisi template yang sudah siap digunakan untuk import SO Lines.