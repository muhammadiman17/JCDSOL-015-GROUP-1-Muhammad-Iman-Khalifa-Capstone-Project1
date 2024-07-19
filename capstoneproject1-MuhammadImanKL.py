# Capstone Project Purwadhika Data Science - Aplikasi untuk Admin Perpustakaan Purwadhika (Muhammad Iman Khalifa Latuconsina)
# ----------------------------------------------------------------------------------

#variable global yang dapat diakses oleh semua fungsi
data_buku = [
    {"ID": "001250", 
     "Title": "Belajar Coding", 
     "Author": "Bunyamin", 
     "Year": "2020", 
     "Status": "Ada"},
    {"ID": "001251", 
     "Title": "Coding 101", 
     "Author": "Januar", 
     "Year": "2021", 
     "Status": "Dipinjam"},
    {"ID": "001252", 
     "Title": "Data Analysis Terbaru", 
     "Author": "Rizaldy", 
     "Year": "2019", 
     "Status": "Ada"},
]

# callback function -> Fungsi kembali ke fungsi asal
# Akan digunakan di banyak argumen
def kembali(fungsi_asal):
    input("\nMasukkan apapun untuk kembali: ")
    fungsi_asal()

# ----------------------------------------------------------------------------------
# 1. Fitur create 
# fitur ini memungkinkan pengguna untuk memasukkan detail buku seperti ID buku, judul, penulis, tahun terbit, dan status buku.

def daftar_buku():
    print('''   
    Halaman Pendaftaran Buku
    ------------------------------------------
          
    1. Input Buku
    2. Kembali ke Beranda
    0. Keluar Program
    ''') #tampilan menu untuk menampilkan opsi untuk pengguna

    input_option = input('\nMasukkan tujuan Anda (0-2): ') # local function yang mengambil input dari pengguna untuk menentukan tujuan

    while True:
        if input_option == "1":
            while True:
                print('\nMasukkan ID buku. Masukkan 0 untuk membatalkan.')
                book_id = input('\nMasukkan ID: ')
                if not book_id.isnumeric():  # If condition untuk memeriksa apakah ID buku numerik
                    print('''
        ID buku harus numerik!
                    ''')
                    continue # Melanjutkan loop jika ID bukan numerik
                elif book_id == '0':
                    daftar_buku() #recursive function

                id_terdaftar = False
                for book in data_buku:
                    if book['ID'] == book_id:
                        print('''
        ID Buku sudah terdaftar! Silahkan Coba Lagi!
                        ''')
                        id_terdaftar = True
                        break # Keluar dari loop jika ID buku sudah terdaftar

                if id_terdaftar: # If condition untuk melanjutkan loop jika ID buku sudah terdaftar
                    continue
                
                # Jika ID buku tidak terdaftar, minta input lainnya
                print('\nMasukkan judul buku. Masukkan 0 untuk membatalkan.')
                title = input("\nMasukkan judul buku: ").capitalize()
                    
                while True:
                    print('\nMasukkan nama Penulis. Masukkan 0 untuk membatalkan.')
                    author = input("\nMasukkan nama Penulis: ").capitalize()
                    if author == '0':
                        daftar_buku()
                        return
                    if not all(c.isalpha() or c.isspace() for c in author): # If condition untuk memeriksa apakah nama penulis hanya terdiri dari huruf dan spasi
                        print('''
        Nama Penulis harus alfabet! Silahkan coba lagi!
                        ''')
                    elif len(author) < 2: # If condition untuk memeriksa apakah nama penulis terlalu pendek
                        print('''
        Huruf terlalu sedikit! Silahkan coba lagi!
                        ''')
                    else:
                        break
                while True:   
                    print('\nMasukkan tahun terbit buku. Masukkan 0 untuk membatalkan.') 
                    year = input("\nMasukkan tahun terbit: ")
                    if not year.isnumeric(): # If condition untuk memeriksa apakah tahun terbit numerik
                        print('''
        Tahun harus numerik!
                        ''')
                    elif year == '0':
                        daftar_buku()
                    else:
                        break
                while True:
                    print('\nMasukkan status buku. [Ada(1)/Dipinjam(2)]') 
                    status = input("\nMasukkan status: ")
                    if status not in ['1', '2']:
                        print('''
        Data yang dimasukkan salah! Silahkan coba lagi!
                        ''')
                    elif status == "1":
                        status = 'Ada'
                        break
                    elif status == "2":
                        status = 'Dipinjam'
                        break
                    else:
                        break

                data_buku.append({
                    "ID": book_id,
                    "Title": title,
                    "Author": author,
                    "Year": year,
                    "Status": status
                })
                print('''
        Buku berhasil ditambahkan!
                ''') # Ketika semua kondisi sudah terpenuhi, pesan ini akan muncul dan program akan keluar dari loop
                break
            daftar_buku() #recursive function
        elif input_option == "2":
            beranda()
        elif input_option == "0":
            keluar_program()
        else:
            print('''
        Input yang anda masukkan tidak tersedia! Silahkan coba lagi!
            ''')
            daftar_buku()
                





