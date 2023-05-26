while True:
    a = input("Masukan password: ")
    if len(a) < 8:
        print("Kata sandi minimal 8 karakter")
    elif len(a) > 32:
        print("Kata sandi maksimal 32 karakter")
    elif a[0].isdigit():
        print("Karakter awal tidak boleh angka")
    elif not any (i.isdigit() for i in a):
        print("Harus memiliki angka")
    elif not any (i.islower() for i in a):
        print("Harus memiliki huruf kapital dan huruf kecil")
    elif not any (i.isupper() for i in a):
        print("Harus memiliki huruf kapital dan huruf kecil")
    else:
        print("Kata sandi valid")
        break