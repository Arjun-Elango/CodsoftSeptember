import tkinter as tk
from tkinter import messagebox
from random import shuffle

class Quiz_Game:
    def __init__(self,A):
        self.A=A
        self.A.title("Quiz Game")

        self.QD=[
            {
                "question":"Which gas do plants absorb from the atmosphere during photosynthesis ?",
                "options":["Oxygen","Carbon dioxide","Nitrogen","Hydrogen"],
                "answer":"Carbon dioxide"
            },
            {
                "question":"Which country is known as the land of the rising sun?",
                "options":["China","Japan","south korea","Thailand"],
                "answer":"Japan"
            },       
            {
                "question":"What is the capital of France ?",
                "options":["London","Berlin","Paris","Rome"],
                "answer":"Paris"
            },
            {
                "question":"which is the largest mammal in the world?",
                "options":["Africa Elephant","Blue Whale","Giraffe","polar Bear"],
                "answer":"Blue Whale"
            },
             {
                "question":"what is the chemical symbol for gold?",
                "options":["Go","Au","Ag","Ge"],
                "answer":"Au"
            },
            {
                "question":"which is the largest planet in our solar system?",
                "options":["Jupiter","saturn","Neptune","Mars"],
                "answer":"Jupiter"
            },
             {
                "question":"which planet is known as the RED planet?",
                "options":["jupiter","saturn","neptune","mars"],
                "answer":"mars"
            },
             {
                "question":"which is the largest continent in the world?",
                "options":["Asia","Africa","North America","Europe"],
                "answer":"Asia"
            },
             {
                "question":"what is the capital city of tamil nadu?",
                "options":["chennai","Madurai","coimbatore","Tiruchirappalli"],
                "answer":"chennai"
            },
             {
                "question":"which festival is widely celebratedin tamil nadu during the month of january?",
                "options":["deepavali","Navaratri","pongal","chrismas"],
                "answer":"pongal"
            },
        ]
        self.scr=0
        self.current_Qns=0
        self.Qn_label=tk.Label(self.A,text="",font=("Arial",28),wraplength=470,fg="#1F6357",bg="#D2B48C")
        self.Qn_label.pack(pady=5,padx=5)

        self.option_button=[]
        for i in range(4):
          button=tk.Button(self.A,text="",font=("Arial",28),width=30,command=lambda i=i: self.check_answer(i),fg="#95B9C7",bg="#00A36C")
          button.pack(pady=5)
          self.option_button.append(button)

        self.scr_label=tk.Label(self.A,text="score: 0",font=("Arial",12))
        self.scr_label.pack(pady=20)
        
        self.nxt_q()

    def nxt_q(self):
       if self.current_Qns < len(self.QD):
          Qns=self.QD[self.current_Qns]
          self.Qn_label.config(text=Qns["question"])
          option=Qns["options"]
          shuffle(option)
          for i in range(4):
            self.option_button[i].config(text=option[i])
            self.scr_label.config(text="score: {}".format(self.scr))
       else:
         self.end_game()

    def check_answer(self,selected_option):
     question=self.QD[self.current_Qns]
     selected_answer=question["options"][selected_option]
     correct_answer=question["answer"]
     if selected_answer==correct_answer:
          self.scr+=1
     self.current_Qns +=1
     self.nxt_q()
    
    def end_game(self):
        messagebox.showinfo("Game Over","Quiz has ended!\n Your Score: {}".format(self.scr))
        self.A.destroy()
A=tk.Tk()
A.geometry("465x550")
A.resizable(0,0)
quiz_game=Quiz_Game(A)
A.mainloop()