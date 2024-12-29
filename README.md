# Encryption-Decryption-tool

A simple GUI application for text encryption and decryption using the Fernet symmetric encryption provided by the cryptography library.

---

## Features
- **Encrypt Text:** Enter plain text to encrypt it securely.
- **Decrypt Text:** Provide encrypted text to decrypt it back to the original plain text.
- **User-Friendly Interface:** Built using Tkinter for easy text encryption and decryption.

---

## Prerequisites
- Python 3.7 or higher
- Required Python libraries: tkinter, cryptography

---

## Usage
**1. Encrypt Text**
- Enter the plain text in the "Enter Text" field.
- Click on the Encrypt button.
- The encrypted text will appear in the "Result" field.
**2. Decrypt Text**
- Enter the encrypted text in the "Enter Text" field.
- Click on the Decrypt button.
- The decrypted text will appear in the "Result" field.

---

## How It Works
**Fernet Encryption:**

A symmetric encryption key is generated at runtime using Fernet.generate_key().
Text is encrypted using the encrypt method and decrypted using the decrypt method.

**Tkinter GUI:**

Provides input and output text fields for encryption and decryption.
Buttons to trigger respective operations.

---

## Notes
The encryption key is generated at runtime and not saved persistently. If the app is restarted, previously encrypted text cannot be decrypted.
Handle encrypted text carefully, as invalid input will cause errors.

---


## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/heatblaze/Encryption-Decryption-tool.git
