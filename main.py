from tkinter import *
import random
from PIL import Image, ImageTk

names = []
asked = []
score=0

def randomiser():
    global qnum
    qnum = random.randint(1,3)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
      

class QuizStarter:
  def __init__(self, parent):
    background_color="lightgrey"

    self.heading_label=Label(window, text = "Sports quiz", font =( "Tw Cen MT","18","bold"),bg=background_color)
    self.heading_label.place(x=100,y=100)

    self.con1=IntVar()

    self.user_label=Label(window, text="Enter name: ", font=( "Tw Cen MT","18","bold"),bg=background_color)
    self.user_label.place(x=468,y=100)

    self.entry_box=Entry(window)
    self.entry_box.place(x=475,y=150)

    self.continue_button = Button(window, text="Start Quiz", font=( "Helvetica","13","bold"), bg="lightblue",command=self.name_collection)
    self.continue_button.place(x=500, y=200)
    

  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        print(names)
        self.heading_label.destroy()
        self.user_label.destroy()
        self.entry_box.destroy()
        self.continue_button.destroy()
        Quiz(window)

class Quiz:

  def __init__(self, parent):
    background_color="lightgrey"
    
    self.qa_dictionary = {
    1: ["Who won the 2002 FIFA World cup?", 'Brazil', 'America','UK', 'Austrailia' ,'Brazil',1],
    2: ["Which NBA player has won the most championships?",'Michael Jordan','Bill Russel','Lebron James', 'Wilt Chamberlain','Bill Russel',2],
    3: ["Which position in soccer is allowed to touch the ball?", 'Forward','Midfielder', 'Defender','Goalkeeper','Goalkeeper',4],
    4:["How many gold medals has Usain Bolt won?",'6','8','9','7','8',2,], 
    5:["What "]

}
  
  
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(window, text = self.qa_dictionary[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.con1=IntVar()

    self.rb1 = Radiobutton(window, text = self.qa_dictionary[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.con1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton(window, text = self.qa_dictionary[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.con1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton(window, text = self.qa_dictionary[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.con1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton(window, text = self.qa_dictionary[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.con1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(window, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_button.place(x=300,y=235)
    self.score_label  = Label(window, text = 
                             'score')
    self.score_label.place(x=390,y=240)  

    self.quit=Button(window,text="Quit",font=("Helvetica","13","bold"),bg="red2",command=self.end_screen)
    self.quit.place(x=50,y=235)
     
     
  def questions_setup(self):
     randomiser()
     self.con1.set(0)
     self.question_label.config(text=self.qa_dictionary[qnum][0])
     self.rb1.config(text=self.qa_dictionary[qnum][1])
     self.rb2.config(text=self.qa_dictionary[qnum][2])
     self.rb3.config(text=self.qa_dictionary[qnum][3])
     self.rb4.config(text=self.qa_dictionary[qnum][4]) 
  
  def test_progress(self):
      global score 
      scr_label=self.score_label 
      choice=self.con1.get()
      if len(asked)>2:
        if choice == self.qa_dictionary[qnum][6]:
          score +=1 
          scr_label.configure(text=score) 
          self.confirm_button.config(text="Confirm")
          self.end_screen()
          
        else:
          score+=0 
          scr_label.configure(text="The correct answer was: "+ self.qa_dictionary[qnum][5] ) 
          self.confirm_button.config(text="confirm")
          self.end_screen()
      
      else:
            if choice==0: 
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.con1.get() 
            else:
              if choice == self.qa_dictionary[qnum][6]: 
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup() 
  
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + self.qa_dictionary[qnum][5])
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup()
    
  def end_screen(self):
    window.withdraw()
    end_object=End()

class End:
  def _innit_(self):
    background="OldLace"
    self.end_box= Toplevel(window)
    self.end_box.title("End Box")

    self.end_frame = Frame (self.end_box,width=1000,height=1000,bg=background)
    self.end_frame.grid(row=1)

    end_heading = Label(self.end_frame,text='Well Done',font=('Tw Cen Mt',22,'bold'),bg=background,pady=15)
    end_heading.grid(row=0)

    exit_button=Button (self.end_frame,text='Exit',width=10,bg="indianRed1",font=('Tw Cen Mt',12,'bold'),command=self.close_end)
    exit_button.grid(row=4,pady=20)

    self.listLabel = Label(self.end_frame,text="1st Place Available",font=('Tw Cen MT'),width=40,bg=backround,padx=10,pady=10)
    self.listLabel.grid(column=0,row=2)
  
  
  def close_end(self):
    self.end_box.destroy()
    window.withdraw()
  


class leaderBoard:
    def _innit_(self, parent):

     parent.geometry("500x600")
     self.bg_img = image.open("blue.png")
     self.bg_img = self.bg_img.resize(("500x600"),image.ANTIALIAS)
     image = imageTk.PhotoImage(self.bg_img)
     image_label.config(image=image)
     image_label.image = image

     self.name.label=Label(parent,text="name",height=3,width=15)
      
  
  




  
    name=names[0]
    file=open("leaderBoard.txt","a")
    
    if name== "rowel_erase":
      file=open("leaderboard.txt","w")
    else:
      file.write(str(score))
      file.write(" - ")
      file.write(name+"\n")
      file.close
  
    inputFile = open("leaderBoard.txt","r")
    lineList = inputFile.readlines()
    lineList.sort()
    top=[]
    top5=(lineList[-5:])
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]),point[1]))
    file.close()
    top.sort()
    top.reverse()
    return_string = ""
    for i in range(len(top)):
      return_string+="{} - {}\n".format(top[i][0],top[i][1])
    print(return_string)
  
    end_object=End()
    end_object.listLabel.config(text=return_string)
    
if __name__== "__main__":
    window = Tk()
    window.title("12CSC Quiz")
    window.geometry("700x600")
    bg_image = Image.open("guy running.png")
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = QuizStarter(window)
    
    window.mainloop()