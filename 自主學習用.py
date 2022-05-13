#import
import csv
import time
import random

#變數
m = []
s = 0

def word_file(name):
    word = []
    with open(name, mode='r', encoding='utf-8') as csvfile:
        content = csv.reader(csvfile)
        for words in content:
            word.append(tuple(words))
    return word

def examination(name):
    global m
    global s
    word = word_file(name)
    a = 1
    question = 100
    for(english,chinese) in random.sample(word, question):
        try:
            print("\n")
            print(a,'::')
            a+=1
            answer = input("{} -->".format(chinese))
            if(answer == english):
                print("--It's correct.")
                s+=1
            
            else:
                print("--wrong")
                m.append(chinese)
                m.append(english)
        
        except:
            continue

def score():
    global m
    global s
    print("錯誤題目:")
    for i in range(len(m)):
        if(i%2 == 0):
            print(m[i],":",m[i+1])
    print("score =",s)


while True:
    print("-----單字測驗-----")
    print("(1)level 1~3  (2)level 4  (3)level 5  (4)level 6  (5)level 4~6")
    level = input("選擇等級：")
    start = input("按下ENTER來開始")
    if start == '':
        if level == '1':
            if __name__ == '__main__':
                examination("level 1-3.csv")
                score()
                
        elif level == '2':
            if __name__ == '__main__':
                examination("level 4~6.csv")
                score()
        
        elif level == '3':
            if __name__ == '__main__':
                examination("level 4.csv")
                score()
        
        elif level == '4':
            if __name__ == '__main__':
                examination("level 5.csv")
                score()

        elif level == '5':
            if __name__ == '__main__':
                examination("level 6.csv")
                score()


        else:
            print("您輸入的選項錯誤")
