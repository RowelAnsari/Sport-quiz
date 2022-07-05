# quiz game

from tkinter import *  # for GUI
import random  # for randomising
from PIL import Image, ImageTk  # for images
from tkinter import messagebox  # for message box

# list that are names saved to

names = []

# list

asked = []
score = 0


# randomiser method

def randomiser():
    global qnum  # the question number is the key in our dictionary qa_dictionary, we have 10 keys (10 quuestions)
    qnum = random.randint(1, 10)  # so that the order of questions i srandom every time

    # check that the question is not already asked,if not,will add to the asked list, if it is then randomly will be picked

    if qnum not in asked:  # asked is a list we declared, so to start of with any number will be added, then this statement checkeck if ti was ther before
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


# component 1 quiz window

class quizwindow:

    def __init__(self, parent):  # constructor, The __init__() function is called automatically every time the class is being used to create a new object.
        background_color = 'lightgrey'  # to set it as background color for all the label widgets

        # heading label

        self.heading_label = Label(window, text='Sports quiz',
                                   font=('Tw Cen MT', '18', 'bold'),
                                   bg=background_color)
        self.heading_label.place(x=100, y=100)

        # enter label

        self.enter_label = Label(window, text='Enter name: ',
                                 font=('Tw Cen MT', '18', 'bold'),
                                 bg=background_color)
        self.enter_label.place(x=468, y=100)

        # entry box

        self.entry_box = Entry(window)
        self.entry_box.place(x=475, y=150)

        # continue button

        self.continue_button = Button(window, text='Start Quiz',
                font=('Helvetica', '13', 'bold'), bg='lightblue',
                command=self.name_collection)
        self.continue_button.place(x=500, y=200)

    # method in class to collect the name entered by user, destroy the widgets and create a quiz object

    def name_collection(self):
        name = self.entry_box.get()

        # component 6 error handling

        if name == '':
            messagebox.showerror('Name is required!',
                                 'Please enter your name')
        elif len(name) > 15:

        # to make sure name entered is between 1-15

            messagebox.showerror('limit error',
                                 'please enter a name between 1 and 15 characters'
                                 )
        elif name.isnumeric():
            messagebox.showerror('Name error',
                                 'Name can only consist of letters')
        elif not name.isalpha():

        # to make sure name entered is only letters not numbers

            messagebox.showerror('test', 'name cant consist of symbols')
        else:

        # to make sure name entered is only letters not symbols

            names.append(name)  # add name to names list declared at the beginning
            print (names)
            self.heading_label.destroy()  # destroys heading label
            self.enter_label.destroy()  # destroys enter label
            self.entry_box.destroy()  # destroys entry box
            self.continue_button.destroy()  # destroys continue button
            quizquestions(window)  # now we open the quiz questions page


# component 2 quiz questions

