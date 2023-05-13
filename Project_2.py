from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Web Scraper")
root.geometry("500x300")


def search():
    if entry.get():
        if entry_1.get():
            url = entry.get()
            r = requests.get(url)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, "html.parser")
            abc = soup.find().get_text(entry_1.get())

            file = open(entry_2.get(), "w")
            file.write(abc)

            html_file = open('FILENAME.html', 'w')
            html_file.write(r.text)
            html_file.close()


label = Label(root, text="Enter URL", font=('arial', 20), fg="black")
label.place(x=180, y=30)

entry = Entry(root, width=45)
entry.place(x=120, y=80)

label_1 = Label(root, text="Enter key words", font=('arial', 20), fg="red")
label_1.place(x=40, y=130)

entry_1 = Entry(root)
entry_1.place(x=320, y=142)

label_2 = Label(root, text="Save file as", font=('arial', 20), fg="red")
label_2.place(x=40, y=180)

entry_2 = Entry(root)
entry_2.place(x=320, y=190)

button = Button(root, width=10, text="Enter", command=search)
button.place(x=210, y=240)

root.mainloop()