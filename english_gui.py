import tkinter as tk
import random
import words
import time

window = tk.Tk()

monitor_height = window.winfo_screenheight()
monitor_width = window.winfo_screenwidth()


#main
class basedesk():
    Score=0
    def __init__(self,master):
        self.window = master
        self.window.config()
        self.window.title("Englsih Words Test")
        self.window.geometry("800x600")#for windows
        self.window.resizable(width=0, height=0)

        title(self.window)

class title():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='white')

        self.master.attributes('-fullscreen', False)#關閉全螢幕

        self.title = tk.Frame(self.master,bg='white')
        self.title.pack(expand='yes')
        start_title = tk.Label(self.title, bg='white', text='高中英語單字測驗', font=('標楷體',64))
        start_title.pack()
        aid2_label = tk.Label(self.title, bg='white', text='')
        aid2_label.pack(ipady=30)

        self.button = tk.Frame(self.master,bg='white')
        self.button.pack(pady=30)
        start_button = tk.Button(self.button, text='start',bd=1.5,relief='groove',bg='white', activeforeground='red', font=('Comic Sans MS',24), command=self.chang1)
        start_button.grid(column=1,row=1,ipadx=50,padx=25)
        close_button = tk.Button(self.button, text='quit',bd=1.5,bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS',24), command=self.quit)
        close_button.grid(column=2,row=1,ipadx=50,padx=25)
        

    def chang1(self):
        self.EnterAnswer = False
        self.master.attributes('-topmost',self.EnterAnswer)
        self.title.destroy()
        self.button.destroy()
        face1(self.master)

    def quit(self):
        self.title.quit()
        self.button.quit()
            
class face1():
    global monitor_height
    global wrong
    def __init__(self,master):
        self.master = master
        self.master.config(bg='white')

        self.master.attributes('-fullscreen', True)#全螢幕  
        self.fullScreenState = False
        #self.master.bind("<F11>", self.toggleFullScreen)

        self.face1 = tk.Frame(self.master,bg='white')
        self.face1.pack()
        title_lebal = tk.Label(self.face1, text='選擇等級', fg='black',bg='white', activeforeground='red', font=('標楷體', 81))
        title_lebal.grid(column=2, row=1, ipady=50)

        self.button = tk.Frame(self.master,bg='white')
        self.button.pack()
        level_one = tk.Button(self.button, text='level 1', fg='black', width=12, bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS', 36), command=self.level1)
        level_one.grid(column=1, row=2, padx=30, pady=20)

        level_two = tk.Button(self.button, text='level 2', fg='black', width=12, bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS', 36), command=self.level2)
        level_two.grid(column=2, row=2, padx=30, pady=20)

        level_three = tk.Button(self.button, text='level 3', fg='black', width=12, bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS', 36), command=self.level3)
        level_three.grid(column=3, row=2, padx=30, pady=20)

        level_four = tk.Button(self.button, text='level 4', fg='black', width=12, bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS', 36), command=self.level4)
        level_four.grid(column=1, row=3, padx=30, pady=10)

        level_five = tk.Button(self.button, text='level 5', fg='black', width=12, bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS', 36), command=self.level5)
        level_five.grid(column=2, row=3, padx=30, pady=10)
        
        self.back_frame = tk.Frame(self.master,bg='white')
        self.back_frame.pack(side=tk.BOTTOM)

        back_button = tk.Button(self.back_frame, text='back', fg='black', width=12, bg='white',relief='groove', activeforeground='red', font=('Comic Sans MS', 24), command=self.back)
        back_button.grid(column=1, row=1, pady=20)

    def level1(self):
        self.back_frame.destroy()
        self.face1.destroy()
        self.button.destroy()
        level(self.master,1,0,1)#等級，成績，n


    def level2(self):
        self.back_frame.destroy()
        self.face1.destroy()
        self.button.destroy()
        level(self.master,2,0,1)

    def level3(self):
        self.back_frame.destroy()
        self.face1.destroy()
        self.button.destroy()
        level(self.master,3,0,1)

    def level4(self):
        self.back_frame.destroy()
        self.face1.destroy()
        self.button.destroy()
        level(self.master,4,0,1)

    def level5(self):
        self.back_frame.destroy()
        self.face1.destroy()
        self.button.destroy()
        level(self.master,5,0,1)

    def back(self):
        self.back_frame.destroy()
        self.face1.destroy()
        self.button.destroy()
        title(self.master)

'''
#調整全螢幕模式
    def toggleFullScreen(self,even):
        self.fullScreenState = not self.fullScreenState
        self.master.attributes("-fullscreen", self.fullScreenState)
'''

class level():
    def __init__(self,master,level_num,myscore,n):
        word = []
        self.master = master
        self.level_num = level_num#等級
        self.myscore = myscore#成績
        self.master.config(bg='white')
        self.n = n#題數
        self.English = ''


        if(level_num == 1):
            word = words.level1
        elif(level_num == 2):
            word = words.level2
        elif(level_num == 3):
            word = words.level3
        elif(level_num == 4):
            word = words.level4
        elif(level_num == 5):
            word = words.level5

        question = 1
        for(english,chinese) in random.sample(word, question):
            self.English = english #抓英語單字
            strn = str(self.n)
            self.level = tk.Frame(self.master,bg='white')
            self.level.pack()
            #question
            num_label = tk.Label(self.level, text=strn, fg='black',bg='white', font=('Comic Sans MS', 36))#題號
            num_label.grid(column=0, row=1, pady=30)

            self.title_label = tk.Label(self.level, text=(chinese),bg='white', wraplength=800, fg='black', font=('標楷體', 40))#題目
            self.title_label.grid(column=0, row=2, pady=20)
            
            #self.master.bind('<Return>', self.callback)

            #answer
            self.start_entry = tk.Entry(self.level, width=15, bd=3 ,bg='white', cursor='arrow', fg='black', font=('Comic Sans MS',36))
            self.start_entry.grid(column=0, row=3, pady=30)

            #button
            self.button = tk.Frame(self.master,bg='white')
            self.button.pack(side=tk.BOTTOM)

            self.master.attributes('-topmost',True)
            # -alpha, -transparentcolor, -disabled, -fullscreen, -toolwindow, or -topmost
            self.EnterAnswer = False
            self.master.bind('<Return>',self.next_page)


    def next_page(self,even):
        Ans = self.start_entry.get()#作答的答案
        answer = self.English#正確答案

        Ans.strip()
        answer.strip()
        Ans.rstrip()
        answer.rstrip()
        #print(Ans,len(Ans))
        #print(answer,len(answer))
        self.EnterAnswer = False
        self.master.attributes('-topmost',self.EnterAnswer)
        self.level.destroy()
        self.button.destroy()
        correction(self.master,self.level_num,self.myscore,self.n,Ans,answer)


class correction():
    global monitor_height
    def __init__(self,master,level_num,myscore,n,Ans,answer):
        self.master = master
        self.level_num = level_num
        self.myscore = myscore
        self.master.config(bg='white')
        self.n = n
        self.Ans = Ans#作答的答案
        self.answer = answer#正確答案

        print(level_num,myscore,n,Ans,answer)


        self.frame = tk.Frame(self.master,bg='white')
        self.frame.pack()
        if(Ans == answer):
            labeltest = tk.Label(self.frame,text='', fg='black',bg='white', activeforeground='red', font=('Comic Sans MS', 60))
            labeltest.grid(row=0,column=0)
            label = tk.Label(self.frame,text='correct', fg='black',bg='white', activeforeground='red', font=('Comic Sans MS', 60))
            label.grid(row=1,column=0,pady=150)
            self.myscore += 1
            if(n == 20):
                self.master.bind('<Return>',self.next_page2)
            else:
                self.master.bind('<Return>',self.next_page)


        else:
            labeltest = tk.Label(self.frame,text='', fg='black',bg='white', activeforeground='red', font=('Comic Sans MS', 60))
            labeltest.grid(row=0,column=0)
            label = tk.Label(self.frame,text='wrong!!', fg='black',bg='white', activeforeground='red', font=('Comic Sans MS', 60))
            label.grid(row=1,column=0,pady=150)
            self.correctanswer = tk.Frame(self.master,bg='white')
            self.correctanswer.pack()
            label2 = tk.Label(self.correctanswer,text='answer : ', fg='black',bg='white', activeforeground='red', font=('Comic Sans MS', 60))
            label2.grid(row=1,column=0,pady=10)
            label3 = tk.Label(self.correctanswer,text=(answer), fg='black',bg='white', activeforeground='red', font=('Comic Sans MS', 60))
            label3.grid(row=1,column=1,pady=10)
            if(n == 20):
                self.master.bind('<Return>',self.next_page2)
            else:
                self.master.bind('<Return>',self.next_page)
            


    def next_page(self,even):
        self.n += 1
        self.frame.destroy()
        self.correctanswer.destroy()
        level(self.master,self.level_num,self.myscore,self.n)

    def next_page2(self,even):
        self.n += 1
        self.frame.destroy()
        self.correctanswer.destroy()
        score(self.master,self.myscore)

class score():
    def __init__(self,master,Score):
        self.master = master
        self.master.config(bg='white')

        self.score = tk.Frame(self.master,bg='white')
        self.score.pack()
        self.score_label = tk.Label(self.score, text='SCORE', fg='black',bg='white', font=("Comic Sans MS", 48))
        self.score_label.grid(column=1, row=1, ipady=100, padx=100)
        self.score_score = tk.Label(self.score, text = (Score*5), fg='black',bg='white', font=("Comic Sans MS", 48))
        self.score_score.grid(column=1, row=2, ipady=0, padx=30)
        
        self.score_grid = tk.Frame(self.master,bg='white')
        self.score_grid.pack()
        self.score_grid1 = tk.Label(self.score_grid, text='', bg='white')
        self.score_grid1.grid(column=1, row=1, ipady=0, padx=100)

        self.EnterAnswer = False#待修改
        self.master.bind('<Return>',self.back)#待修改

        self.score_button = tk.Button(self.score_grid, text='back', fg='black',bg='white', font=("Comic Sans MS", 30), command=self.back)
        self.score_button.grid(column=2, row=3,pady=250)

    def back(self):
        self.master.attributes('-topmost',False)#待修改
        self.score_grid.destroy()
        self.score.destroy()
        title(self.master)

if __name__ == '__main__':
    basedesk(window)
    window.mainloop()