# ----------------------------------------------------------------------------------
# 2. Fitur Read
# fitur ini digunakan untuk mencari dan menampilkan informasi buku yang ada dalam daftar buku perpustakaan.

def cari_buku() :
    print('''
    Halaman Pencarian Buku
    ------------------------------------------
    
    1. Cari berdasarkan ID.
    2. Cari berdasarkan judul.
    3. Cari berdasarkan penulis.
    4. Cari berdasarkan tahun terbit.
    5. Kembali
    0. Keluar Program

    ''')
    
    input_option = input('\nMasukkan tujuan Anda (0-5): ')

    while True:
        if input_option == '1':
            book_id = input('\nMasukkan ID buku: ')
            found_books = [book for book in data_buku if book['ID'] == book_id]
            if found_books:
                for book in found_books:
                    print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                    kembali(cari_buku)
                    
            else:
                print('\nBuku tidak ditemukan.')
                kembali(cari_buku)

        elif input_option == '2':
            title = input('\nMasukkan judul buku: ').capitalize()
            found_books = [book for book in data_buku if book['Title'].lower() == title.lower()]
            if found_books:
                for book in found_books:
                    print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                    kembali(cari_buku)
            else:
                print('\nBuku tidak ditemukan.')
                kembali(cari_buku)

        elif input_option == '3':
            author = input('\nMasukkan nama penulis: ').capitalize()
            found_books = [book for book in data_buku if book['Author'].lower() == author.lower()]
            if found_books:
                for book in found_books:
                    print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                    kembali(cari_buku)
            else:
                print('\nBuku tidak ditemukan.')
                kembali(cari_buku)

        elif input_option == '4':
            year = input('\nMasukkan tahun terbit: ')
            found_books = [book for book in data_buku if book['Year'] == year]
            if found_books:
                for book in found_books:
                    print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                kembali(cari_buku)
            else:
                print('\nBuku tidak ditemukan.')
                kembali(cari_buku)

        elif input_option == '5':
            beranda()
            return
        elif input_option == '0':
            keluar_program()

        else:
            print('Input yang anda masukkan tidak tersedia! Silahkan coba lagi.')
            cari_buku()
        
        input_option = input('\nMasukkan tujuan Anda (1-5): ')


