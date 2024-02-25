import sympy as s 
from tkinter import * 
from tkinter import ttk 
# from matplotlib import pyplot 
import matplotlib
matplotlib.use("TkAgg") 
import matplotlib.pyplot as plt
import time
import numpy as np 
import random as r 
############################################
lst = []
lst_f = []
lst_x = []
lst_y = []


def b_3_equation() : 
    win_ask.destroy()
    win = Tk()
    win.geometry("700x500")
    win.title("equation")
    win.resizable(False,False)
    cnv1 = Canvas(win)#
    n_0 = PhotoImage(file=r"C:\Program Files\masscal\zero.png")
    n_1 = PhotoImage(file=r"C:\Program Files\masscal\number-1.png")
    n_2 = PhotoImage(file=r"C:\Program Files\masscal\two.png")
    n_3 = PhotoImage(file=r"C:\Program Files\masscal\three.png")
    n_4 = PhotoImage(file=r"C:\Program Files\masscal\four.png")
    n_5 = PhotoImage(file=r"C:\Program Files\masscal\five.png")
    n_6 = PhotoImage(file=r"C:\Program Files\masscal\six.png")
    n_7 = PhotoImage(file=r"C:\Program Files\masscal\seven.png")
    n_8 = PhotoImage(file=r"C:\Program Files\masscal\eight.png")
    n_9 = PhotoImage(file=r"C:\Program Files\masscal\nine.png")
    n_m = PhotoImage(file=r"C:\Program Files\masscal\minus.png")
    n_s = PhotoImage(file=r"C:\Program Files\masscal\study.png")
    n_l = PhotoImage(file=r"C:\Program Files\masscal\education.png")
    n_me = PhotoImage(file=r"C:\Program Files\masscal\hacker.png")
    im_me = PhotoImage(file=r"C:\Program Files\masscal\instagram.png")
    im_me2 = PhotoImage(file=r"C:\Program Files\masscal\telegram.png")
    im_exit = PhotoImage(file=r"C:\Program Files\masscal\exit.png")
    im_square = PhotoImage(file=r"C:\Program Files\masscal\square (2).png")
    im_error = PhotoImage(file=r"C:\Program Files\masscal\computer.png")
    im_instagram_id = PhotoImage(file=r"C:\Program Files\masscal\instagram_id.png")
    im_telegram_id = PhotoImage(file=r"C:\Program Files\masscal\telegram_id.png")
    im_learning = PhotoImage(file=r"C:\Program Files\masscal\equation_teaching2.png")
    im_practice = PhotoImage(file=r"C:\Program Files\masscal\3x_exces.png")
    im_cal = PhotoImage(file=r"C:\Program Files\masscal\calculator.png")
    im1 = PhotoImage(file=r"C:\Program Files\masscal\one.png")
    im2 = PhotoImage(file=r"C:\Program Files\masscal\number-2.png")
    im3 = PhotoImage(file=r"C:\Program Files\masscal\number-3.png")
    im4 = PhotoImage(file=r"C:\Program Files\masscal\number-4.png")
    im5 = PhotoImage(file=r"C:\Program Files\masscal\number-5.png")
    im6 = PhotoImage(file=r"C:\Program Files\masscal\number-six.png")
    im7 = PhotoImage(file=r"C:\Program Files\masscal\number-7.png")
    im8 = PhotoImage(file=r"C:\Program Files\masscal\number-8.png")
    im9 = PhotoImage(file=r"C:\Program Files\masscal\number-9.png")
    im0 = PhotoImage(file=r"C:\Program Files\masscal\number-zero.png")
    # ----------------------------------------------- 
    def number (x) :
        if entry_a["state"] == "normal" : 
            index = len(entry_a.get()) 
            entry_a.insert(index , x)

        if entry_b["state"] == "normal" : 
            index = len(entry_b.get()) 
            entry_b.insert(index , x)

        if entry_c["state"] == "normal" : 
            index = len(entry_c.get()) 
            entry_c.insert(index , x)

        if entry_d["state"] == "normal" : 
            index = len(entry_d.get()) 
            entry_d.insert(index , x)

    def clear () :
        entry_a.delete(0,END)
        entry_b.delete(0,END)
        entry_c.delete(0,END)
        entry_d.delete(0,END)

    #

    def help() :
        new_win = Toplevel(win)
        new_win.geometry("450x250")
        label_1 = Label(new_win,image=n_label)
        label_1.place(x=0,y=0) 

    #

    def learn () : 
        win_teach = Toplevel(win)
        win_teach.geometry("832x565")
        win_teach.resizable(False,False)
        label_teach = Label(win_teach,image=im_learning)
        label_teach.place(x=0,y=0)

    #

    def b_me () : 
        def b_tel () : 
            telegram = Toplevel()
            telegram.geometry("530x90")
            telegram.title("TELEGRAM")
            ins_id = Label(telegram,image=im_telegram_id,bg="white")
            ins_id.place(x=0,y=0)

        def b_instagram () :
            instagram = Toplevel()
            instagram.geometry("560x120") 
            instagram.title("INSTAGRAM")
            ins_id = Label(instagram,image=im_instagram_id,bg="white")
            ins_id.place(x=0,y=0)

        win_about_me = Toplevel()
        win_about_me.geometry("550x300")
        win_about_me.title("About Me")
        l_1 = Label(win_about_me,background="#00FFAE",height=500,width=800)
        l_1.place(x=0,y=0)
        l_2 = Label(win_about_me,background="#00FFAE",foreground="white",font=("Tw Cen MT Condensed Extra Bold",27),text=" Hello again\n Thank you for choosing my app\n  My name is Parham Beiraghdar\n  you can contact me using these ways",)
        l_2.place(x=0,y=0)
        b_instagram = Button(win_about_me,command=b_instagram,image=im_me,relief=FLAT,background="#00FFAE",activebackground="#00FFAE")
        b_instagram.place(x=170,y=230)
        b_telegram = Button(win_about_me,command=b_tel,image=im_me2,relief=FLAT,background="#00FFAE",activebackground="#00FFAE")
        b_telegram.place(x=270,y=230)
    #
    def practice () : 
        practice_win = Toplevel()
        practice_win.title("PRACTICE TIME ")
        practice_win.geometry("600x700")
        l_examples = Label(practice_win,image=im_practice)
        l_examples.place(x=0,y=0)
    #
    def exit () : 
        win.destroy()
    #
    def equal () :
        try : 
            a = int(entry_a.get())
            b = int(entry_b.get())
            c = int(entry_c.get())
            d = int(entry_d.get())
            x = s.symbols("x")
            expr = a*x**3 + b*x**2 + c*x + d  
            sol = s.solve(expr,x)
            answer_entry.delete(0,END)
            answer_entry.insert(0,sol)

            new_win1 = Toplevel()
            new_win1.geometry("600x160")

            def yes_button () :
                for item in range(-10,10):
                    lst_x.append(item)
                    y = a*item**3 + b*item**2 + c*item + d 
                    lst_y.append(y)
                x = np.array(lst_x)
                y = np.array(lst_y)
                rounded_sol = [round(item) for item in sol]

                if len(rounded_sol) == 1 : 
                    plt.scatter(rounded_sol,0, color="red", marker="o", label="Intersection Points")
                if len(rounded_sol) == 2 : 
                    plt.scatter(rounded_sol,[0,0], color="red", marker="o", label="Intersection Points")    
                if len(rounded_sol) == 3 : 
                    plt.scatter(rounded_sol,[0,0,0], color="red", marker="o", label="Intersection Points") 

                plt.axhline(0, color="black", linewidth=3)
                plt.axvline(0, color="black", linewidth=3)
                plt.xlabel("X-axis")
                plt.ylabel("Y-axis")
                plt.plot(x,y)
                plt.legend()
                plt.grid()
                plt.show()
                lst_y.clear()
                lst_x.clear()

            def no_button () :
                new_win1.destroy()

            label_1=Label(new_win1,text="Do you want to see the chart as well ? ",background="#00FF9E",foreground="white",font=("Microsaft",20,"bold"))
            label_1.place(x=44,y=10,height=80,width=520)
            b_1 = ttk.Button(new_win1,text="YES please",command=yes_button)
            b_2 = ttk.Button(new_win1,text="NO thanks",command=no_button)
            b_1.place(x=360,y=110)
            b_2.place(x=160,y=110)
    
        except :
            error_win = Toplevel(win)
            error_win.geometry("260x260")
            error_label = Label(error_win,image=im_error,bg="#FFD1D1")
            error_label.place(x=0,y=0)
    #

    def e_a (event) : 
        entry_a.config(state=NORMAL) # baraye taghiir estefade mishe 
        entry_b.config(state="readonly") 
        entry_c.config(state="readonly") 
        entry_d.config(state="readonly")
    #
    def e_b (event) :
        entry_a.config(state="readonly") # baraye taghiir estefade mishe 
        entry_b.config(state=NORMAL) 
        entry_c.config(state="readonly") 
        entry_d.config(state="readonly")
    #
    def e_c (event) :
        entry_a.config(state="readonly") # baraye taghiir estefade mishe 
        entry_b.config(state="readonly") 
        entry_c.config(state=NORMAL) 
        entry_d.config(state="readonly")
    #
    def e_d (event) :
        entry_a.config(state="readonly") # baraye taghiir estefade mishe 
        entry_b.config(state="readonly") 
        entry_c.config(state="readonly") 
        entry_d.config(state=NORMAL)
    #
    #
    def calculator () : 
        win_cal =  Toplevel(win)
        win_cal.title("calculator")
        win_cal.geometry("400x500")  
        win_cal.resizable(False,False)
        
        def number (x) :
            index = len(entry_1.get()) # agar in nabashe tartibe neveshtan kharab mishe 
            entry_1.insert(index , x) # tosh minevice
        
        def equal () :
            data = entry_1.get()
            result = (eval(data))  # in tabe negah mikone bebine chie hesab kone vorody ham str migire  va tartibe amliat ham dare 
            entry_1.delete(0,END)
            entry_1.insert(0,result) # avaly index / dovomy chizy ke baiad insert beshe 
        
        def clear () :
            entry_1.delete(0,END)

        def sin () : 
            need = int(entry_1.get())
            result_2 = np.sin(need * np.pi/180)
            entry_1.delete(0,END)
            entry_1.insert(0,result_2)
            
        def cos () : 
            need = int(entry_1.get())
            result_2 = np.cos(need * np.pi/180)
            entry_1.delete(0,END)
            entry_1.insert(0,result_2)
        #
        l = Label(win_cal,bg="#00C9FF",width=100,height=100)
        l.place(x=0,y=0)

        entry_1 = Entry(win_cal,foreground="black",background="white",relief=SUNKEN,font=("Rackwell",30,"bold"))
        entry_1.place(x=18,y=18,width=360,height=60)
        #
        b_plus = Button(win_cal,text="+",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="+":number(a))
        b_plus.place(x=350,y=340)
        #
        b_minus = Button(win_cal,text="_",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="-":number(a))
        b_minus.place(x=350,y=245)
        #
        #
        b_times = Button(win_cal,text="X",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="*":number(a))
        b_times.place(x=350,y=180)
        #
        #
        b_division = Button(win_cal,text="/",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),width=1,height=1,command=lambda a="/":number(a))
        b_division.place(x=350,y=80)
        #
        #
        b_clear = Button(win_cal ,text="c",foreground="#212F3C",background="white",activebackground="red",relief=RAISED,font=("Microsoft",22),width=9,height=1,command=clear)
        b_clear.place(x=6,y=439)
        #
        b_equal = Button(win_cal ,text="=",foreground="red",background="white",activebackground="yellow",relief=RAISED,font=("Microsoft",22),width=12,height=1,command=equal)
        b_equal.place(x=180,y=439)
        #
        b_1 = Button(win_cal,image=im1,activebackground="#00C9FF",relief=FLAT,bg="#00C9FF",command=lambda a=1:number(a))
        b_1.place(x=40,y=270)
        #
        b_2 = Button(win_cal,relief=FLAT,activebackground="#00C9FF", image=im2,bg="#00C9FF",command=lambda a=2:number(a))
        b_2.place(x=130,y=270)
        #
        b_3 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im3,bg="#00C9FF",command=lambda a=3:number(a))
        b_3.place(x=220,y=270)
        #
        b_4 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im4,bg="#00C9FF",command=lambda a=4:number(a))
        b_4.place(x=40,y=180)
        #
        b_5 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im5,bg="#00C9FF",command=lambda a=5:number(a))
        b_5.place(x=130,y=180)
        #
        b_6 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im6,bg="#00C9FF",command=lambda a=6:number(a))
        b_6.place(x=220,y=180)
        #
        b_7 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im7,bg="#00C9FF",command=lambda a=7:number(a))
        b_7.place(x=40,y=90)
        #
        b_8 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im8,bg="#00C9FF",command=lambda a=8:number(a))
        b_8.place(x=130,y=90)
        #
        b_9 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im9,bg="#00C9FF" ,command=lambda a=9:number(a))
        b_9.place(x=220,y=90)
        #
        b_0 = Button(win_cal,relief=FLAT,activebackground="#00C9FF", image=im0,bg="#00C9FF",command=lambda a=0:number(a))
        b_0.place(x=130,y=360)
        #
        b_sin = Button(win_cal,text="sin",foreground="black",background="white",activebackground="#00C9FF",relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",22),height=1,width=4,command=sin)
        b_sin.place(x=45,y=362)
        #
        b_cos = Button(win_cal,text="cos",foreground="black",background="white",activebackground="#00C9FF",relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",22),height=1,width=4,command=cos)
        b_cos.place(x=225,y=362)

        win_cal.mainloop()

###########################################
    label_all = Label(win,text="     x³+     x²+    x+    ",font=("Tw Cen MT Condensed Extra Bold",50),foreground="#00A6FF",bg="white")
    label_all.place(x=20,y=10)
    label_a = Label(win,image=im_square,width=60,height=60,background="white")
    label_a.place(x=28,y=20)
    label_b = Label(win,image=im_square,width=60,height=60,background="white")
    label_b.place(x=212,y=20)
    label_c = Label(win,image=im_square,width=60,height=60,background="white")
    label_c.place(x=378,y=20)
    label_d = Label(win,image=im_square,width=60,height=60,background="white")
    label_d.place(x=518,y=20)
    #
    #
    entry_a = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_a.place(x=31,y=23,width=55,height=55)
    entry_a.bind("<Button-1>",e_a)

    entry_b = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_b.place(x=217,y=23,width=55,height=55)
    entry_b.bind("<Button-1>",e_b)

    entry_c = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_c.place(x=381,y=23,width=55,height=55)
    entry_c.bind("<Button-1>",e_c)

    entry_d = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_d.place(x=521,y=23,width=55,height=55)
    entry_d.bind("<Button-1>",e_d)
    #
    answer_entry = Entry(win,font=("Rackwell",19),foreground="#00C9FF",relief=SUNKEN,width=28)
    answer_entry.place(x=6,y=434,height=56)
    answer_entry.insert(0, " your answer will be shown here")
################################
    frame_1 = Frame(win,width=90,height=500,bg="#00D4FF")
    frame_1.pack(side=RIGHT,fill=Y)
    #
    b_clear = Button(win ,text="c",foreground="white",background="#00A6FF",activebackground="sky blue",relief=FLAT,font=("Microsoft",22,"bold"),width=8,height=1,command=clear)
    b_clear.place(x=6,y=270)
    # 
    b_submit = Button(win ,text="submit",foreground="white",background="#00A6FF",activebackground="sky blue",relief=FLAT,font=("Microsoft",22,"bold"),width=10,height=1,command=equal)
    b_submit.place(x=6,y=340)
    #
    b_1 = Button(win ,relief=FLAT,command=lambda a=1:number(a),image=n_1)
    b_1.place(x=320,y=335)
    #
    b_2 = Button(win,relief=FLAT,command=lambda a=2:number(a),image=n_2)
    b_2.place(x=410,y=335)
    #
    b_3 = Button(win,relief=FLAT,command=lambda a=3:number(a),image=n_3)
    b_3.place(x=500,y=335)
    #
    b_4 = Button(win ,relief=FLAT,command=lambda a=4:number(a),image=n_4)
    b_4.place(x=320,y=245)
    #
    b_5 = Button(win ,relief=FLAT,command=lambda a=5:number(a),image=n_5)
    b_5.place(x=410,y=245)
    #
    b_6 = Button(win ,relief=FLAT,command=lambda a=6:number(a),image=n_6)
    b_6.place(x=500,y=245)
    #
    b_7 = Button(win ,relief=FLAT,command=lambda a=7:number(a),image=n_7)
    b_7.place(x=320,y=155)
    #
    b_8 = Button(win ,relief=FLAT,command=lambda a=8:number(a),image=n_8)
    b_8.place(x=410,y=155)
    #
    b_9 = Button(win ,relief=FLAT,command=lambda a=9:number(a),image=n_9)
    b_9.place(x=500,y=155)
    #
    b_0 = Button(win ,relief=FLAT,command=lambda a=0:number(a),image=n_0)
    b_0.place(x=410,y=425)
    #
    b_m = Button(win,image=n_m,relief=FLAT,command=lambda a="-":number(a))
    b_m.place(x=500,y=425) # 380 390
    #
    b_study = Button(frame_1,command=practice,image=n_s,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_study.pack(pady=15,padx=10)
    #
    b_learning = Button(frame_1,command=learn,image=n_l,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_learning.pack(pady=15)
    #
    b_me= Button(frame_1,command=b_me,image=n_me,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_me.pack(pady = 15)
    #
    b_cal = Button(frame_1,command=calculator,image=im_cal,relief=FLAT,bg="#00D4FF",activebackground="#00D4FF")
    b_cal.pack(pady=15)
    #
    b_exit = Button(frame_1,command=exit,image=im_exit,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_exit.pack(pady=15)
    #
    win.mainloop()



lst = []
lst_f = []
lst_x = []
lst_y = []

def b_2_equation () : 

    win_ask.destroy()
    win = Tk()
    win.geometry("700x500")
    win.title("equation")
    win.resizable(False,False)
    cnv1 = Canvas(win)
    # images 
    n_0 = PhotoImage(file=r"C:\Program Files\masscal\zero.png")
    n_1 = PhotoImage(file=r"C:\Program Files\masscal\number-1.png")
    n_2 = PhotoImage(file=r"C:\Program Files\masscal\two.png")
    n_3 = PhotoImage(file=r"C:\Program Files\masscal\three.png")
    n_4 = PhotoImage(file=r"C:\Program Files\masscal\four.png")
    n_5 = PhotoImage(file=r"C:\Program Files\masscal\five.png")
    n_6 = PhotoImage(file=r"C:\Program Files\masscal\six.png")
    n_7 = PhotoImage(file=r"C:\Program Files\masscal\seven.png")
    n_8 = PhotoImage(file=r"C:\Program Files\masscal\eight.png")
    n_9 = PhotoImage(file=r"C:\Program Files\masscal\nine.png")
    n_m = PhotoImage(file=r"C:\Program Files\masscal\minus.png")
    n_s = PhotoImage(file=r"C:\Program Files\masscal\study.png")
    n_l = PhotoImage(file=r"C:\Program Files\masscal\education.png")
    n_me = PhotoImage(file=r"C:\Program Files\masscal\hacker.png")
    im_me = PhotoImage(file=r"C:\Program Files\masscal\instagram.png")
    im_me2 = PhotoImage(file=r"C:\Program Files\masscal\telegram.png")
    im_exit = PhotoImage(file=r"C:\Program Files\masscal\exit.png")
    im_square = PhotoImage(file=r"C:\Program Files\masscal\square (2).png")
    im_error = PhotoImage(file=r"C:\Program Files\masscal\computer.png")
    im_instagram_id = PhotoImage(file=r"C:\Program Files\masscal\instagram_id.png")
    im_telegram_id = PhotoImage(file=r"C:\Program Files\masscal\telegram_id.png")
    im_practice = PhotoImage(file=r"C:\Program Files\masscal\2x_exces.png")
    im_learning = PhotoImage(file=r"C:\Program Files\masscal\equation_teaching.png")
    im_cal = PhotoImage(file=r"C:\Program Files\masscal\calculator.png")
    im1 = PhotoImage(file=r"C:\Program Files\masscal\one.png")
    im2 = PhotoImage(file=r"C:\Program Files\masscal\number-2.png")
    im3 = PhotoImage(file=r"C:\Program Files\masscal\number-3.png")
    im4 = PhotoImage(file=r"C:\Program Files\masscal\number-4.png")
    im5 = PhotoImage(file=r"C:\Program Files\masscal\number-5.png")
    im6 = PhotoImage(file=r"C:\Program Files\masscal\number-six.png")
    im7 = PhotoImage(file=r"C:\Program Files\masscal\number-7.png")
    im8 = PhotoImage(file=r"C:\Program Files\masscal\number-8.png")
    im9 = PhotoImage(file=r"C:\Program Files\masscal\number-9.png")
    im0 = PhotoImage(file=r"C:\Program Files\masscal\number-zero.png")
    # ------------------------------------------ 
    def number (x) :
        if entry_a["state"] == "normal" : 
            index = len(entry_a.get()) 
            entry_a.insert(index , x)

        if entry_b["state"] == "normal" : 
            index = len(entry_b.get()) 
            entry_b.insert(index , x)

        if entry_c["state"] == "normal" : 
            index = len(entry_c.get()) 
            entry_c.insert(index , x)

    def clear () :
        entry_a.delete(0,END)
        entry_b.delete(0,END)
        entry_c.delete(0,END)
    
    #
    def help() :
        new_win = Toplevel(win)
        new_win.geometry("450x250")
        label_1 = Label(new_win,image=n_label)
        label_1.place(x=0,y=0) 
    #
    def learn () : 
        win_teach = Toplevel(win)
        win_teach.geometry("602x580")
        win_teach.resizable(False,False)
        label_teach = Label(win_teach,image=im_learning)
        label_teach.place(x=0,y=0)
    #
    def b_me () : 
        def b_tel () : 
            telegram = Toplevel()
            telegram.geometry("530x90")
            telegram.title("TELEGRAM")
            ins_id = Label(telegram,image=im_telegram_id,bg="white")
            ins_id.place(x=0,y=0)

        def b_instagram () :
            instagram = Toplevel()
            instagram.geometry("560x120") 
            instagram.title("INSTAGRAM")
            ins_id = Label(instagram,image=im_instagram_id,bg="white")
            ins_id.place(x=0,y=0)

        win_about_me = Toplevel()
        win_about_me.geometry("550x300")
        win_about_me.title("About Me")
        l_1 = Label(win_about_me,background="#00FFAE",height=500,width=800)
        l_1.place(x=0,y=0)
        l_2 = Label(win_about_me,background="#00FFAE",foreground="white",font=("Tw Cen MT Condensed Extra Bold",27),text=" Hello again\n Thank you for choosing my app\n  My name is Parham Beiraghdar\n  you can contact me using these ways",)
        l_2.place(x=0,y=0)
        b_instagram = Button(win_about_me,command=b_instagram,image=im_me,relief=FLAT,background="#00FFAE",activebackground="#00FFAE")
        b_instagram.place(x=170,y=230)
        b_telegram = Button(win_about_me,command=b_tel,image=im_me2,relief=FLAT,background="#00FFAE",activebackground="#00FFAE")
        b_telegram.place(x=270,y=230)
    #
    def practice () : 
        practice_win = Toplevel()
        practice_win.title("PRACTICE TIME ")
        practice_win.geometry("600x700")
        l_examples = Label(practice_win,image=im_practice)
        l_examples.place(x=0,y=0)
    #
    def exit () : 
        win.destroy()
    #
    def equal () :
        try : 
            a = int(entry_a.get())
            b = int(entry_b.get())
            c = int(entry_c.get())
            x = s.symbols("x")
            expr = a*x**2 + b*x + c 
            sol = s.solve(expr,x)
            answer_entry.delete(0,END)
            answer_entry.insert(0,sol)
            # answer_len = len(sol)
            # size = int(answer_len)*350
            # answer_win = Toplevel()
            # answer_win.geometry(f"{size}x100")
            # answer_fill_label = Label(answer_win,bg="#0078FF",height=300,width=300)
            # answer_label = Label(answer_win,font=("Rackwell",20,"bold"),bg="#00C9FF",foreground="white",text=f"your answer is : {sol}")
            # answer_fill_label.place(x=0,y=0)
            # answer_label.place(x=20,y=20,height=60)
            new_win1 = Toplevel()
            new_win1.geometry("600x160")

            def yes_button () :
                for item in range(-15,15):
                    lst_x.append(item)
                    y = a*item**2 + b*item + c 
                    lst_y.append(y)
                x = np.array(lst_x)
                y = np.array(lst_y)
                rounded_sol = [round(item) for item in sol]
                if len(rounded_sol) == 1 : 
                    plt.scatter(rounded_sol,0, color="red", marker="o", label="Intersection Points")
                if len(rounded_sol) == 2 : 
                    plt.scatter(rounded_sol,[0,0], color="red", marker="o", label="Intersection Points")
                plt.axhline(0, color="black", linewidth=3)
                plt.axvline(0, color="black", linewidth=3)
                plt.xlabel("X-axis")
                plt.ylabel("Y-axis")
                plt.plot(x,y)
                plt.legend()
                plt.grid()
                plt.show()
                lst_y.clear()
                lst_x.clear()

            def no_button () :
                new_win1.destroy()

            label_1=Label(new_win1,text="Do you want to see the chart as well ? ",background="#00FF9E",foreground="white",font=("Microsaft",20,"bold"))
            label_1.place(x=44,y=10,height=80,width=520)
            b_1 = ttk.Button(new_win1,text="YES please",command=yes_button)
            b_2 = ttk.Button(new_win1,text="NO thanks",command=no_button)
            b_1.place(x=360,y=110)
            b_2.place(x=160,y=110)
    
        except :
            error_win = Toplevel(win)
            error_win.geometry("260x260")
            error_label = Label(error_win,image=im_error,bg="#FFD1D1")
            error_label.place(x=0,y=0)
    # 
    def e_a (event) : 
        entry_a.config(state=NORMAL) # baraye taghiir estefade mishe 
        entry_b.config(state="readonly") 
        entry_c.config(state="readonly") 
    #
    def e_b (event) :
        entry_a.config(state="readonly") # baraye taghiir estefade mishe 
        entry_b.config(state=NORMAL) 
        entry_c.config(state="readonly") 
    #
    def e_c (event) :
        entry_a.config(state="readonly") # baraye taghiir estefade mishe 
        entry_b.config(state="readonly") 
        entry_c.config(state=NORMAL) 
    #
    def calculator () : 
        win_cal =  Toplevel(win)
        win_cal.title("calculator")
        win_cal.geometry("400x500")  
        win_cal.resizable(False,False)
        
        def number (x) :
            index = len(entry_1.get()) # agar in nabashe tartibe neveshtan kharab mishe 
            entry_1.insert(index , x) # tosh minevice
        
        def equal () :
            data = entry_1.get()
            result = (eval(data))  # in tabe negah mikone bebine chie hesab kone vorody ham str migire  va tartibe amliat ham dare 
            entry_1.delete(0,END)
            entry_1.insert(0,result) # avaly index / dovomy chizy ke baiad insert beshe 
        
        def clear () :
            entry_1.delete(0,END)

        def sin () : 
            need = int(entry_1.get())
            result_2 = np.sin(need * np.pi/180)
            entry_1.delete(0,END)
            entry_1.insert(0,result_2)
            
        def cos () : 
            need = int(entry_1.get())
            result_2 = np.cos(need * np.pi/180)
            entry_1.delete(0,END)
            entry_1.insert(0,result_2)
        #
        l = Label(win_cal,bg="#00C9FF",width=100,height=100)
        l.place(x=0,y=0)

        entry_1 = Entry(win_cal,foreground="black",background="white",relief=SUNKEN,font=("Rackwell",30,"bold"))
        entry_1.place(x=18,y=18,width=360,height=60)
        #
        b_plus = Button(win_cal,text="+",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="+":number(a))
        b_plus.place(x=350,y=340)
        #
        b_minus = Button(win_cal,text="_",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="-":number(a))
        b_minus.place(x=350,y=245)
        #
        #
        b_times = Button(win_cal,text="X",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="*":number(a))
        b_times.place(x=350,y=180)
        #
        #
        b_division = Button(win_cal,text="/",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),width=1,height=1,command=lambda a="/":number(a))
        b_division.place(x=350,y=80)
        #
        #
        b_clear = Button(win_cal ,text="c",foreground="#212F3C",background="white",activebackground="red",relief=RAISED,font=("Microsoft",22),width=9,height=1,command=clear)
        b_clear.place(x=6,y=439)
        #
        b_equal = Button(win_cal ,text="=",foreground="red",background="white",activebackground="yellow",relief=RAISED,font=("Microsoft",22),width=12,height=1,command=equal)
        b_equal.place(x=180,y=439)
        #
        b_1 = Button(win_cal,image=im1,activebackground="#00C9FF",relief=FLAT,bg="#00C9FF",command=lambda a=1:number(a))
        b_1.place(x=40,y=270)
        #
        b_2 = Button(win_cal,relief=FLAT,activebackground="#00C9FF", image=im2,bg="#00C9FF",command=lambda a=2:number(a))
        b_2.place(x=130,y=270)
        #
        b_3 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im3,bg="#00C9FF",command=lambda a=3:number(a))
        b_3.place(x=220,y=270)
        #
        b_4 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im4,bg="#00C9FF",command=lambda a=4:number(a))
        b_4.place(x=40,y=180)
        #
        b_5 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im5,bg="#00C9FF",command=lambda a=5:number(a))
        b_5.place(x=130,y=180)
        #
        b_6 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im6,bg="#00C9FF",command=lambda a=6:number(a))
        b_6.place(x=220,y=180)
        #
        b_7 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im7,bg="#00C9FF",command=lambda a=7:number(a))
        b_7.place(x=40,y=90)
        #
        b_8 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im8,bg="#00C9FF",command=lambda a=8:number(a))
        b_8.place(x=130,y=90)
        #
        b_9 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im9,bg="#00C9FF" ,command=lambda a=9:number(a))
        b_9.place(x=220,y=90)
        #
        b_0 = Button(win_cal,relief=FLAT,activebackground="#00C9FF", image=im0,bg="#00C9FF",command=lambda a=0:number(a))
        b_0.place(x=130,y=360)
        #
        b_sin = Button(win_cal,text="sin",foreground="black",background="white",activebackground="#00C9FF",relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",22),height=1,width=4,command=sin)
        b_sin.place(x=45,y=362)
        #
        b_cos = Button(win_cal,text="cos",foreground="black",background="white",activebackground="#00C9FF",relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",22),height=1,width=4,command=cos)
        b_cos.place(x=225,y=362)

        win_cal.mainloop()
     
##########################################
    label_all = Label(win,text="     x² +     x +     ",font=("Tw Cen MT Condensed Extra Bold",50),foreground="#00A6FF",bg="white")
    label_all.place(x=90,y=10)
    label_a = Label(win,image=im_square,width=60,height=60,background="white")
    label_a.place(x=100,y=20)
    label_b = Label(win,image=im_square,width=60,height=60,background="white")
    label_b.place(x=295,y=20)
    label_c = Label(win,image=im_square,width=60,height=60,background="white")
    label_c.place(x=470,y=20)
    #
    #
    entry_a = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_a.place(x=103,y=23,width=55,height=55)
    entry_a.bind("<Button-1>",e_a)

    entry_b = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_b.place(x=298,y=23,width=55,height=55)
    entry_b.bind("<Button-1>",e_b)

    entry_c = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_c.place(x=473,y=23,width=55,height=55)
    entry_c.bind("<Button-1>",e_c)
    #

    answer_entry = Entry(win,font=("Rackwell",19),foreground="#00C9FF",relief=SUNKEN,width=28)
    answer_entry.place(x=6,y=434,height=56)
    answer_entry.insert(0, " your answer will be shown here")


    ###############
    # label_3 = Label(win,bg = "#00FFFB",width=1,height=500)
    # label_3.place(x=721,y=0)
    # #
    # label_4 = Label(win,bg = "#00D4FF",width=10,height=500)
    # label_4.place(x=724,y=0)
    # #
    # label_5 = Label(win,bg = "#00FFFB",width=1,height=500)
    # label_5.place(x=796,y=0)
    #
    frame_1 = Frame(win,width=90,height=500,bg="#00D4FF")
    frame_1.pack(side=RIGHT,fill=Y)
    #
    b_clear = Button(win ,text="c",foreground="white",background="#00A6FF",activebackground="sky blue",relief=FLAT,font=("Microsoft",22,"bold"),width=8,height=1,command=clear)
    b_clear.place(x=6,y=270)
    # 
    b_submit = Button(win ,text="submit",foreground="white",background="#00A6FF",activebackground="sky blue",relief=FLAT,font=("Microsoft",22,"bold"),width=10,height=1,command=equal)
    b_submit.place(x=6,y=340)
    #
    b_1 = Button(win ,relief=FLAT,command=lambda a=1:number(a),image=n_1)
    b_1.place(x=320,y=335)
    #
    b_2 = Button(win,relief=FLAT,command=lambda a=2:number(a),image=n_2)
    b_2.place(x=410,y=335)
    #
    b_3 = Button(win,relief=FLAT,command=lambda a=3:number(a),image=n_3)
    b_3.place(x=500,y=335)
    #
    b_4 = Button(win ,relief=FLAT,command=lambda a=4:number(a),image=n_4)
    b_4.place(x=320,y=245)
    #
    b_5 = Button(win ,relief=FLAT,command=lambda a=5:number(a),image=n_5)
    b_5.place(x=410,y=245)
    #
    b_6 = Button(win ,relief=FLAT,command=lambda a=6:number(a),image=n_6)
    b_6.place(x=500,y=245)
    #
    b_7 = Button(win ,relief=FLAT,command=lambda a=7:number(a),image=n_7)
    b_7.place(x=320,y=155)
    #
    b_8 = Button(win ,relief=FLAT,command=lambda a=8:number(a),image=n_8)
    b_8.place(x=410,y=155)
    #
    b_9 = Button(win ,relief=FLAT,command=lambda a=9:number(a),image=n_9)
    b_9.place(x=500,y=155)
    #
    b_0 = Button(win ,relief=FLAT,command=lambda a=0:number(a),image=n_0)
    b_0.place(x=410,y=425)
    #
    # b_h = Button(win ,relief=FLAT,command=lambda a="#":number(a),image=n_h)
    # b_h.place(x=320,y=425)
    #
    # b_c = Button(win,image=n_c,relief=FLAT,command=lambda a="y":cal_icon(a))
    # b_c.place(x=530,y=170)
    #
    b_m = Button(win,image=n_m,relief=FLAT,command=lambda a="-":number(a))
    b_m.place(x=500,y=425) # 380 390
    #
    b_study = Button(frame_1,command=practice,image=n_s,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_study.pack(pady=15,padx=10)
    #
    b_learning = Button(frame_1,command=learn,image=n_l,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_learning.pack(pady=15)
    #
    b_me= Button(frame_1,command=b_me,image=n_me,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_me.pack(pady = 15)
    #
    b_cal = Button(frame_1,command=calculator,image=im_cal,relief=FLAT,bg="#00D4FF",activebackground="#00D4FF")
    b_cal.pack(pady=15)
    #
    b_exit = Button(frame_1,command=exit,image=im_exit,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_exit.pack(pady=15)
    #
    win.mainloop()


########################################################
########################################################
########################################################
########################################################
lst = []
lst_f = []
lst_x = []
lst_y = []

def b_info_function () : 
    info_label_image = PhotoImage(file=r"C:\Program Files\masscal\info_label.png")
    win_info = Toplevel()
    win_info.geometry("878x195") 
    win_info.resizable(False,False)
    win_info.title("How to use ?")
    info_page = Label(win_info,image=info_label_image,bg="white")
    info_page.place(x=0,y=0)
    win_info.mainloop()



def b_1_equation () : 

    win_ask.destroy()
    win = Tk()
    win.geometry("700x500")
    win.title("equation")
    win.resizable(False,False)
    cnv1 = Canvas(win)
    # images 
    n_0 = PhotoImage(file=r"C:\Program Files\masscal\zero.png")
    n_1 = PhotoImage(file=r"C:\Program Files\masscal\number-1.png")
    n_2 = PhotoImage(file=r"C:\Program Files\masscal\two.png")
    n_3 = PhotoImage(file=r"C:\Program Files\masscal\three.png")
    n_4 = PhotoImage(file=r"C:\Program Files\masscal\four.png")
    n_5 = PhotoImage(file=r"C:\Program Files\masscal\five.png")
    n_6 = PhotoImage(file=r"C:\Program Files\masscal\six.png")
    n_7 = PhotoImage(file=r"C:\Program Files\masscal\seven.png")
    n_8 = PhotoImage(file=r"C:\Program Files\masscal\eight.png")
    n_9 = PhotoImage(file=r"C:\Program Files\masscal\nine.png")
    n_s = PhotoImage(file=r"C:\Program Files\masscal\study.png")
    n_l = PhotoImage(file=r"C:\Program Files\masscal\education.png")
    n_m = PhotoImage(file=r"C:\Program Files\masscal\minus.png")
    n_me = PhotoImage(file=r"C:\Program Files\masscal\hacker.png")
    im_me = PhotoImage(file=r"C:\Program Files\masscal\instagram.png")
    im_me2 = PhotoImage(file=r"C:\Program Files\masscal\telegram.png")
    im_exit = PhotoImage(file=r"C:\Program Files\masscal\exit.png")
    im_square = PhotoImage(file=r"C:\Program Files\masscal\square (2).png")
    im_error = PhotoImage(file=r"C:\Program Files\masscal\computer.png")
    im_instagram_id = PhotoImage(file=r"C:\Program Files\masscal\instagram_id.png")
    im_telegram_id = PhotoImage(file=r"C:\Program Files\masscal\telegram_id.png")
    im_practice = PhotoImage(file=r"C:\Program Files\masscal\1x_exces.png")
    im_learning = PhotoImage(file=r"C:\Program Files\masscal\equation_teaching.png")
    im_learning_1 = PhotoImage(file=r"C:\Program Files\masscal\linear_equation_1.png")
    im_learning_2 = PhotoImage(file=r"C:\Program Files\masscal\linear_equation_2.png")
    im_learning_3 = PhotoImage(file=r"C:\Program Files\masscal\linear_equation_3(2).png")
    im_cal = PhotoImage(file=r"C:\Program Files\masscal\calculator.png")
    im1 = PhotoImage(file=r"C:\Program Files\masscal\one.png")
    im2 = PhotoImage(file=r"C:\Program Files\masscal\number-2.png")
    im3 = PhotoImage(file=r"C:\Program Files\masscal\number-3.png")
    im4 = PhotoImage(file=r"C:\Program Files\masscal\number-4.png")
    im5 = PhotoImage(file=r"C:\Program Files\masscal\number-5.png")
    im6 = PhotoImage(file=r"C:\Program Files\masscal\number-six.png")
    im7 = PhotoImage(file=r"C:\Program Files\masscal\number-7.png")
    im8 = PhotoImage(file=r"C:\Program Files\masscal\number-8.png")
    im9 = PhotoImage(file=r"C:\Program Files\masscal\number-9.png")
    im0 = PhotoImage(file=r"C:\Program Files\masscal\number-zero.png")
    # ------------------------------------------ 
    def number (x) :
        if entry_a["state"] == "normal" : 
            index = len(entry_a.get()) 
            entry_a.insert(index , x)

        if entry_b["state"] == "normal" : 
            index = len(entry_b.get()) 
            entry_b.insert(index , x)

    def clear () :
        entry_a.delete(0,END)
        entry_b.delete(0,END)
    

    #
    def learn () : 
        def b_page3 () : 
            label_teach.configure(image=im_learning_2)

        def b_page2 () : 
            label_teach.configure(image=im_learning_1)
        
        def b_page1 () : 
            label_teach.configure(image=im_learning_3)

        win_teach = Toplevel()
        win_teach.geometry("740x720")
        win_teach.resizable(False,False)
        label_teach = Label(win_teach,image=im_learning_3,bg="black")
        label_teach.place(x=2,y=0)
        b_teach_p1 = Button(win_teach,command=b_page1,relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",25),bg="#C984FF",foreground="white",text="page 1")
        b_teach_p2 = Button(win_teach,command=b_page2,relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",25),bg="#C984FF",foreground="white",text="page 2")
        b_teach_p3 = Button(win_teach,command=b_page3,relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",25),bg="#C984FF",foreground="white",text="page 3")
        b_teach_p1.place(x=170,y=630)
        b_teach_p2.place(x=320,y=630)
        b_teach_p3.place(x=470,y=630)

    #
    def b_me () : 
        def b_tel () : 
            telegram = Toplevel()
            telegram.geometry("530x90")
            telegram.title("TELEGRAM")
            ins_id = Label(telegram,image=im_telegram_id,bg="white")
            ins_id.place(x=0,y=0)

        def b_instagram () :
            instagram = Toplevel()
            instagram.geometry("560x120") 
            instagram.title("INSTAGRAM")
            ins_id = Label(instagram,image=im_instagram_id,bg="white")
            ins_id.place(x=0,y=0)

        win_about_me = Toplevel()
        win_about_me.geometry("550x300")
        win_about_me.title("About Me")
        l_1 = Label(win_about_me,background="#00FFAE",height=500,width=800)
        l_1.place(x=0,y=0)
        l_2 = Label(win_about_me,background="#00FFAE",foreground="white",font=("Tw Cen MT Condensed Extra Bold",27),text=" Hello again\n Thank you for choosing my app\n  My name is Parham Beiraghdar\n  you can contact me using these ways",)
        l_2.place(x=0,y=0)
        b_instagram = Button(win_about_me,command=b_instagram,image=im_me,relief=FLAT,background="#00FFAE",activebackground="#00FFAE")
        b_instagram.place(x=170,y=230)
        b_telegram = Button(win_about_me,command=b_tel,image=im_me2,relief=FLAT,background="#00FFAE",activebackground="#00FFAE")
        b_telegram.place(x=270,y=230)
    #
    def practice () : 
        practice_win = Toplevel()
        practice_win.title("PRACTICE TIME ")
        practice_win.geometry("600x730")
        l_examples = Label(practice_win,image=im_practice)
        l_examples.place(x=0,y=0)
    #
    def exit () : 
        win.destroy()
    #
    def equal () :
        try : 
            a = int(entry_a.get())
            b = int(entry_b.get())
            x = s.symbols("x")
            expr = a*x + b 
            sol = s.solve(expr,x)
            answer_entry.delete(0,END)
            answer_entry.insert(0,sol)
            new_win1 = Toplevel()
            new_win1.geometry("600x160")

            def yes_button () :
                for item in range(-15,15):
                    lst_x.append(item)
                    y = a*item + b 
                    lst_y.append(y)
                x = np.array(lst_x)
                y = np.array(lst_y)
                plt.scatter(sol,0,color="red", marker="o", label="Intersection Points")
                plt.axhline(0, color="black", linewidth=2)
                plt.axvline(0, color="black", linewidth=2)
                plt.xlabel("X-axis")
                plt.ylabel("Y-axis")
                plt.plot(x,y)
                plt.legend()
                plt.grid()
                plt.show()
                lst_y.clear()
                lst_x.clear()

            def no_button () :
                new_win1.destroy()

            label_1=Label(new_win1,text="Do you want to see the chart as well ? ",background="#00FF9E",foreground="white",font=("Microsaft",20,"bold"))
            label_1.place(x=44,y=10,height=80,width=520)
            b_1 = ttk.Button(new_win1,text="YES please",command=yes_button)
            b_2 = ttk.Button(new_win1,text="NO thanks",command=no_button)
            b_1.place(x=360,y=110)
            b_2.place(x=160,y=110)
    
        except :
            error_win = Toplevel(win)
            error_win.geometry("260x260")
            error_label = Label(error_win,image=im_error,bg="#FFD1D1")
            error_label.place(x=0,y=0)
    # 
    def e_a (event) : 
        entry_a.config(state=NORMAL) # baraye taghiir estefade mishe 
        entry_b.config(state="readonly") 
        # entry_c.config(state="readonly") 
    #
    def e_b (event) :
        entry_a.config(state="readonly") # baraye taghiir estefade mishe 
        entry_b.config(state=NORMAL) 
        # entry_c.config(state="readonly") 
    # 
    def calculator () : 
        win_cal =  Toplevel(win)
        win_cal.title("calculator")
        win_cal.geometry("400x500")  
        win_cal.resizable(False,False)
        
        def number (x) :
            index = len(entry_1.get()) # agar in nabashe tartibe neveshtan kharab mishe 
            entry_1.insert(index , x) # tosh minevice
        
        def equal () :
            data = entry_1.get()
            result = (eval(data))  # in tabe negah mikone bebine chie hesab kone vorody ham str migire  va tartibe amliat ham dare 
            entry_1.delete(0,END)
            entry_1.insert(0,result) # avaly index / dovomy chizy ke baiad insert beshe 
        
        def clear () :
            entry_1.delete(0,END)

        def sin () : 
            need = int(entry_1.get())
            result_2 = np.sin(need * np.pi/180)
            entry_1.delete(0,END)
            entry_1.insert(0,result_2)
            
        def cos () : 
            need = int(entry_1.get())
            result_2 = np.cos(need * np.pi/180)
            entry_1.delete(0,END)
            entry_1.insert(0,result_2)
        #
        l = Label(win_cal,bg="#00C9FF",width=100,height=100)
        l.place(x=0,y=0)

        entry_1 = Entry(win_cal,foreground="black",background="white",relief=SUNKEN,font=("Rackwell",30,"bold"))
        entry_1.place(x=18,y=18,width=360,height=60)
        #
        b_plus = Button(win_cal,text="+",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="+":number(a))
        b_plus.place(x=350,y=340)
        #
        b_minus = Button(win_cal,text="_",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="-":number(a))
        b_minus.place(x=350,y=245)
        #
        #
        b_times = Button(win_cal,text="X",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),height=1,width=1,command=lambda a="*":number(a))
        b_times.place(x=350,y=180)
        #
        #
        b_division = Button(win_cal,text="/",foreground="white",background="#00C9FF",activebackground="#00C9FF",relief=FLAT,font=("Tw Cen MT Condensed Extra Bold",40),width=1,height=1,command=lambda a="/":number(a))
        b_division.place(x=350,y=80)
        #
        #
        b_clear = Button(win_cal ,text="c",foreground="#212F3C",background="white",activebackground="red",relief=RAISED,font=("Microsoft",22),width=9,height=1,command=clear)
        b_clear.place(x=6,y=439)
        #
        b_equal = Button(win_cal ,text="=",foreground="red",background="white",activebackground="yellow",relief=RAISED,font=("Microsoft",22),width=12,height=1,command=equal)
        b_equal.place(x=180,y=439)
        #
        b_1 = Button(win_cal,image=im1,activebackground="#00C9FF",relief=FLAT,bg="#00C9FF",command=lambda a=1:number(a))
        b_1.place(x=40,y=270)
        #
        b_2 = Button(win_cal,relief=FLAT,activebackground="#00C9FF", image=im2,bg="#00C9FF",command=lambda a=2:number(a))
        b_2.place(x=130,y=270)
        #
        b_3 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im3,bg="#00C9FF",command=lambda a=3:number(a))
        b_3.place(x=220,y=270)
        #
        b_4 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im4,bg="#00C9FF",command=lambda a=4:number(a))
        b_4.place(x=40,y=180)
        #
        b_5 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im5,bg="#00C9FF",command=lambda a=5:number(a))
        b_5.place(x=130,y=180)
        #
        b_6 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im6,bg="#00C9FF",command=lambda a=6:number(a))
        b_6.place(x=220,y=180)
        #
        b_7 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im7,bg="#00C9FF",command=lambda a=7:number(a))
        b_7.place(x=40,y=90)
        #
        b_8 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im8,bg="#00C9FF",command=lambda a=8:number(a))
        b_8.place(x=130,y=90)
        #
        b_9 = Button(win_cal,relief=FLAT,activebackground="#00C9FF",image=im9,bg="#00C9FF" ,command=lambda a=9:number(a))
        b_9.place(x=220,y=90)
        #
        b_0 = Button(win_cal,relief=FLAT,activebackground="#00C9FF", image=im0,bg="#00C9FF",command=lambda a=0:number(a))
        b_0.place(x=130,y=360)
        #
        b_sin = Button(win_cal,text="sin",foreground="black",background="white",activebackground="#00C9FF",relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",22),height=1,width=4,command=sin)
        b_sin.place(x=45,y=362)
        #
        b_cos = Button(win_cal,text="cos",foreground="black",background="white",activebackground="#00C9FF",relief=RAISED,font=("Tw Cen MT Condensed Extra Bold",22),height=1,width=4,command=cos)
        b_cos.place(x=225,y=362)

        win_cal.mainloop()


     
##########################################
    label_all = Label(win,text="        x +       ",font=("Tw Cen MT Condensed Extra Bold",50),foreground="#00A6FF",bg="white")
    label_all.place(x=150,y=10)
    label_a = Label(win,image=im_square,width=60,height=60,background="white")
    label_a.place(x=180,y=20)
    label_b = Label(win,image=im_square,width=60,height=60,background="white")
    label_b.place(x=405,y=20)
    #
    #
    entry_a = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_a.place(x=185,y=23,width=55,height=55)
    entry_a.bind("<Button-1>",e_a)

    entry_b = Entry(win,state=DISABLED,relief=FLAT,font=("Rackwell",36,"bold"))
    entry_b.place(x=409,y=23,width=55,height=55)
    entry_b.bind("<Button-1>",e_b)
    #
    answer_entry = Entry(win,font=("Rackwell",19),foreground="#00C9FF",relief=SUNKEN,width=28)
    answer_entry.place(x=6,y=434,height=56)
    answer_entry.insert(0, " your answer will be shown here")


    ###############

    frame_1 = Frame(win,width=90,height=500,bg="#00D4FF")
    frame_1.pack(side=RIGHT,fill=Y)
    #
    b_clear = Button(win ,text="c",foreground="white",background="#00A6FF",activebackground="sky blue",relief=FLAT,font=("Microsoft",22,"bold"),width=8,height=1,command=clear)
    b_clear.place(x=6,y=270)
    # 
    b_submit = Button(win ,text="submit",foreground="white",background="#00A6FF",activebackground="sky blue",relief=FLAT,font=("Microsoft",22,"bold"),width=10,height=1,command=equal)
    b_submit.place(x=6,y=340)
    #
    b_1 = Button(win ,relief=FLAT,command=lambda a=1:number(a),image=n_1)
    b_1.place(x=320,y=335)
    #
    b_2 = Button(win,relief=FLAT,command=lambda a=2:number(a),image=n_2)
    b_2.place(x=410,y=335)
    #
    b_3 = Button(win,relief=FLAT,command=lambda a=3:number(a),image=n_3)
    b_3.place(x=500,y=335)
    #
    b_4 = Button(win ,relief=FLAT,command=lambda a=4:number(a),image=n_4)
    b_4.place(x=320,y=245)
    #
    b_5 = Button(win ,relief=FLAT,command=lambda a=5:number(a),image=n_5)
    b_5.place(x=410,y=245)
    #
    b_6 = Button(win ,relief=FLAT,command=lambda a=6:number(a),image=n_6)
    b_6.place(x=500,y=245)
    #
    b_7 = Button(win ,relief=FLAT,command=lambda a=7:number(a),image=n_7)
    b_7.place(x=320,y=155)
    #
    b_8 = Button(win ,relief=FLAT,command=lambda a=8:number(a),image=n_8)
    b_8.place(x=410,y=155)
    #
    b_9 = Button(win ,relief=FLAT,command=lambda a=9:number(a),image=n_9)
    b_9.place(x=500,y=155)
    #
    b_0 = Button(win ,relief=FLAT,command=lambda a=0:number(a),image=n_0)
    b_0.place(x=410,y=425)
    #
    # b_h = Button(win ,relief=FLAT,command=lambda a="#":number(a),image=n_h)
    # b_h.place(x=320,y=425)
    #
    # b_c = Button(win,image=n_c,relief=FLAT,command=lambda a="y":cal_icon(a))
    # b_c.place(x=530,y=170)
    #
    b_m = Button(win,image=n_m,relief=FLAT,command=lambda a="-":number(a))
    b_m.place(x=500,y=425) # 380 390
    #
    b_study = Button(frame_1,command=practice,image=n_s,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_study.pack(pady=15,padx=10)
    #
    b_learning = Button(frame_1,command=learn,image=n_l,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_learning.pack(pady=15)
    #
    b_me= Button(frame_1,command=b_me,image=n_me,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_me.pack(pady = 15)
    #
    b_cal = Button(frame_1,command=calculator,image=im_cal,relief=FLAT,bg="#00D4FF",activebackground="#00D4FF")
    b_cal.pack(pady=15)
    #
    b_exit = Button(frame_1,command=exit,image=im_exit,relief=FLAT,background="#00D4FF",activebackground="#00D4FF")
    b_exit.pack(pady=15)
    #
    win.mainloop()


########################################################

# asking window : 

win_ask = Tk()
win_ask.title("equation solver")
win_ask.geometry("1050x300")
win_ask.resizable(False,False)
cnv1 = Canvas(win_ask)
#
info_image = PhotoImage(file=r"C:\Program Files\masscal\info.png")
#
time = int(time.strftime("%H"))

if time >= 18 and time <= 24  : 
    an = "Good night"

if time >= 0 and time < 12 : 
    an = "Good morning"

if time >= 12 and time < 18 : 
    an = "Good afteroon "

welcome_list = ["Hello","Hi","Hey there","nice to meet you","Hello my friend","Hey what's up ?","Hi how are you ? "]
welcome_text = r.choice(welcome_list)
label_2 = Label(win_ask,background="#00C9FF",height=1400,width=500)
label_2.place(x=0,y=0)
label_1 = Label(win_ask,text=f"{welcome_text}\n{an}\n please let me know which equation do you like to solve or learn ? ",foreground="white",background="#00C9FF",font=("Tw Cen MT Condensed Extra Bold",30))	
label_1.place(x=10,y=10)
# 
b_info = Button(win_ask,command=b_info_function,relief=FLAT,image=info_image)
b_info.place(x=0,y=0)
b_x = Button(win_ask,command=b_1_equation,relief=FLAT,text="linear\nequation",activebackground="#00C9FF",foreground="white",background="#00FF9E",font=("Tw Cen MT Condensed Extra Bold",15),height=2,width=10,activeforeground="white")
b_x2 = Button(win_ask,command=b_2_equation,relief=FLAT,text="Quadratic\nequation",foreground="white",activebackground="#00C9FF",background="#00FF9E",font=("Tw Cen MT Condensed Extra Bold",15),height=2,width=10,activeforeground="white")
b_x3 = Button(win_ask,command=b_3_equation,relief=FLAT,text="cubic\nequation",foreground="white",activebackground="#00C9FF",background="#00FF9E",font=("Tw Cen MT Condensed Extra Bold",15),height=2,width=10,activeforeground="white")
b_x.place(x=200,y=200)
b_x2.place(x=450,y=200)
b_x3.place(x=700,y=200)


win_ask.mainloop()
