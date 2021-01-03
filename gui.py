import tkinter as tk
import webbrowser
import requests

from news import News

window = tk.Tk()
window.title(" Sheet Metal News Scraper")
window.iconbitmap('./news scraper.ico')
def internet_connection(url='http://www.google.com/', timeout=3):


    try:
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:

        return False

def open_link(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.open(url)


def call_fractory_news():
    lab = tk.Label(text="Fractory news",padx=5,pady=20)
    lab.grid(row=0,column=0,sticky="W")

    nws = News()  # Instantiating News class from news module
    lst = nws.fractory()


    lst_values = list(lst.values())
    lst_keys = list(lst.keys())
    lks = [i for i in range(10)]

    lks[0] = tk.Label(text=f"1. {lst_keys[0]}", fg="blue", cursor="hand2")
    lks[0].bind('<Button-1>', lambda j: open_link(lst_values[0]))
    lks[0].grid(row=1,column=0,sticky="W")

    lks[1] = tk.Label(text=f"2. {lst_keys[1]}", fg="blue", cursor="hand2")
    lks[1].bind('<Button-1>', lambda j: open_link(lst_values[1]))
    lks[1].grid(row=2,column=0, sticky="W")

    lks[2] = tk.Label(text=f"3. {lst_keys[2]}", fg="blue", cursor="hand2")
    lks[2].bind('<Button-1>', lambda j: open_link(lst_values[2]))
    lks[2].grid(row=3,column=0, sticky="W")

    lks[3] = tk.Label(text=f"4. {lst_keys[3]}", fg="blue", cursor="hand2")
    lks[3].bind('<Button-1>', lambda j: open_link(lst_values[3]))
    lks[3].grid(row=4,column=0, sticky="W")

    lks[4] = tk.Label(text=f"5. {lst_keys[4]}", fg="blue", cursor="hand2")
    lks[4].bind('<Button-1>', lambda j: open_link(lst_values[4]))
    lks[4].grid(row=5,column=0, sticky="W")

    lks[5] = tk.Label(text=f"6. {lst_keys[5]}", fg="blue", cursor="hand2")
    lks[5].bind('<Button-1>', lambda j: open_link(lst_values[5]))
    lks[5].grid(row=6,column=0, sticky="W")

    lks[6] = tk.Label(text=f"7. {lst_keys[6]}", fg="blue", cursor="hand2")
    lks[6].bind('<Button-1>', lambda j: open_link(lst_values[6]))
    lks[6].grid(row=7,column=0, sticky="W")

    lks[7] = tk.Label(text=f"8. {lst_keys[7]}", fg="blue", cursor="hand2")
    lks[7].bind('<Button-1>', lambda j: open_link(lst_values[7]))
    lks[7].grid(row=8,column=0, sticky="W")

    lks[8] = tk.Label(text=f"9. {lst_keys[8]}", fg="blue", cursor="hand2")
    lks[8].bind('<Button-1>', lambda j: open_link(lst_values[8]))
    lks[8].grid(row=9,column=0, sticky="W")

    lks[9] = tk.Label(text=f"10. {lst_keys[9]}", fg="blue", cursor="hand2")
    lks[9].bind('<Button-1>', lambda j: open_link(lst_values[9]))
    lks[9].grid(row=10,column=0, sticky="W")




def call_fabricator_news():
    lab = tk.Label(text="The Fabricator.com news", padx=5, pady=20)
    lab.grid(row=11, column=0, sticky="W")
    nwsf=News()
    lstf=nwsf.fabricator() #Calling fabricator method

    lstf_values = list(lstf.values())   #value list from fabricator.com site*
    lstf_keys = list(lstf.keys())#key list from fabricator.com site
    lksf = [i for i in range(10)]

    lksf[0] = tk.Label(text=f"1. {lstf_keys[0]}", fg="blue", cursor="hand2")
    lksf[0].bind('<Button-1>', lambda j: open_link(lstf_values[0]))
    lksf[0].grid(row=12, column=0, sticky="W")

    lksf[1] = tk.Label(text=f"2. {lstf_keys[1]}", fg="blue", cursor="hand2")
    lksf[1].bind('<Button-1>', lambda j: open_link(lstf_values[1]))
    lksf[1].grid(row=13, column=0, sticky="W")

    lksf[2] = tk.Label(text=f"3. {lstf_keys[2]}", fg="blue", cursor="hand2")
    lksf[2].bind('<Button-1>', lambda j: open_link(lstf_values[2]))
    lksf[2].grid(row=14, column=0, sticky="W")

    lksf[3] = tk.Label(text=f"4. {lstf_keys[3]}", fg="blue", cursor="hand2")
    lksf[3].bind('<Button-1>', lambda j: open_link(lstf_values[3]))
    lksf[3].grid(row=15, column=0, sticky="W")

    lksf[4] = tk.Label(text=f"5. {lstf_keys[4]}", fg="blue", cursor="hand2")
    lksf[4].bind('<Button-1>', lambda j: open_link(lstf_values[1]))
    lksf[4].grid(row=16, column=0, sticky="W")

    lksf[5] = tk.Label(text=f"6. {lstf_keys[1]}", fg="blue", cursor="hand2")
    lksf[5].bind('<Button-1>', lambda j: open_link(lstf_values[5]))
    lksf[5].grid(row=17, column=0, sticky="W")

    lksf[6] = tk.Label(text=f"7. {lstf_keys[6]}", fg="blue", cursor="hand2")
    lksf[6].bind('<Button-1>', lambda j: open_link(lstf_values[6]))
    lksf[6].grid(row=18, column=0, sticky="W")

    lksf[7] = tk.Label(text=f"8. {lstf_keys[7]}", fg="blue", cursor="hand2")
    lksf[7].bind('<Button-1>', lambda j: open_link(lstf_values[7]))
    lksf[7].grid(row=19, column=0, sticky="W")

    lksf[8] = tk.Label(text=f"9. {lstf_keys[8]}", fg="blue", cursor="hand2")
    lksf[8].bind('<Button-1>', lambda j: open_link(lstf_values[8]))
    lksf[8].grid(row=20, column=0, sticky="W")

    lksf[9] = tk.Label(text=f"10. {lstf_keys[9]}", fg="blue", cursor="hand2")
    lksf[9].bind('<Button-1>', lambda j: open_link(lstf_values[9]))
    lksf[9].grid(row=21, column=0, sticky="W")

if internet_connection():
    call_fractory_news()
    call_fabricator_news()
    window.mainloop()

else:

    a=tk.Label(text="No Internet Connection")
    a.grid(row=0,column=0)
    window.mainloop()
# btn_frame = tk.Frame(master=window, relief=tk.SUNKEN)
# button = tk.Button(master=btn_frame, text="Get News", width=10, height=2, )
# btn_frame.pack()
# button.pack()
#
# frame = tk.Frame(master=window, relief=tk.GROOVE)
# label = tk.Label(master=frame, text="Here's the latest sheet-metal news", bg="plum")
# label.pack()
# frame.pack()
#
# window.mainloop()
