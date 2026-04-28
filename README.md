<div align="center">

# 🔐 Enkryptor - Advanced Data Encryption Tool

### A Robust, Desktop-Based File Security Solution featuring AES-256 Encryption, Secure Key Derivation, and a Modern GUI.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-Lib-red?style=for-the-badge&logo=pypi&logoColor=white)
![AES](https://img.shields.io/badge/AES-Security-005571?style=for-the-badge&logo=security&logoColor=white)

</div>

---

## 📖 Overview

**Enkryptor** is a desktop application designed to secure sensitive data against unauthorized access in an era of escalating cyber threats. Unlike complex command-line tools, Enkryptor bridges the gap between **military-grade security** and **user experience** by offering a sleek, intuitive GUI for encryption operations.

The system utilizes the **Advanced Encryption Standard (AES)** via the Fernet symmetric encryption scheme. It ensures data integrity and confidentiality for individuals and enterprises handling sensitive documents, images, and archives.

---

## 🚀 Key Features

### 🛡️ 1. Robust AES Encryption
- **Standard:** Implements **AES (Advanced Encryption Standard)** in CBC mode via the Fernet specification.
- **Key Strength:** Supports 128-bit, 192-bit, and **256-bit encryption keys** for maximum security.
- **Data Integrity:** Ensures files cannot be read or modified without the correct key.

### 🔑 2. Secure Key Management
- **Key Derivation:** Uses **PBKDF2HMAC** with **SHA256** hashing to derive strong cryptographic keys from user passwords.
- **Salting:** Implements random 16-byte salts to prevent rainbow table attacks.
- **Custom Passwords:** Allows users to set custom passwords or generate strong, random keys automatically.

### 💻 3. Modern GUI (PyQt5)
- **Drag & Drop:** Intuitive interface allowing users to drag files directly into the encryptor.
- **Batch Processing:** Capable of encrypting or decrypting **multiple files** simultaneously.
- **Visual Feedback:** Real-time progress indicators and success/failure status alerts.

### 📁 4. File Handling & Compatibility
- **Universal Support:** Encrypts text files, images, PDFs, and archives without data corruption.
- **Metadata Preservation:** Retains original file extensions and attributes post-decryption.
- **Padding Logic:** Automatically handles block padding to align with AES block requirements.

---

## 🧰 Tech Stack

| Layer | Technology |
|------|------------|
| **Core Logic** | Python 3.12 |
| **GUI Framework** | PyQt5 (Qt Designer) |
| **Encryption Lib** | `cryptography` (Python Library) |
| **Algorithm** | AES (Symmetric) |
| **Hashing** | SHA256 (via `hashlib`) |
| **Key Derivation** | PBKDF2HMAC |

---

## 🏗️ System Architecture

| Component | Description |
| :--- | :--- |
| **Frontend (UI)** | Built with **PyQt5**, handling file selection, drag-and-drop events, and user inputs. |
| **Controller** | Manages logic flow between the UI and the cryptographic engine. |
| **Encryption Engine** | Generates keys, salts passwords, and performs AES transformations. |
| **File Handler** | Reads binary data, applies padding, and writes encrypted/decrypted outputs. |

### 🔄 Data Flow (Encryption Pipeline)
1. **Input:** User selects file & enters password.
2. **Salt & Hash:** System generates a random salt and hashes the password using **PBKDF2HMAC**.
3. **Key Gen:** A URL-safe base64-encoded key is derived.
4. **Encryption:** File data is read, padded, and encrypted using the **Fernet** cipher.
5. **Output:** Encrypted ciphertext is written to a new file (e.g., `.enc`).

---

## 🛠️ Installation & Setup

### Prerequisites
- Python (v3.10+)
- pip package manager

### 1. Clone the Repository
```bash
git clone [https://github.com/Er-Ishan-Srivastav/EncryptionDecryptionTool.git](https://github.com/Er-Ishan-Srivastav/EncryptionDecryptionTool.git)
cd EncryptionDecryptionTool
```
