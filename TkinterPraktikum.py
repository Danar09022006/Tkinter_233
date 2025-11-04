import tkinter as tk
import tkinter.messagebox as msg

# --- List global untuk menyimpan widget Entry ---
entry_widgets = []
jumlah_input = 10 

# --- FUNGSI PREDIKSI YANG DIMODIFIKASI ---
    

# --- Setup Jendela Utama ---
top = tk.Tk()
top.title("Aplikasi Prediksi Prodi")
top.geometry("350x450") # Sesuaikan ukuran untuk 10 input + output
# Atur warna latar belakang seperti di gambar
top.configure(bg="#0ce8e1") 

# --- Variabel khusus untuk mengontrol teks di label output ---
# Kita buat ini agar mudah mengubah teksnya dari dalam fungsi
output_var = tk.StringVar(value="Luaran Hasil Prediksi")


# --- Frame untuk Form Input 1-10 ---
frame_form = tk.Frame(top, bg="#0ce8e1")
frame_form.pack(pady=10, padx=20) 

# --- Loop untuk membuat 10 Label dan Entry ---
for i in range(jumlah_input):
    # Label "Nilai 1:", "Nilai 2:", dst.
    L = tk.Label(frame_form, text=f"Nilai {i+1}:", bg="#ffffff", font=("Arial", 10))
    L.grid(row=i, column=0, pady=5, sticky="w")
    
    # Entry (Kotak Input)
    E = tk.Entry(frame_form, bd=3, relief="sunken") # bd=3 agar ada border
    E.grid(row=i, column=1, pady=5, padx=10)
    
    entry_widgets.append(E) # Masukkan ke list

# --- TOMBOL PREDIKSI (Digayakan seperti gambar) ---
btn_prediksi = tk.Button(
    top, 
    text="Prediksi Prodi", 
    font=("Arial", 10, "bold"),
    bg="#ff4500",  # Warna oranye/merah
    fg="white",     # Teks putih
    relief="raised", # Agar terlihat menonjol
    bd=3            # Lebar border
)
btn_prediksi.pack(pady=10) # .pack() di bawah frame

# --- OUTPUT FIELD (Read-Only) ---
# Ini adalah "padding" yang tidak bisa diinput seperti yang Anda minta.
# Kita pakai Label, tapi kita gayakan agar MIRIP Entry di gambar.
label_output = tk.Label(
    top,
    textvariable=output_var, # Teksnya dikontrol oleh variabel
    bd=3,                    # Border (seperti Entry)
    relief="sunken",         # 'sunken' (cekung) agar terlihat seperti Entry
    font=("Arial", 10, "italic"),
    bg="#75948f",
    width=35,                # Lebar field
    anchor="w",              # Teks rata kiri (West)
    padx=5                   # Padding internal kiri-kanan
)
label_output.pack(pady=10, padx=20)

# --- Menjalankan Aplikasi ---
top.mainloop()