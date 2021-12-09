from tkinter import *
from random import *

# لیستی که خانه های انتخابی یوزر در ان ذخیره میشود
user_cells = []
# لیستی که خانه های انتخابی کامپیوتر در ان ذخیره میشود
computer_cells = []

# لیستی دریافت میکند و مشخص میکند که در ان لیست سه سلول دوز تشکیل میشوند یا خیر
class check_win:
    def __init__(self,lst) :
        self.lst = lst
    def win(self) :
        chek_list = []
        for i in [1,2,3] :
            if i in self.lst :
                chek_list.append(True)
            else :
                chek_list.append(False)
        if all(chek_list) == True :
            return True
        else :
            chek_list = []
            for i in [4,5,6] :
                if i in self.lst :
                    chek_list.append(True)
                else :
                    chek_list.append(False)
            if all(chek_list) == True :
                return True
            else :
                chek_list = []
                for i in [7,8,9] :
                    if i in self.lst :
                        chek_list.append(True)
                    else :
                        chek_list.append(False)
                if all(chek_list) == True :
                    return True
                else :
                    chek_list = []
                    for i in [1,4,7] :
                        if i in self.lst :
                            chek_list.append(True)
                        else :
                            chek_list.append(False)
                    if all(chek_list) == True :
                        return True
                    else :
                        chek_list = []
                        for i in [2,5,8] :
                            if i in self.lst :
                                chek_list.append(True)
                            else :
                                chek_list.append(False)
                        if all(chek_list) == True :
                            return True
                        else :
                            chek_list = []
                            for i in [3,6,9] :
                                if i in self.lst :
                                    chek_list.append(True)
                                else :
                                    chek_list.append(False)
                            if all(chek_list) == True :
                                return True
                            else :
                                chek_list = []
                                for i in [1,5,9] :
                                    if i in self.lst :
                                        chek_list.append(True)
                                    else :
                                        chek_list.append(False)
                                if all(chek_list) == True :
                                    return True
                                else :
                                    chek_list = []
                                    for i in [3,5,7] :
                                        if i in self.lst :
                                            chek_list.append(True)
                                        else :
                                            chek_list.append(False)
                                    if all(chek_list) == True :
                                        return True
                                    else :
                                        return False
                                        
window = Tk()

#--------------------------------------------------------
def reset() :
    global user_cells
    global computer_cells

    label_1=Label(window,text="    1    ",bg='dim gray',fg='white')
    label_1.grid(column=0,row=0,sticky=E+W,padx=4,pady=4)
    label_2=Label(window,text="    2    ",bg='dim gray',fg='white')
    label_2.grid(column=1,row=0,sticky=E+W,padx=4,pady=4)
    label_3=Label(window,text="    3    ",bg='dim gray',fg='white')
    label_3.grid(column=2,row=0,sticky=E+W,padx=4,pady=4)
    label_4=Label(window,text="    4    ",bg='dim gray',fg='white')
    label_4.grid(column=0,row=1,sticky=E+W,padx=4,pady=4)
    label_5=Label(window,text="    5    ",bg='dim gray',fg='white')
    label_5.grid(column=1,row=1,sticky=E+W,padx=4,pady=4)
    label_6=Label(window,text="    6    ",bg='dim gray',fg='white')
    label_6.grid(column=2,row=1,sticky=E+W,padx=4,pady=4)
    label_7=Label(window,text="    7    ",bg='dim gray',fg='white')
    label_7.grid(column=0,row=2,sticky=E+W,padx=4,pady=4)
    label_8=Label(window,text="    8    ",bg='dim gray',fg='white')
    label_8.grid(column=1,row=2,sticky=E+W,padx=4,pady=4)
    label_9=Label(window,text="    9    ",bg='dim gray',fg='white')
    label_9.grid(column=2,row=2,sticky=E+W,padx=4,pady=4)

    user_cells = []
    computer_cells = []

    return user_cells , computer_cells
