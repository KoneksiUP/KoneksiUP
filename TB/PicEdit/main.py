from PIL import Image, ImageFilter

# Fungsi untuk memuat gambar dan menampilkan informasi dasar
def load_image(filename):
    image = Image.open(filename)
    print("Gambar:", filename)
    print("Format:", image.format)
    print("Ukuran:", image.size)
    print("Mode:", image.mode)
    return image

# Fungsi untuk memperbaiki kecerahan gambar
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    adjusted_image = enhancer.enhance(factor)
    return adjusted_image

# Fungsi untuk menerapkan efek blur pada gambar
def apply_blur(image, radius):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    return blurred_image

# Fungsi untuk menyimpan gambar hasil pemrosesan
def save_image(image, filename):
    image.save(filename)
    print("Gambar hasil disimpan sebagai:", filename)

# Contoh penggunaan
input_image = load_image("input.jpg")
# brightened_image = adjust_brightness(input_image, 1.5)
blurred_image = apply_blur(input_image, 2)
# save_image(brightened_image, "brightened_output.jpg")
save_image(blurred_image, "blurred_output.jpg")
