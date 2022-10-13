import scraper
import tkinter as tk
from tkinter import ttk, Text
import schedule
import threading


def select(url):
    scraper.scrape(url)


def runSchedule():
    schedule.every(5).minutes.do(scraper.main())


if __name__ == '__main__':
    # create the application window
    root = tk.Tk()

    # window title
    root.title("FAST ETL")

    # window size
    root.geometry('700x400+50+50')
    root.resizable(0, 0)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=7)

    text = Text(root, height=19)
    text.place(x=25, y=70)

    # text.insert('1.0', 'Stock Information\n'
    #                    'Page  1\n'
    #                    'Stock Code: VI220220\n'
    #                    'Stock Code: VK220221\n'
    #                    'Stock Code: VN220222\n'
    #                    'Stock Code: SA220084\n'
    #                    'Stock Code: VN220215\n'
    #                    'Stock Code: VS220216\n'
    #                    'Stock Code: VX220217\n'
    #                    'Stock Code: FZ220001\n'
    #                    'Stock Code: FZ220002\n'
    #                    'Stock Code: VS220195\n'
    #                    'Stock Code: VN220169\n'
    #                    'Stock Code: UG220112\n'
    #                    'Stock Code: VE220151\n'
    #                    'Stock Code: VF220152')
    text['state'] = 'disabled'
    scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
    scrollbar.place(x=660, y=70, height=308)

    announcement = ttk.Button(
        root,
        text='All Announcement',
        command=lambda: threading.Thread(target=select(
            'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB010400')
        ).start()
    )

    facility = ttk.Button(
        root,
        text='Facility Information',
        command=lambda: threading.Thread(target=select(
            'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030800')
        ).start()
    )

    stock = ttk.Button(
        root,
        text='Stock Information',
        command=lambda: threading.Thread(target=select(
            'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB030900')
        ).start()
    )

    auction = ttk.Button(
        root,
        text='Auction Calendar',
        command=lambda: threading.Thread(target=select(
            'https://fast.bnm.gov.my/fastweb/public/FastPublicBrowseServlet.do?mode=MAIN&taskId=PB050500')
        ).start()
    )

    scheduler = ttk.Button(
        root,
        text='Start Scheduler',
        command=lambda: threading.Thread(target=runSchedule())
    )

    announcement.grid(row=0, column=1, padx=5, pady=5, ipadx=10)
    facility.grid(row=0, column=2, padx=5, pady=5, ipadx=10)
    stock.grid(row=0, column=3, padx=5, pady=5, ipadx=14)
    auction.grid(row=0, column=4, padx=5, pady=5, ipadx=15)
    scheduler.grid(row=0, column=5, padx=5, pady=5, ipadx=15)

    # place a label on the root window
    # message = tk.Label(root, text="Hello, World!")
    # message.pack()

    # keeps the window visible on the screen
    root.mainloop()