#--------------------------------------------------------
def choose():
    # دکمه چوز یک عدد از کاربر میگیردو بررسی میکند که ان عدد غیر مجاز نباشد و در صورت مجاز بودن خانه ان را ابی میکند
    global entry_user
    global user_cells
    global computer_cells
    result = int(entry_user.get())
    
    if result in user_cells or result in computer_cells :
        label_wrong=Label(window,text='your cells is repeatly :(',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 1 :
        label_1=Label(window,text="    1    ",bg='blue',fg='black')
        label_1.grid(column=0,row=0,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 2 :
        label_2=Label(window,text="    2    ",bg='blue',fg='black')
        label_2.grid(column=1,row=0,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)


    elif result == 3 :
        label_3=Label(window,text="    3    ",bg='blue',fg='black')
        label_3.grid(column=2,row=0,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 4 :
        label_4=Label(window,text="    4    ",bg='blue',fg='black')
        label_4.grid(column=0,row=1,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 5 :
        label_5=Label(window,text="    5    ",bg='blue',fg='black')
        label_5.grid(column=1,row=1,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 6 :
        label_6=Label(window,text="    6    ",bg='blue',fg='black')
        label_6.grid(column=2,row=1,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 7 :
        label_7=Label(window,text="    7    ",bg='blue',fg='black')
        label_7.grid(column=0,row=2,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 8 :
        label_8=Label(window,text="    8    ",bg='blue',fg='black')
        label_8.grid(column=1,row=2,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    elif result == 9 :
        label_9=Label(window,text="    9    ",bg='blue',fg='black')
        label_9.grid(column=2,row=2,sticky=E+W,padx=4,pady=4)
        user_cells.append(result)

        label_wrong=Label(window,text=':)',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

    # اگرعدد غیر مجاز انتخاب کند
    else :
        label_wrong=Label(window,text='your chose is wrong  :(',bg='black',fg='white')
        label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)
    
    # چک کردن برنده شدن کاربر
    chec = check_win(user_cells)
    if chec.win() == True :
        label_user_win=Label(window,text='user win',bg='black',fg='white')
        label_user_win.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)
    
    # اگر کاربر برنده نشده بود
    elif chec.win() == False :
        # اگر کامپیوتر 4 انتخاب کرد دیگر انتخاب پنجم را نکند
        if len(computer_cells) < 5 :
            # یک عدد بین 1 تا 9 انخاب میکند و اگر تکراری بود دوباره انتخاب مکند
            computer_number = randint(1,9)
            while computer_number in user_cells or computer_number in computer_cells :
                computer_number = randint(1,9)
            else :
                computer_cells.append(computer_number)
                if computer_number == 1 :
                    label_1=Label(window,text="    1    ",bg='red',fg='black')
                    label_1.grid(column=0,row=0,sticky=E+W,padx=4,pady=4)

                elif computer_number == 2 :
                    label_2=Label(window,text="    2    ",bg='red',fg='black')
                    label_2.grid(column=1,row=0,sticky=E+W,padx=4,pady=4)

                elif computer_number == 3 :
                    label_3=Label(window,text="    3    ",bg='red',fg='black')
                    label_3.grid(column=2,row=0,sticky=E+W,padx=4,pady=4)

                elif computer_number == 4 :
                    label_4=Label(window,text="    4    ",bg='red',fg='black')
                    label_4.grid(column=0,row=1,sticky=E+W,padx=4,pady=4)

                elif computer_number == 5 :
                    label_5=Label(window,text="    5    ",bg='red',fg='black')
                    label_5.grid(column=1,row=1,sticky=E+W,padx=4,pady=4)

                elif computer_number == 6 :
                    label_6=Label(window,text="    6    ",bg='red',fg='black')
                    label_6.grid(column=2,row=1,sticky=E+W,padx=4,pady=4)

                elif computer_number == 7 :
                    label_7=Label(window,text="    7    ",bg='red',fg='black')
                    label_7.grid(column=0,row=2,sticky=E+W,padx=4,pady=4)

                elif computer_number == 8 :
                    label_8=Label(window,text="    8    ",bg='red',fg='black')
                    label_8.grid(column=1,row=2,sticky=E+W,padx=4,pady=4)

                elif computer_number == 9 :
                    label_9=Label(window,text="    9    ",bg='red',fg='black')
                    label_9.grid(column=2,row=2,sticky=E+W,padx=4,pady=4)

                chec = check_win(computer_cells)
                if chec.win() == True :
                    label_user_win=Label(window,text='computer win',bg='black',fg='white')
                    label_user_win.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

        else :
            label_finish_1=Label(window,text=':(',bg='black',fg='white')
            label_finish_1.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

            label_finish_2=Label(window,text='any one no win',bg='black',fg='white')
            label_finish_2.grid(row=3,column=3,sticky=E+W,padx=6,pady=4)
#--------------------------------------------------------

window.minsize(290,163)
window.maxsize(290,163)
window.title("Made by Ali HajiAli !!!")

# حالت اولیه بازی
label_1=Label(window,text="    1    ",bg='dim gray',fg='white')
label_1.grid(column=0,row=0,sticky=E+W,padx=4,pady=4)
label_2=Label(window,text="    2    ",bg='dim gray',fg='white')
label_2.grid(column=1,row=0,sticky=E+W,padx=4,pady=4)
label_3=Label(window,text="    3    ",bg='dim gray',fg='white')
label_3.grid(column=2,row=0,sticky=E+W,padx=4,pady=4)
label_4=Label(window,text="    4    ",bg='dim gray',fg='white')
label_4.grid(column=0,row=1,sticky=E+W,padx=4,pady=4)
label_5=Label(window,text="    5    ",bg='dim gray',fg='white')
label_5.grid(column=1,row=1,sticky=E+W,padx=4,pady=4)
label_6=Label(window,text="    6    ",bg='dim gray',fg='white')
label_6.grid(column=2,row=1,sticky=E+W,padx=4,pady=4)
label_7=Label(window,text="    7    ",bg='dim gray',fg='white')
label_7.grid(column=0,row=2,sticky=E+W,padx=4,pady=4)
label_8=Label(window,text="    8    ",bg='dim gray',fg='white')
label_8.grid(column=1,row=2,sticky=E+W,padx=4,pady=4)
label_9=Label(window,text="    9    ",bg='dim gray',fg='white')
label_9.grid(column=2,row=2,sticky=E+W,padx=4,pady=4)

label_statement=Label(window,text='please enter your choose : ',bg='pink',fg='blue')
label_statement.grid(column=3,row=0,sticky=E+W,padx=6,pady=4)

label_wrong=Label(window,text=':)',bg='black',fg='white')
label_wrong.grid(column=3,row=2,sticky=E+W,padx=6,pady=4)

entry_user=Entry(window,bg='beige')
entry_user.grid(column=3,row=1,padx=6,pady=4)

label_welcom=Label(window,text='welcome !',bg='pink',fg='blue')
label_welcom.grid(row=3,columnspan=3,sticky=E+W,padx=4,pady=6)

button_choose=Button(window,text='choose',bg='beige',fg='green',command=choose)
button_choose.grid(row=3,column=3,sticky=E+W,padx=4,pady=6)

button_reset=Button(window,text='reset',bg='cyan2',fg='green',command=reset)
button_reset.grid(row=4,columnspan=4,sticky=E+W,padx=4,pady=6)

window.mainloop()