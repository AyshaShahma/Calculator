from tkinter import Tk, END,Entry,N,E,S,W,Button
from tkinter import font
from tkinter import Label
from functools import partial
def get_input (entry,argu):
    entry.insert(END,argu)
def backspace(entry):
    input_len=len(entry.get())
    entry.delete(input_len-1)
def clear(entry):
    entry.delete(0,END)
def calc(entry):
    input=entry.get()
    try:
        output=str(eval(input.strip()))
    except ZeroDivisionError:
        popupmsg()
        output=""
    clear(entry)
    entry.insert(END, output)
def popupmsg():
    popup=Tk()
    popup.resizable(0,0)
    popup.geometry("120x120")
    popup.title("Alert")
    label=Label(popup,text="Cannot divide by 0!\n Enter valid numbers")
    label.pack(side="top",fill="x",pady=10)
    B1=Button(popup, text="Okay", bg='#F2E9E1',command=popup.destroy)
    B1.pack
def cal():
    base=Tk()
    base.title("Calculator")
    base.iconbitmap("C:/Users/USER/Downloads/gummy-bear (1).ico")
    base.resizable(0,0)
    entry_font=font.Font(size=15)
    entry=Entry(base,justify="right",font=entry_font)
    entry.grid(row=0,column=0,columnspan=4,sticky=N+W+S+E,padx=5,pady=5)
    cal_b_bg='#F8C8DC'
    num_b_bg='#FFFFFF'
    other_b_bg='#E2ECE9'
    text_fg='#4A4E69'
    b_active_bg='#D8E2DC'
    num_b=partial(Button,base,fg=text_fg,bg=num_b_bg,padx=10,pady=3,activebackground=b_active_bg)
    cal_b=partial(Button,base,fg=text_fg,bg=cal_b_bg,padx=10,pady=3,activebackground=b_active_bg)
    b7=num_b(text="7",bg=num_b_bg,command=lambda:get_input(entry,"7"))
    b7.grid(row=2,column=0,pady=5)
    b8=num_b(text="8",command=lambda:get_input(entry,"8"))
    b8.grid(row=2,column=1,pady=5)
    b9=num_b(text="9",command=lambda:get_input(entry,"9"))
    b9.grid(row=2,column=2,pady=5)
    b10=num_b(text="+",command=lambda:get_input(entry,"+"))
    b10.grid(row=4,column=3,pady=5)
    b4=num_b(text="4",command=lambda:get_input(entry,"4"))
    b4.grid(row=3,column=0,pady=5)
    b5=num_b(text="5",command=lambda:get_input(entry,"5"))
    b5.grid(row=3,column=1,pady=5)
    b6=num_b(text="6",command=lambda:get_input(entry,"6"))
    b6.grid(row=3,column=2,pady=5)
    b11=num_b(text="-",command=lambda:get_input(entry,"-"))
    b11.grid(row=3,column=3,pady=5)
    b1=num_b(text="1",command=lambda:get_input(entry,"1"))
    b1.grid(row=4,column=0,pady=5)
    b2=num_b(text="2",command=lambda:get_input(entry,"2"))
    b2.grid(row=4,column=1,pady=5)
    b3=num_b(text="3",command=lambda:get_input(entry,"3"))
    b3.grid(row=4,column=2,pady=5)
    b12=num_b(text="*",command=lambda:get_input(entry,"*"))
    b12.grid(row=2,column=3,pady=5)
    b0=num_b(text="0",command=lambda:get_input(entry,"0"))
    b0.grid(row=5,column=0,pady=5)
    b13=num_b(text=".",command=lambda:get_input(entry,"."))
    b13.grid(row=5,column=1,pady=5)
    b14=Button(base,text="/",fg=text_fg,bg=cal_b_bg,padx=10,pady=3,command=lambda:get_input(entry,"/"))
    b14.grid(row=1,column=3,pady=5)
    b15=Button(base,text="DEL",fg=text_fg,bg=cal_b_bg,padx=10,pady=3,command=lambda:backspace(entry),activebackground=b_active_bg)
    b15.grid(row=1,column=0,columnspan=2,padx=3,pady=5,sticky=N+S+E+W)

    b16=Button(base,text="C",fg=text_fg,bg=cal_b_bg,padx=10,pady=3,command=lambda:clear(entry),activebackground=b_active_bg)
    b16.grid(row=1,column=2,pady=5)
    b17=Button(base,text="=",fg=text_fg,bg=cal_b_bg,padx=10,pady=3,command=lambda:calc(entry),activebackground=b_active_bg)
    b17.grid(row=5,column=3,pady=5)
    b18=Button(base,text="^",fg=text_fg,bg=cal_b_bg,padx=10,pady=3,command=lambda:get_input(entry,"**"))
    b18.grid(row=5,column=2,pady=5)
    quit_btn = Button(base,text="Quit ♡",fg=text_fg,bg=cal_b_bg,relief="flat",command=base.quit,height=1,width=8,
)
    quit_btn.grid(row=6, column=1, columnspan=2, pady=8)
    base.mainloop()
if __name__ == "__main__":
    cal()
                  
            
                  
                  
    
    
    
    
    
    

    
    
    
        
        
    
    
    


