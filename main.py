from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt text
def encrypt_text():
    plain_text = text_input.get("1.0", END).strip()
    if plain_text:
        encrypted_text = cipher.encrypt(plain_text.encode())
        result_output.delete("1.0", END)
        result_output.insert("1.0", encrypted_text)
    else:
        messagebox.showerror("Error", "Please enter text to encrypt.")

# Decrypt text
def decrypt_text():
    encrypted_text = text_input.get("1.0", END).strip()
    if encrypted_text:
        try:
            decrypted_text = cipher.decrypt(encrypted_text.encode())
            result_output.delete("1.0", END)
            result_output.insert("1.0", decrypted_text.decode())
        except Exception as e:
            messagebox.showerror("Error", "Invalid encrypted text.")
    else:
        messagebox.showerror("Error", "Please enter encrypted text.")

# Create GUI
app = Tk()
app.title("Encryption/Decryption App")
app.geometry("400x300")

Label(app, text="Enter Text:").pack()
text_input = Text(app, height=5)
text_input.pack()

Button(app, text="Encrypt", command=encrypt_text).pack(pady=5)
Button(app, text="Decrypt", command=decrypt_text).pack(pady=5)

Label(app, text="Result:").pack()
result_output = Text(app, height=5)
result_output.pack()

app.mainloop()
