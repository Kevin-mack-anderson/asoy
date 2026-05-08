import barcode
from barcode.writer import ImageWriter

# Pilih jenis barcode (misal: EAN-13, Code128, dll)
number = '123456789012'
barcode_format = barcode.get_barcode_class('ean13')

# Simpan sebagai file gambar (PNG)
my_barcode = barcode_format(number, writer=ImageWriter())
my_barcode.save('barcode_produk_saya')