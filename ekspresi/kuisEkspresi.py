dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
if dico >500000:
  diskon = 0.10
  potongan = dico * diskon
else:
  potongan = 0
  
total_harga = dico - potongan
print(f"Total harga belanjaan dico setelah diskon adalah Rp{total_harga:,.0f}")