class quizquestions:

    def __init__(self, parent):
        background_color = 'lightgrey'

       # dictionary has key of numbers (for each question number) and : the value for each is a list that has 7 items, so index is 0-6

        self.qa_dictionary = {  
            1: [
                'Who won the 2002 FIFA World cup?',# item 1,index 0 will be the question
                'Brazil',# item 2,index 1 will be the second choice
                'America',# item 3,index 2 will be the third choice
                'UK',# item 4,index 3 will be the fourth choice
                'Austrailia',# item 5,index 4 will be the fifth choice
                'Brazil',# item 6,will be index 5 which will be the write statement to display the rigth answer if the user enters a wrong choice
                1,# item 7, index 6 will be the position of the rigth answer, this will check if answer is correct or not
                ],
            2: [
                'Which NBA player has won the most \n championships?',
                'Michael Jordan',
                'Bill Russel',
                'Lebron James',
                'Wilt Chamberlain',
                'Bill Russel',
                2,
                ],
            3: [
                'Which position in soccer is allowed to touch the \n ball?'
                    ,
                'Forward',
                'Midfielder',
                'Defender',
                'Goalkeeper',
                'Goalkeeper',
                4,
                ],
            4: [
                'How many gold medals has Usain Bolt won?',
                '6',
                '8',
                '9',
                '7',
                '8',
                2,
                ],
            5: [
                'What is the only sport to be played on the moon?',
                'Basketball',
                'Soccer',
                'Golf',
                'Cricket',
                'Golf',
                3,
                ],
            6: [
                'The Olympics are held every how many years?',
                '2',
                '3',
                '4',
                '5',
                '4',
                3,
                ],
            7: [
                'What is the record for red cards given in a soccer \n game?'
                    ,
                '36',
                '18',
                '29',
                '11',
                '36',
                1,
                ],
            8: [
                'How many players are on court at one time during \n volleyball game?'
                    ,
                '12',
                '14',
                '10',
                '16',
                '12',
                1,
                ],
            9: [
                'Which of these is not currently an Olympic sport?',
                'Taekwondo',
                'Cricket',
                'Handball',
                'Judo',
                'Cricket',
                2,
                ],
            10: [
                'Which terms means you knocked down all of \n the pins in bowling?'
                    ,
                'Split',
                'Set',
                'Spare',
                'Strike',
                'Strike',
                4,
                ],
            }
        #quiz frame
      
        self.quiz_frame = Frame(parent, bg=background_color, padx=40,
                                pady=40)

        randomiser()

        # question label

        self.question_label = Label(window,
                                    text=self.qa_dictionary[qnum][0],
                                    font=('Tw Cen MT', '18', 'bold'))
        self.question_label.grid(row=0, padx=10, pady=10)

        # hold value of radio buttons

        self.con1 = IntVar()

        # radio buttons 1

        self.rb1 = Radiobutton(
            window,
            text=self.qa_dictionary[qnum][1],
            font=('Helvetica', '12'),
            bg=background_color,
            value=1,
            variable=self.con1,
            pady=10,
            )
        self.rb1.grid(row=1, sticky=W)

        # radio buttons 2

        self.rb2 = Radiobutton(
            window,
            text=self.qa_dictionary[qnum][2],
            font=('Helvetica', '12'),
            bg=background_color,
            value=2,
            variable=self.con1,
            pady=10,
            )
        self.rb2.grid(row=2, sticky=W)

        # radio buttons 3

        self.rb3 = Radiobutton(
            window,
            text=self.qa_dictionary[qnum][3],
            font=('Helvetica', '12'),
            bg=background_color,
            value=3,
            variable=self.con1,
            pady=10,
            )
        self.rb3.grid(row=3, sticky=W)

        # radio buttons 4

        self.rb4 = Radiobutton(
            window,
            text=self.qa_dictionary[qnum][4],
            font=('Helvetica', '12'),
            bg=background_color,
            value=4,
            variable=self.con1,
            pady=10,
            )
        self.rb4.grid(row=4, sticky=W)

        # confirm button

        self.confirm_button = Button(window, text='Confrim', bg='white'
                , command=self.quiz_score)
        self.confirm_button.place(x=300, y=235)

        # score label

        self.score_label = Label(window, text='score')
        self.score_label.place(x=390, y=240)

        # component 4 leave button

        self.leave = Button(window, text='Leave', font=('Helvetica',
                            '13', 'bold'), bg='lightblue',
                            command=self.end_screen)
        self.leave.place(x=50, y=235)

    # configuring (editing) the question label to new questions and possible answers as new radio button choices

    def qa_setup(self):
        randomiser()
        self.con1.set(0)
        self.question_label.config(text=self.qa_dictionary[qnum][0])
        self.rb1.config(text=self.qa_dictionary[qnum][1])
        self.rb2.config(text=self.qa_dictionary[qnum][2])
        self.rb3.config(text=self.qa_dictionary[qnum][3])
        self.rb4.config(text=self.qa_dictionary[qnum][4])

    # component 3 score counter

    def quiz_score(self):  # can pass on users choice as argument here as well
        global score  # this score needs to b accessible to all
        score_label = self.score_label  # renaming the score label each time the score is different
        choice = self.con1.get()  # get the user choice, remember are con1 is the IntVar() method that stores the number chosen
        if len(asked) > 9:  # to determine if its the lat question and just end the quiz after
            if choice == self.qa_dictionary[qnum][6]:  # checking that the key (qnum) has the correct answet which is stored in index 6 of the value array
                score += 1  # adds one point to score
                score_label.configure(text=score)  # will change label to new score
                self.confirm_button.config(text='Confirm')  # will change the text on the button to confirm
                self.end_screen()  # to open end screen (end box) when quiz is done
            else:

                score += 0  # score will stay the same
                score_label.configure(text='The correct answer was: '
                        + self.qa_dictionary[qnum][5])  # this is to give the right answer instead of their score
                self.confirm_button.config(text='confirm')  # button text
        else:

             # if the length of the asked list is 9 or less, so quiz will have question to ask

            if choice == 0:  # if user does not select an option
                self.confirm_button.config(text="Try Again, you didn't select an option then submit again"
                        )

                         # error message

                choice = self.con1.get()  # still get the answer if they choose it
            else:

                 # if choice is made

                if choice == self.qa_dictionary[qnum][6]:  # if the choice made is correct
                    score += 1
                    score_label.configure(text=score)
                    self.confirm_button.config(text='confirm')
                    self.qa_setup()  # move to the next question: use the question.setup() method to configure the question label and answers
                else:

                     # if choice was not the correct answer

                    score += 0
                    score_label.configure(text='The correct answer was: '
                             + self.qa_dictionary[qnum][5])
                    self.confirm_button.config(text='Confirmn')
                    self.qa_setup()  # move to next question

    # method to end screen

    def end_screen(self):
        window.destroy()
        name = names[0]

        open_end_object = end()


# component 5 exit box

class end:

    def __init__(self):
        background_color = 'darkturquoise'
        global window2
        window2 = Tk()
        window2.title('Exit Box')
        window2.geometry('700x600')

        # end frame

        self.end_frame = Frame(window2, width=700, height=600,
                               bg=background_color)
        self.end_frame.grid(row=1)

        # end heading

        self.end_heading = Label(window2,
                                 text='Nice try, you finished the quiz '
                                 , font=('Tw Cen Mt', 22, 'bold'),
                                 bg=background_color)
        self.end_heading.place(x=80, y=50)

        # exit button

        self.exit_button = Button(
            window2,
            text='Exit',
            width=10,
            bg='lightblue',
            font=('Tw Cen Mt', 12, 'bold'),
            command=self.close_end,
            )
        self.exit_button.place(x=260, y=200)

        # list label

        self.list_label = Label(window2, text='Feel free to try again',
                                font=('Tw Cen Mt', 12, 'bold'),
                                width=40, bg=background_color)
        self.list_label.place(x=110, y=100)

    def close_end(self):
        self.end_frame.destroy()
        self.end_heading.destroy()
        self.exit_button.destroy()
        self.list_label.destroy()
        window2.destroy()


# program runs below

if __name__ == '__main__':
    window = Tk()
    window.title('12CSC Quiz')
    window.geometry('700x600')
    bg_image = Image.open('guy running.png')  # need to use Image if need to resize
    bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)

    # image label

    image_label = Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = quizwindow(window)

    window.mainloop()  # so the window doesnt dissapear