# ----------------------------------------------------------------------------------
# 3. Fitur Update
# fitur ini memungkinkan pengguna untuk melihat semua buku yang ada, mengubah informasi buku seperti judul, penulis, dan tahun terbit, serta mengubah status buku (misalnya, dari "Ada" menjadi "Dipinjam" atau sebaliknya).
def update_buku() :
    print('''
    
    Halaman Pembaruan Informasi Buku
    ------------------------------------------
    
    1. Tampilkan semua buku.
    2. Ubah informasi buku.
    3. Ubah status buku.
    4. Kembali
    0. Keluar Program
    
    ''')

    input_option = input('\nMasukkan tujuan Anda (0-4): ')
    
    if input_option == "0":
        keluar_program()
    elif input_option == "1":
        print("\nData Buku:")
        for book in data_buku:
            print(f"ID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
        kembali(update_buku)
    elif input_option == "2":
        book_id = input('Masukkan ID buku yang ingin diperbarui: ')
        for book in data_buku:
            if book['ID'] == book_id:
                print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                print('''
Pilih informasi yang ingin dirubah
                      
1. Judul
2. Penulis
3. Tahun terbit
4. Kembali

                ''')
                
                input_option = input('Masukkan tujuan Anda (1-4): ')
                while True:
                    if input_option == '1':
                        book['Title'] = input("Masukkan judul baru: ").capitalize()
                        
                        print("\nData buku telah diperbarui.")
                        kembali(update_buku)
                    elif input_option == '2':
                        book['Author'] = input("Masukkan penulis baru: ").capitalize()
                        print("\nData buku telah diperbarui.")
                        kembali(update_buku)
                    elif input_option == '3':
                        book['Year'] = input("Masukkan tahun terbit baru: ")
                        print("\nData buku telah diperbarui.")
                        kembali(update_buku)
                    elif input_option == '4':
                        update_buku()
                    else:
                        print('\nInput yang Anda masukkan salah! Silahkan coba lagi!')
                        kembali(update_buku)
        else:
            print("\nID buku tidak ditemukan.")
        kembali(update_buku)
    elif input_option == "3":
        book_id = input('Masukkan ID buku yang ingin diubah statusnya: ')
        for book in data_buku:
            if book['ID'] == book_id:
                print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                status_option = input("Masukkan status baru [Ada(1)/Dipinjam(2)]: ")
                if status_option == "1":
                    book['Status'] = 'Ada'
                    print("\nStatus buku telah diperbarui.")
                    kembali(update_buku)
                elif status_option == "2":
                    book['Status'] = 'Dipinjam'
                    print("\nStatus buku telah diperbarui.")
                    kembali(update_buku)
                else :
                    print('Input yang Anda masukkan salah! Silahkan coba lagi!')
                kembali(update_buku)
                
        else:
            print("\nID buku tidak ditemukan.")
        kembali(update_buku)
    
    elif input_option == "4":
        beranda()
    else:
        print('\nOpsi yang Anda input salah!')
        kembali(update_buku)



# ----------------------------------------------------------------------------------
# 4. Fitur Delete
# fitur ini digunakan untuk menghapus data yang ada di dictionary.


def hapus_buku() :
    print('''
    
    Halaman Penghapusan Buku
    ------------------------------------------
    
    1. Hapus Informasi Buku
    2. Kembali
    0. Keluar Program
    

    ''')

    input_option = input('\nMasukkan tujuan Anda (0-2): ')

    while True:
        if input_option == '1':
            # Meminta pengguna untuk memasukkan ID buku yang ingin dihapus
            book_id = input('\nMasukkan ID buku yang ingin dihapus: ')
            book_found = False

            # Menggunakan enumerate untuk mendapatkan indeks dan buku secara bersamaan
            for i, book in enumerate(data_buku):
                if book['ID'] == book_id:
                    book_found = True  # Menampilkan informasi buku yang akan dihapus
                    print(f"\nID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
                    confirm = input("\nApakah Anda yakin ingin menghapus buku ini? (Ya/Tidak): ").lower()

                    if confirm == 'ya':
                        # Menghapus buku dari daftar
                        data_buku.pop(i) 
                        print("\nBuku berhasil dihapus.")
                    elif confirm == 'tidak':
                        print("\nPenghapusan buku dibatalkan.")
                    else:
                        print('Input anda salah!')

            if not book_found:
                print("\nID buku tidak ditemukan.")
            kembali(hapus_buku)
        
        elif input_option == '2':
            beranda()
            return
        
        elif input_option == '0':
            keluar_program()
            return
        
        else:
            print('Input yang anda masukkan tidak tersedia! Silahkan coba lagi.')
            hapus_buku()


# ----------------------------------------------------------------------------------
# 5. Fitur list
# fitur ini memungkinkan pengguna untuk melihat semua buku yang ada, buku yang tersedia, atau buku yang sedang dipinjam.
def list_buku():
    print('''
    Halaman Pencarian Buku
    ------------------------------------------
    
    1. Tampilkan semua buku
    2. Tampilkan buku yang tersedia
    3. Tampilkan buku yang sedang dipinjam
    4. Kembali
    0. Keluar Program

    ''')
    
    input_option = input('\nMasukkan tujuan Anda (0-4): ')
    
    if input_option == '1':
        # Menampilkan semua buku
        print("\nDaftar Semua Buku:")
        for book in data_buku:
            print(f"ID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
        kembali(list_buku)  # Meminta pengguna untuk kembali ke menu setelah menampilkan buku
    elif input_option == '2':
        # Menampilkan buku yang tersedia
        print("\nDaftar Buku yang Tersedia:")
        for book in data_buku:
            if book['Status'].lower() == 'ada':  # Mengecek jika status buku adalah 'Ada'
                print(f"ID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
        kembali(list_buku)  # Meminta pengguna untuk kembali ke menu setelah menampilkan buku
    elif input_option == '3':
        # Menampilkan buku yang sedang dipinjam
        print("\nDaftar Buku yang Sedang Dipinjam:")
        for book in data_buku:
            if book['Status'].lower() == 'dipinjam':  # Mengecek jika status buku adalah 'Dipinjam'
                print(f"ID: {book['ID']}, Judul: {book['Title']}, Penulis: {book['Author']}, Tahun: {book['Year']}, Status: {book['Status']}")
        kembali(list_buku)  # Meminta pengguna untuk kembali ke menu setelah menampilkan buku
    elif input_option == '4':
        # Kembali ke beranda
        beranda()
    elif input_option == '0':
            keluar_program()
            return
    else:
        # Menangani input yang tidak valid
        print('Input yang anda masukkan tidak tersedia! Silahkan coba lagi.')
        list_buku()





# ----------------------------------------------------------------------------------
# 6. Fitur Keluar Program
# fitur ini memastikan bahwa pengguna memiliki opsi untuk mengonfirmasi apakah mereka benar-benar ingin keluar dari aplikasi sebelum benar-benar menutup program.
# digunakan sebagai recursive function atau callback function

def keluar_program():
    print('Apakah Anda yakin ingin keluar? (Ya(1)/Tidak(2))')
    confirm = input('1/2 :')
    while True :
        if confirm == "1" :
            print("Terima Kasih! Sampai jumpa kembali!")
            quit()
        elif confirm == "2" :
            beranda()
        else :
            print('Input yang Anda masukkan salah! Silahkan coba lagi!')
            keluar_program()

# ----------------------------------------------------------------------------------
# Beranda
# fungsi utama yang menampilkan menu beranda dari aplikasi perpustakaan
def beranda():
    print('''

Perpustakaan Purwadhika - Beranda   
Selamat Datang, Administrator!

Beranda:
1. Pendaftaran Buku Baru
2. Pencarian Buku
3. Pembaruan Informasi Buku
4. Hapus Informasi Buku 
5. Status Buku
6. Keluar
    ''')

    option_beranda = input('Masukkan pilihan Anda (1-6): ')

    if option_beranda == '1' :
        daftar_buku()
    elif option_beranda == '2' :
        cari_buku()
    elif option_beranda == '3' :
        update_buku()
    elif option_beranda == '4' :
        hapus_buku()
    elif option_beranda == '5' :
        list_buku()
    elif option_beranda == '6' :
        keluar_program()
    else :
        print('\n Pilihan Tidak Tersedia!')
        beranda()
    
beranda()