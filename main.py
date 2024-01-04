import tkinter as tk
from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry
from PIL import Image, ImageTk
from random import choice
from tkinter import messagebox


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.count_sys = 0
        self.count_user = 0
        self.game_sys = ["paper", "rock", "scissors"]
        self.st_btn = True
        self.dor_bazi = 3
        
        self.title("paper rock scissors")
        self.geometry("500x500+400+80")
        self.resizable(False, False)
        self.config(bg="#aee1f2")

        self.frame_top = CTkFrame(self, width=490, height=50, fg_color="#3f9fbf", bg_color="#aee1f2",
                                  border_width=2, border_color="black")
        self.frame_top.place(x=5, y=5)
        
        CTkLabel(self.frame_top, text="paper rock scissors", font=("Arial", 20, "bold")).place(x=150, y=10)
        
        self.frame_con = CTkFrame(self, width=490, height=80, fg_color="#3f9fbf", bg_color="#aee1f2",
                                  border_width=2, border_color="black")
        self.frame_con.place(x=5, y=60)
        
        CTkLabel(self.frame_con, text="System: ", font=("Arial", 20, "bold")).place(x=20, y=10)
        CTkLabel(self.frame_con, text="User: ", font=("Arial", 20, "bold")).place(x=20, y=40)
        
        self.lbl_count_sys = CTkLabel(self.frame_con, text="0", font=("Arial", 20, "bold"))
        self.lbl_count_sys.place(x=100, y=10)
        
        self.lbl_count_user = CTkLabel(self.frame_con, text="0", font=("Arial", 20, "bold"))
        self.lbl_count_user.place(x=100, y=40)
        
        self.entry = CTkEntry(self.frame_con, width=80, height=40, border_width=2, border_color="black",
                              font=("Arial", 20, "bold"))
        self.entry.place(x=300, y=20)
        
        self.bt_sub = CTkButton(self.frame_con, text="Submit", fg_color="#3dd9a0", text_color="white",
                                width=80, height=40, border_width=2, border_color="black",
                              font=("Arial", 20, "bold"), hover_color="black", command=self.game_count)
        self.bt_sub.place(x=390, y=20)
        
        self.frame_Bottom = CTkFrame(self, width=490, height=300, fg_color="#3f9fbf", bg_color="#aee1f2",
                                  border_width=2, border_color="black")
        self.frame_Bottom.place(x=5, y=145)
        
        self.frame_pic = CTkFrame(self.frame_Bottom, width=450, height=190, fg_color="white")
        self.frame_pic.place(x=20, y=10)
        
        self.img_sys = Image.open("pictures/paper.png")
        self.img_sys = self.img_sys.resize((155, 155))
        self.ph_sys = ImageTk.PhotoImage(self.img_sys)
        self.lbl_pic_sys = tk.Label(self.frame_pic, text="", image=self.ph_sys)
        
        self.img_user = Image.open("pictures/paper.png")
        self.img_user = self.img_user.resize((155, 155))
        self.ph_user = ImageTk.PhotoImage(self.img_user)
        self.lbl_pic_user = tk.Label(self.frame_pic, text="", image=self.ph_user)
        # self.lbl_pa.place(x=10, y=15)
        # self.lbl_pa.place(x=280, y=15)
        
        self.frame_btns = CTkFrame(self.frame_Bottom, width=450, height=80)
        self.frame_btns.place(x=20, y=210)
        
        self.btn_paper = CTkButton(self.frame_btns, text="Paper", width=140, height=50,
                                   font=("Arial", 16, "bold"), fg_color="#2c3538", text_color="white",
                                   border_width=2, border_color="black", hover_color="#0d1314",
                                   command=lambda x="paper": self.click(x))
        self.btn_paper.grid(row=0, column=0, padx=5, pady=10)
        
        self.btn_scissors = CTkButton(self.frame_btns, text="Scissors", width=140, height=50,
                                   font=("Arial", 16, "bold"), fg_color="#2c3538", text_color="white",
                                   border_width=2, border_color="black", hover_color="#0d1314",
                                   command=lambda x="scissors": self.click(x))
        self.btn_scissors.grid(row=0, column=1, padx=5, pady=10)
        
        self.btn_rock = CTkButton(self.frame_btns, text="Rock", width=140, height=50,
                                   font=("Arial", 16, "bold"), fg_color="#2c3538", text_color="white",
                                   border_width=2, border_color="black", hover_color="#0d1314",
                                   command=lambda x="rock": self.click(x))
        self.btn_rock.grid(row=0, column=2, padx=5, pady=10)
        
        self.frame_Bot = CTkFrame(self, width=490, height=45, fg_color="#121414", bg_color="#aee1f2",
                                  border_width=2, border_color="black")
        self.frame_Bot.place(x=5, y=450)
        
        self.lbl_result = CTkLabel(self.frame_Bot, text="User Win", font=("Arial", 20, "bold"),
                                   fg_color="#121414", text_color="white")
        # self.lbl_result.place(x=200, y=10)
    
    def win_change(self, user, sys):
        if user == sys:
            return "equal"
        elif user == "paper" and sys == "rock":
            self.count_user += 1
            return "user"
        elif user == "scissors" and sys == "paper":
            self.count_user += 1
            return "user"
        elif user == "rock" and sys == "scissors":
            self.count_user += 1
            return "user"
        else:
            self.count_sys += 1
            return "sys"

    def game_count(self):
        number = self.entry.get()
        if number.isnumeric():
            self.dor_bazi = int(number)
            self.bt_sub.configure(state=tk.DISABLED)
            self.entry.configure(state=tk.DISABLED)
            self.st_btn = False
        else:
            messagebox.showerror("Error", "please etner number...!!!")
    
    def end_game(self):
        if self.count_user == self.dor_bazi or self.count_sys == self.dor_bazi:
            self.result_game()
            if messagebox.askyesno("End Game", "Do you want to play again?"):
                self.count_sys, self.count_user = 0, 0
                self.lbl_count_sys.configure(text="0")
                self.lbl_count_user.configure(text="0")
                self.lbl_pic_sys.place_forget()
                self.lbl_pic_user.place_forget()
                self.lbl_result.place_forget()
                self.bt_sub.configure(state=tk.NORMAL)
                self.entry.configure(state=tk.NORMAL)
                self.st_btn = True
            else:
                self.destroy()
    
    def result_game(self):
        if self.count_user > self.count_sys:
            messagebox.showinfo("End Game", "User Win\nVery Good")
        else:
            messagebox.showinfo("End Game", "System Win\nLuck was not on your side")
    
    def click(self, user):
        if self.st_btn == False:
            # user info
            if user == "paper":
                self.img_user = Image.open(r"pictures/paper.png")
                self.img_user = self.img_user.resize((155, 155))
                self.ph_user = ImageTk.PhotoImage(self.img_user)
            elif user == "rock":
                self.img_user = Image.open(r"pictures/rock.png")
                self.img_user = self.img_user.resize((155, 155))
                self.ph_user = ImageTk.PhotoImage(self.img_user)
            else:
                self.img_user = Image.open(r"pictures/scissors.png")
                self.img_user = self.img_user.resize((155, 155))
                self.ph_user = ImageTk.PhotoImage(self.img_user)
            self.lbl_pic_user.config(image=self.ph_user, bg="white")
            self.lbl_pic_user.place(x=10, y=15)
            
            # system info
            sys = choice(self.game_sys)
            if sys == "paper":
                self.img_sys = Image.open(r"pictures/paper.png")
                self.img_sys = self.img_sys.resize((155, 155))
                self.ph_sys = ImageTk.PhotoImage(self.img_sys)
            elif sys == "rock":
                self.img_sys = Image.open(r"pictures/rock.png")
                self.img_sys = self.img_sys.resize((155, 155))
                self.ph_sys = ImageTk.PhotoImage(self.img_sys)
            else:
                self.img_sys = Image.open(r"pictures/scissors.png")
                self.img_sys = self.img_sys.resize((155, 155))
                self.ph_sys = ImageTk.PhotoImage(self.img_sys)
            self.lbl_pic_sys.config(image=self.ph_sys, bg="white")
            self.lbl_pic_sys.place(x=280, y=15)
            
            result = self.win_change(user, sys)
            if result == "user":
                self.lbl_result.configure(text="User Win", text_color="#57b0d4")
                self.lbl_result.place(x=200, y=10)
                self.lbl_count_user.configure(text=self.count_user, text_color="white")
            elif result == "sys":
                self.lbl_result.configure(text="System Win", text_color="#e62020")
                self.lbl_result.place(x=190, y=10)
                self.lbl_count_sys.configure(text=self.count_sys, text_color="#e62020")
            else:
                self.lbl_result.configure(text="Equal", text_color="#ffffff")
                self.lbl_result.place(x=210, y=10)

            # -------------- End Game
            self.end_game()
        else:
            messagebox.showerror("Error", "Please specify how many games to play")
        
        
if __name__ == "__main__":
    window = Game()
    window.mainloop()