# 🔐 Secret Code Translator

A lightweight secret message encoder and decoder built with Python and deployed as an interactive web app using Streamlit. 

Created as a fun project based on Python's **Exercise 4 (Secret Code Language)** to practice string manipulation, slicing, loops, and cloud deployment.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

## 🌐 Live Demo

👉 **[Try the Live App Here](https://your-app-name.streamlit.app)** *(Replace with your Streamlit URL)*

---

## ✨ Features

* **Two-Way Translation:** Seamlessly switch between **Encode** and **Decode** modes.
* **Randomized Obfuscation:** Uses Python's `random` and `string` modules to inject fresh 3-character lowercase padding around longer words on every run—so the same message looks different each time you encode it.
* **Input Validation:** Prevents empty submissions with clean UI warnings.
* **One-Click Copy:** Displays results inside a Streamlit code block for quick copying and sharing.

---

## ⚙️ How It Works

The translator splits your message word-by-word and applies two simple rules:

### Encoding
* **Words with 3 or more characters:**
  1. Moves the first letter to the end of the word.
  2. Attaches 3 random lowercase letters to the front and 3 to the back.
* **Words with fewer than 3 characters:**
  1. Reverses the word.

**Example:** `"python is fun"` ➔ `"qweythonpxyz si abcunfdef"`

### Decoding
* **Words with 3 or more characters:** Strips the 3 random characters from both ends and moves the last letter back to the front.
* **Words with fewer than 3 characters:** Reverses the word back to normal.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Frontend & Hosting:** Streamlit / Streamlit Community Cloud
* **Standard Libraries:** `random`, `string`

---

## 🚀 Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/secret-code-app.git](https://github.com/your-username/secret-code-app.git)
   cd secret-code-app
