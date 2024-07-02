from tkinter import *
from QuickAgent import ConversationManager
import asyncio
def click():
    manager = ConversationManager()
    asyncio.run(manager.main())
window=Tk()
button=Button(window,
              text='click me!',
              command=click,
              font=('Comic Sans',30))
button.pack()
window.mainloop()