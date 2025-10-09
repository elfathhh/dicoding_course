import argparse
from datetime import datetime

# Fungsi untuk menghitung usia dari tanggal lahir
def hitung_usia(tanggal_lahir_str):
    try:
        tanggal_lahir = datetime.strptime(tanggal_lahir_str, "%d-%m-%Y")
    except ValueError:
        print("Format tanggal salah! Gunakan format dd-mm-yyyy.")
        exit(1)
    
    hari_ini = datetime.today()
    usia = hari_ini.year - tanggal_lahir.year - ((hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day))
    return usia

# Setup argparser
parser = argparse.ArgumentParser(description="Panggil Dicoding")

parser.add_argument('-n', '--nama', type=str, required=True, help='Nama pemanggil')
parser.add_argument('-t', '--tanggallahir', type=str, required=True, help='Tanggal lahir (format: dd-mm-yyyy)')

args = parser.parse_args()

# Hitung usia
usia = hitung_usia(args.tanggallahir)

# Tentukan panggilan
if usia < 30:
    panggilan = "kakak"
else:
    panggilan = "bapak"

# Tampilkan hasil
print(f"Halo {panggilan} {args.nama.upper()}")
