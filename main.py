import tkinter as tk

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + shift
            if char.islower():  
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():  
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char) - shift
            if char.islower():  
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_decrypt():
    message = entry_message.get()
    shift = int(entry_shift.get())

    encrypted_message = caesar_encrypt(message, shift)
    decrypted_message = caesar_decrypt(encrypted_message, shift)

    label_encrypted.config(text="Encrypted message: " + encrypted_message)
    label_decrypted.config(text="Decrypted message: " + decrypted_message)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")

# Create input fields
label_message = tk.Label(window, text="Enter the message:", font=("Helvetica", 12))
label_message.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_message = tk.Entry(window, width=50, font=("Helvetica", 12))
entry_message.grid(row=0, column=1, padx=10, pady=5)

label_shift = tk.Label(window, text="Enter the shift value:", font=("Helvetica", 12))
label_shift.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_shift = tk.Entry(window, width=50, font=("Helvetica", 12))
entry_shift.grid(row=1, column=1, padx=10, pady=5)

# Create buttons
encrypt_button = tk.Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt, font=("Helvetica", 12))
encrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Create output labels
label_encrypted = tk.Label(window, text="", font=("Helvetica", 12))
label_encrypted.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

label_decrypted = tk.Label(window, text="", font=("Helvetica", 12))
label_decrypted.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Start the GUI event loop
window.mainloop()
