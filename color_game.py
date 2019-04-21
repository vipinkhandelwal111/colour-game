import tkinter 
import random 
  
colours = ['Red','Blue','Green','Pink','Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30

  
def startGame(event): 
      if timeleft == 30:  
        countdown() 
           
      nextColour() 
        
 
def nextColour(): 
  
    global score 
    global timeleft 
  

    if timeleft > 0:  
        t1.focus_set() 

        if t1.get().lower() == colours[1].lower(): 
              
            score+=1
  
         
        t1.delete(0, tkinter.END) 
        random.shuffle(colours)
        
        l4.config(fg = str(colours[1]), text = str(colours[0]))
        
        
        l2.config(text = "Score: " + str(score))
    elif timeleft <= 0:
        l4.config(text = "GAME OVER", fg = "white", font = ('Helvetica', 14))
      
  
 
def countdown(): 
  
    global timeleft 
    if timeleft > 0:  
        timeleft -= 1
        l3.config(text = "Time left: "+ str(timeleft)) 
        l3.after(1000, countdown) 
  
  
#design---------GUI----------------using Tkinter---------------------------------------------------
        
root = tkinter.Tk() 
  

root.title("TELL THE COLOR") 
root.geometry("400x225") 
root.configure(background='black')  
 
l1 = tkinter.Label(root, text = "Check your IQ",bg="black",foreground="white",font = ('Comic Sans MS', 14)) 
l1.pack()  
  
 
l2 = tkinter.Label(root, text = "Press enter to start",bg="black",foreground="white",font = ('Comic Sans MS', 13)) 
l2.pack() 
  

l3 = tkinter.Label(root, text = "Time left: " +str(timeleft),bg="black",foreground="white", font = ('Fixedsys', 14)) 
l3.pack() 
  

l4 = tkinter.Label(root,foreground="white",bg="black", font = ('Helvetica', 72)) 
l4.pack() 
  

t1 = tkinter.Entry(root) 
root.bind('<Return>', startGame) 
t1.pack() 
t1.focus_set() 
  
root.mainloop() 
