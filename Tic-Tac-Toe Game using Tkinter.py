from tkinter import *
from tkinter import messagebox
tk =Tk()
tk.title("Tic Tac Toe")

bclick = True

def ttt(button):
     global bclick
     if button["text"] == " " and bclick == True:
         button["text"] = "X"
         bclick = False
     elif button["text"] == " " and bclick == False:
          button["text"] = "O"
          bclick = True
     win()

def win():
     if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          messagebox.showinfo("Player O",'Winner is O !!!!')
          reset()
     if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
          button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
          button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
          messagebox.showinfo("Player X",'Winner is X !!!!')
          reset()
def reset():
      button1["text"]=""
      button2["text"]=""
      button3["text"]=""
      button4["text"]=""
      button5["text"]=""
      button6["text"]=""
      button7["text"]=""
      button8["text"]=""
      button9["text"]=""



buttons=StringVar()

button1 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button1))
button1.grid(row=1,column=0,sticky = S+N+E+W)

button2 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button2))
button2.grid(row=1,column=1,sticky = S+N+E+W)

button3 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button3))
button3.grid(row=1,column=2,sticky = S+N+E+W)

button4 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button4))
button4.grid(row=2,column=0,sticky = S+N+E+W)

button5 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button5))
button5.grid(row=2,column=1,sticky = S+N+E+W)

button6 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button6))
button6.grid(row=2,column=2,sticky = S+N+E+W)

button7 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button7))
button7.grid(row=3,column=0,sticky = S+N+E+W)

button8 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button8))
button8.grid(row=3,column=1,sticky = S+N+E+W)

button9 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=4,width=8,command=lambda:ttt(button9))
button9.grid(row=3,column=2,sticky = S+N+E+W)

tk.mainloop()