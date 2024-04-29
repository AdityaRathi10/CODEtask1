from tkinter import *
import math
from pygame import mixer
import speech_recognition 

mixer.init()

def click(value):
      ex=entryFiled.get()
      answer=''
      if value=='C':
            ex=entryFiled.get()
            ex=ex[0:len(ex)-1]
            entryFiled.delete(0,END)
            entryFiled.insert(0,ex)
      elif value=='CE':
           entryFiled.delete(0,END)

      elif value == '√':
            answer=math.sqrt(eval(ex))
      elif value == 'π':
            answer = math.pi
      elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))
      elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))
      elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))
      elif value == 'cosh':
            answer = math.cosh(eval(ex))
      elif value == 'tanh':
            answer = math.tanh(eval(ex))
      elif value == 'sinh':
            answer = math.sinh(eval(ex))
      elif value=="2π":
            answer = 2*math.pi
      elif value == chr(8731):
            answer = eval(ex)**(1/3)
      elif value=='x\u02b8':
            entryFiled.insert(END ,'**')
      elif value=='x\u00B2':
            answer = eval(ex)**2
      elif value=='x\u00B3':
            answer = eval(ex)**3
      elif value == 'ln':
            answer = math.log2(eval(ex))
      elif value == 'deg':
            answer = math.degrees(eval(ex))
      elif value =='x!':
            answer = math.factorial(eval(ex))
      elif value == 'rad':
            answer = math.radians(eval(ex))
      elif value == 'e':
            answer = math.e
      elif value == chr(247):
            entryFiled.insert(END,'/')
            return
      elif value == '=':
            answer = eval(ex) 

      elif value == 'log10':
            answer = math.log10(eval(ex))

      else:
            entryFiled.insert(END,value)
            return
      
      entryFiled.delete(0,END)
      entryFiled.insert(0,answer)

def add(a,b):
      return a+b

def sub(a,b):
      return a-b

def mul(a,b):
      return a*b

def div(a,b):
      return a/b

def mod(a,b):
      return a%b

def lcm(a,b):
      l=math.lcm(a,b)
      return l

def hcf(a,b):
      h=math.gcd(a,b)
      return h

operations = {'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
              'SUBTRACTION':sub,'DIFFERENCE':sub,'MINUS':sub,'SUBTRACT':sub,
              'PRODUCT':mul,'MULTIPLICATION':mul,'MULTIPLY':mul,
              'DIVISION':div,'DIV':div,'DIVIDE':div,
              'LCM':lcm,'HCF':hcf,
              'MOD':mod,'REMAINDER':mod,'MODULUS':mod}


def findNumbers(t):
      l=[]
      for num in t:
            try:
                  l.append(int(num))
            except ValueError:
                  pass
      return l  


def audio():
      mixer.music.load('C:/Users/adity/Desktop/Python/Intership/music1.mp3')
      mixer.music.play()
      sr=speech_recognition.Recognizer()
      with speech_recognition.Microphone() as source:
            try:
                  sr.adjust_for_ambient_noise(source,duration=0.2)
                  voice = sr.listen(source)
                  text = sr.recognize_google(voice)
                  print(text)
                  mixer.music.load('C:/Users/adity/Desktop/Python/Intership/music2.mp3')
                  mixer.music.play()
                  text_list=text.split(' ')
                  print(text_list)
                  for word in text_list:
                        if word.upper() in operations.keys():
                              l=findNumbers(text_list)
                              print(l)
                              result=operations[word.upper()](l[0],l[1])
                              entryFiled.delete(0,END)
                              entryFiled.insert(END,result)

                        else:
                              pass


            except:
                  pass

root = Tk()
root.title("Smart Calculator")

root.config(bg="dodgerblue3")
root.geometry('680x486+100+100')

logoImage = PhotoImage(file='C:/Users/adity/Desktop/Python/Intership/logo.png')
lable=Label(root,image=logoImage,bg='dodgerblue3')
lable.grid(row=0,column=0)

entryFiled = Entry(root,font=('airal',20,'bold'),bg='dodgerblue3',fg='white',bd=10,relief=SUNKEN,width=30)
entryFiled.grid(row=0,column=0,columnspan=8)

micImage = PhotoImage(file='C:/Users/adity/Desktop/Python/Intership/microphone.png')
micButton=Button(root,image=micImage,bd=0,bg='dodgerblue3',activebackground='dodgerblue3',command=audio)
micButton.grid(row=0,column=7)

button_text_list=['C','CE','√','+','π','cosθ','sinθ','tanθ',
                  '1','2','3','-','2π','cosh','tanh','sinh',
                  '4','5','6','*',chr(8731),'x\u02b8','x\u00B3','x\u00B2',
                  '7','8','9',chr(247),'ln','deg','rad','e',
                  '0','.','%','=','log10','(',')','x!']
rowvalue = 1
columnvalue = 0

for i in button_text_list:
      button = Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='dodgerblue3',fg='white',font=('airal',18,'bold'),activebackground='dodgerblue3',command=lambda button=i:click(button))
      button.grid(row=rowvalue,column=columnvalue,pady=1)
      columnvalue+=1
      if columnvalue>7:
            rowvalue+=1
            columnvalue=0
root.mainloop()