import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x600")
root.title("Calculator")


equation_text = ""
equation_label = ctk.StringVar()

def btn_click(num):
    pass
def btn_equal():
    pass
def btn_clear():
    pass

label = ctk.CTkLabel(root, textvariable=equation_label,fg_color="#EEEEEE",height=130)
label.pack()



#tabmenu
tabmenu = ctk.CTkTabview(root, width=400, height=84)
tabmenu.pack()

tabtrigon = tabmenu.add("Trigonmetry")
tabroot = tabmenu.add("Roots & Square")

tabtrigon.columnconfigure(0,weight=1)
tabtrigon.columnconfigure(1,weight=1)
tabtrigon.columnconfigure(2,weight=1)

#tabmenu buttons
btn_sin = ctk.CTkButton(tabtrigon, text="sin")
btn_sin.grid(row=0,column=0,padx=4,pady=4)
btn_cos = ctk.CTkButton(tabtrigon, text="cos")
btn_cos.grid(row=0,column=1,padx=4,pady=4)
btn_tan = ctk.CTkButton(tabtrigon, text="tan")
btn_tan.grid(row=0,column=2,padx=4,pady=4)

tabroot.columnconfigure(0, weight=1)
tabroot.columnconfigure(1, weight=1)
tabroot.columnconfigure(2, weight=1)

btn_s2 = ctk.CTkButton(tabroot, text="Square")
btn_s2.grid(row=0,column=0, padx=4,pady=4)
btn_s3 = ctk.CTkButton(tabroot, text="Square")
btn_s3.grid(row=0,column=1, padx=4,pady=4)
btn_s4 = ctk.CTkButton(tabroot, text="Square")
btn_s4.grid(row=0,column=2, padx=4,pady=4)

#manage button frame
btn_frame = ctk.CTkFrame(root,width=400, height=80)

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)
btn_frame.columnconfigure(3, weight=1)

btn_pi = ctk.CTkButton(btn_frame, height=50,text="pi")
btn_pi.grid(row=0,column=0,padx=4,pady=4)
btn_n1 = ctk.CTkButton(btn_frame, height=50,text="n!")
btn_n1.grid(row=0,column=1,padx=4,pady=4)
btn_clear = ctk.CTkButton(btn_frame, height=50,text="Clear")
btn_clear.grid(row=0,column=2,padx=4,pady=4)
btn_backspace = ctk.CTkButton(btn_frame, height=50,text="<---")
btn_backspace.grid(row=0,column=3,padx=4,pady=4)

btn_frame.pack(padx=4)

#number button frame
n_btn_frame = ctk.CTkFrame(root,width=400)

n_btn_frame.columnconfigure(0,weight=1)
n_btn_frame.columnconfigure(1,weight=1)
n_btn_frame.columnconfigure(2,weight=1)
n_btn_frame.columnconfigure(3,weight=1)

#first row
btn1= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="first")
btn1.grid(row=0,column=0,padx=4,pady=4)
btn2= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="first")
btn2.grid(row=0,column=1,padx=4,pady=4)
btn3= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="first")
btn3.grid(row=0,column=2,padx=4,pady=4)
btn4= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="first")
btn4.grid(row=0,column=3,padx=4,pady=4)

#second row
btn5= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="second")
btn5.grid(row=1,column=0,padx=4,pady=4)
btn6= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="second")
btn6.grid(row=1,column=1,padx=4,pady=4)
btn7= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="second")
btn7.grid(row=1,column=2,padx=4,pady=4)
btn8= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="second")
btn8.grid(row=1,column=3,padx=4,pady=4)

#thrid row
btn9= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="third")
btn9.grid(row=2,column=0,padx=4,pady=4)
btn10= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="third")
btn10.grid(row=2,column=1,padx=4,pady=4)
btn11= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="third")
btn11.grid(row=2,column=2,padx=4,pady=4)
btn12= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="third")
btn12.grid(row=2,column=3,padx=4,pady=4)

#fourth row
btn13= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fourth")
btn13.grid(row=3,column=0,padx=4,pady=4)
btn14= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fourth")
btn14.grid(row=3,column=1,padx=4,pady=4)
btn15= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fourth")
btn15.grid(row=3,column=2,padx=4,pady=4)
btn16= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fourth")
btn16.grid(row=3,column=3,padx=4,pady=4)

#fifth row
btn17= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fifth")
btn17.grid(row=4,column=0,padx=4,pady=4)
btn18= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fifth")
btn18.grid(row=4,column=1,padx=4,pady=4)
btn19= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fifth")
btn19.grid(row=4,column=2,padx=4,pady=4)
btn20= ctk.CTkButton(n_btn_frame,width=90 ,height=56,text="fifth")
btn20.grid(row=4,column=3,padx=4,pady=4)

n_btn_frame.pack()




root.mainloop()