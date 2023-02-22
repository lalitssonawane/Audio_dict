import tkinter as tk
from tkinter import ttk
import requests
import json
from playsound import playsound

def search_word():
    """Search for a word definition in the API and update the display"""
    word = word_entry.get()
    url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/{}".format(word)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        if data:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, data[0]["meanings"][0]["definitions"][0]["definition"])
            playsound(data[0]["phonetics"][0]["audio"])
        else:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "Word not found.")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: Could not connect to API.")

def main():
    root = tk.Tk()
    root.title("Audio Dictionary")
    root.geometry("400x300")

    # Add a branding title with blue color
    title = tk.Label(root, text="Audio Dictionary", fg="white", bg="#3E6BEC", font=("Helvetica", 16))
    title.pack(fill="x")

    # Define the input field and search button
    word_label = ttk.Label(root, text="Enter word:")
    word_label.pack(pady=5)
    word_entry = ttk.Entry(root)
    word_entry.pack(pady=5)

    search_button = ttk.Button(root, text="Search", command=search_word)
    search_button.pack(pady=5)

    # Define the output field
    result_label = ttk.Label(root, text="Definition:")
    result_label.pack(pady=5)
    result_text = tk.Text(root, height=8)
    result_text.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
