import time
import pyautogui
from faker import Faker

def open_chrome_in_incognito(url):
    # Membuka Google Chrome dalam mode incognito
    pyautogui.hotkey('win', 'r')  # Menampilkan Run dialog
    pyautogui.typewrite('chrome.exe --incognito --start-maximized')  # Mengetik "chrome.exe --incognito" dalam Run dialog
    pyautogui.press('enter')  # Menekan tombol Enter untuk menjalankan Chrome

    # Menunggu beberapa detik agar Chrome sempat membuka
    time.sleep(8)
    # pyautogui.hotkey('f11')
    # Memastikan Chrome sudah aktif dan memfokuskan ke jendela incognito
    # pyautogui.click(x=1920, y=1080)  # Ganti koordinat sesuai dengan resolusi layar Anda

    # Memasukkan URL ke dalam address bar dan menekan Enter
    pyautogui.hotkey('ctrl', 'l')  # Memilih alamat URL
    pyautogui.typewrite(url)
    pyautogui.press('enter')


def fill_registration_form(random_email, random_password, random_name):

    # Buka URL Spotify dalam browser
    # pyautogui.hotkey('ctrl', 'shift', 'n')
    # pyautogui.typewrite("https://www.spotify.com/au/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-id")
    # pyautogui.press('enter')
    # Menunggu beberapa detik sebelum memulai untuk memberikan waktu untuk mengaktifkan browser
    time.sleep(8)
    pyautogui.click(x=300, y=700)  # Ganti koordinat sesuai dengan lokasi kolom input yang diinginkan
   # Ganti koordinat sesuai dengan lokasi kolom input yang diinginkan
    pyautogui.press('tab',presses=3)  # Pindah ke kolom nama
    
    # Menggunakan pyautogui untuk mengisi formulir
    pyautogui.typewrite(random_email)
    pyautogui.press('tab')  # Pindah ke kolom password
    # time.sleep(5)
    pyautogui.typewrite(random_password)
    pyautogui.press('tab',presses=2)  # Pindah ke kolom nama
    # time.sleep(5)
    pyautogui.typewrite(random_name)
    
    # Pindah ke tanggal lahir dan mengisinya
    pyautogui.press('tab', presses=1)  # Pindah ke tanggal lahir
    # time.sleep(5)
    pyautogui.typewrite('12')
    pyautogui.press('tab')  # Pindah ke bulan lahir
    pyautogui.press('down', presses=12)
    pyautogui.press('tab')  # Pindah ke tahun lahir
    pyautogui.typewrite('2000')

    # Pilih "Prefer not to say"
    pyautogui.press('tab', presses=1)
    pyautogui.press('space')

    # Pilih "Please send me news and offers from Spotify"
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')

    # Klik tombol daftar
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')

    # Tunggu beberapa detik untuk proses pendaftaran selesai
    time.sleep(10)

def save_account_to_file(random_email, random_password):
    with open('akun.txt', 'a') as file:
        file.write(f'{random_email}:{random_password}\n')

def create_spotify_account():
    jumlah_akun = 50
    fake = Faker()

    for _ in range(jumlah_akun):
        random_username = fake.user_name()
        gmail_domain = "windcute.icu"
        random_email = f"{random_username}@{gmail_domain}"
        random_password = '@Pisang123'
        random_name = fake.name()
        spotify_url = "https://www.spotify.com/au/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-id"
        open_chrome_in_incognito(spotify_url)
        fill_registration_form(random_email, random_password, random_name)
        save_account_to_file(random_email, random_password)

        # Tutup tab saat ini
        # pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('alt', 'f4')  # Memilih alamat URL


# Menjalankan otomatisasi
create_spotify_account()
