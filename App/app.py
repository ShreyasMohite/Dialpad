


from tkinter import *
import pygame
import time

pygame.init()
class Shreyas:
    def __init__(self,root):
        self.root=root
        self.root.title("Dialpad")
        self.root.geometry("300x450")
        self.root.resizable(0,0)
        self.root.iconbitmap(r"C:\Users\SHREYAS\Desktop\shreyas python\ItemsRecorder\Images\logo488.ico")





#==================hover===========================#
       
        def on_enter1(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave1(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter2(e):
            but_erase['background']="black"
            but_erase['foreground']="cyan"  
        def on_leave2(e):
            but_erase['background']="SystemButtonFace"
            but_erase['foreground']="SystemButtonText"


        def on_enter3(e):
            but_one['background']="black"
            but_one['foreground']="cyan"  
        def on_leave3(e):
            but_one['background']="SystemButtonFace"
            but_one['foreground']="SystemButtonText"

        def on_enter4(e):
            but_two['background']="black"
            but_two['foreground']="cyan"  
        def on_leave4(e):
            but_two['background']="SystemButtonFace"
            but_two['foreground']="SystemButtonText"

        def on_enter5(e):
            but_three['background']="black"
            but_three['foreground']="cyan"  
        def on_leave5(e):
            but_three['background']="SystemButtonFace"
            but_three['foreground']="SystemButtonText"

        def on_enter6(e):
            but_four['background']="black"
            but_four['foreground']="cyan"  
        def on_leave6(e):
            but_four['background']="SystemButtonFace"
            but_four['foreground']="SystemButtonText"

        def on_enter7(e):
            but_five['background']="black"
            but_five['foreground']="cyan"  
        def on_leave7(e):
            but_five['background']="SystemButtonFace"
            but_five['foreground']="SystemButtonText"

        def on_enter8(e):
            but_six['background']="black"
            but_six['foreground']="cyan"  
        def on_leave8(e):
            but_six['background']="SystemButtonFace"
            but_six['foreground']="SystemButtonText"

        def on_enter9(e):
            but_seven['background']="black"
            but_seven['foreground']="cyan"  
        def on_leave9(e):
            but_seven['background']="SystemButtonFace"
            but_seven['foreground']="SystemButtonText"

        def on_enter10(e):
            but_eight['background']="black"
            but_eight['foreground']="cyan"  
        def on_leave10(e):
            but_eight['background']="SystemButtonFace"
            but_eight['foreground']="SystemButtonText"

        def on_enter11(e):
            but_nine['background']="black"
            but_nine['foreground']="cyan"  
        def on_leave11(e):
            but_nine['background']="SystemButtonFace"
            but_nine['foreground']="SystemButtonText"

        def on_enter12(e):
            but_star['background']="black"
            but_star['foreground']="cyan"  
        def on_leave12(e):
            but_star['background']="SystemButtonFace"
            but_star['foreground']="SystemButtonText"

        def on_enter13(e):
            but_zero['background']="black"
            but_zero['foreground']="cyan"  
        def on_leave13(e):
            but_zero['background']="SystemButtonFace"
            but_zero['foreground']="SystemButtonText"

        def on_enter14(e):
            but_hash['background']="black"
            but_hash['foreground']="cyan"  
        def on_leave14(e):
            but_hash['background']="SystemButtonFace"
            but_hash['foreground']="SystemButtonText"

        def on_enter15(e):
            but_call['background']="black"
            but_call['foreground']="cyan"  
        def on_leave15(e):
            but_call['background']="SystemButtonFace"
            but_call['foreground']="SystemButtonText"







#===================function=========================#
        
        def clear():
            pygame.mixer.music.load(r"C:\Users\SHREYAS\Desktop\shreyas python\ItemsRecorder\sound\buttonpush.mp3")
            pygame.mixer.music.play()
            dailtext.delete('1.0',"end")


        def erase():
            pygame.mixer.music.load(r"C:\Users\SHREYAS\Desktop\shreyas python\ItemsRecorder\sound\buttonpush.mp3")
            pygame.mixer.music.play()
            dailtext.delete(1.0,"end")

        
        def click(numbers):
            #global operator
            operator=str(numbers)
            pygame.mixer.music.load(r"C:\Users\SHREYAS\Desktop\shreyas python\ItemsRecorder\sound\clicks.mp3")
            pygame.mixer.music.play()
            dailtext.insert("end",operator)

        def calling():
            pygame.mixer.music.load(r"C:\Users\SHREYAS\Desktop\shreyas python\ItemsRecorder\sound\ringing.mp3")
            pygame.mixer.music.play()


        
        
            
            


        

        
            


#===================mainframe========================#
        
        mainframe=Frame(self.root,width=300,height=450,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        dialframe=Frame(mainframe,width=294,height=100,relief="ridge",bd=3)
        dialframe.place(x=0,y=0)

        keyframe=Frame(mainframe,width=294,height=345,relief="ridge",bd=3,bg="gray77")
        keyframe.place(x=0,y=100)


#=====================dialframe================================#
        
        dailtext=Text(dialframe,width=20,height=1,font=('times new roman',20))
        dailtext.place(x=2,y=0)

        but_clear=Button(dialframe,text="Clear",width=10,font=('times new roman',15),cursor="hand2",command=clear)
        but_clear.place(x=10,y=50)
        but_clear.bind("<Enter>",on_enter1)
        but_clear.bind("<Leave>",on_leave1)


        but_erase=Button(dialframe,text="Erase",width=10,font=('times new roman',15),cursor="hand2",command=erase)
        but_erase.place(x=155,y=50)
        but_erase.bind("<Enter>",on_enter2)
        but_erase.bind("<Leave>",on_leave2)


#====================================================#


        but_one=Button(keyframe,text="1",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(1))
        but_one.place(x=3,y=25)
        but_one.bind("<Enter>",on_enter3)
        but_one.bind("<Leave>",on_leave3)

        but_two=Button(keyframe,text="2",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(2))
        but_two.place(x=98,y=25)
        but_two.bind("<Enter>",on_enter4)
        but_two.bind("<Leave>",on_leave4)

        but_three=Button(keyframe,text="3",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(3))
        but_three.place(x=195,y=25)
        but_three.bind("<Enter>",on_enter5)
        but_three.bind("<Leave>",on_leave5)


        but_four=Button(keyframe,text="4",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(4))
        but_four.place(x=3,y=95)
        but_four.bind("<Enter>",on_enter6)
        but_four.bind("<Leave>",on_leave6)

        but_five=Button(keyframe,text="5",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(5))
        but_five.place(x=98,y=95)
        but_five.bind("<Enter>",on_enter7)
        but_five.bind("<Leave>",on_leave7)

        but_six=Button(keyframe,text="6",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(6))
        but_six.place(x=195,y=95)
        but_six.bind("<Enter>",on_enter8)
        but_six.bind("<Leave>",on_leave8)


        but_seven=Button(keyframe,text="7",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(7))
        but_seven.place(x=3,y=165)
        but_seven.bind("<Enter>",on_enter9)
        but_seven.bind("<Leave>",on_leave9)

        but_eight=Button(keyframe,text="8",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(8))
        but_eight.place(x=98,y=165)
        but_eight.bind("<Enter>",on_enter10)
        but_eight.bind("<Leave>",on_leave10)

        but_nine=Button(keyframe,text="9",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(9))
        but_nine.place(x=195,y=165)
        but_nine.bind("<Enter>",on_enter11)
        but_nine.bind("<Leave>",on_leave11)

        but_star=Button(keyframe,text="*",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click('*'))
        but_star.place(x=3,y=235)
        but_star.bind("<Enter>",on_enter12)
        but_star.bind("<Leave>",on_leave12)

        but_zero=Button(keyframe,text="0",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click(0))
        but_zero.place(x=98,y=235)
        but_zero.bind("<Enter>",on_enter13)
        but_zero.bind("<Leave>",on_leave13)

        but_hash=Button(keyframe,text="#",width=7,font=('times new roman',15),cursor="hand2",command=lambda:click('#'))
        but_hash.place(x=195,y=235)
        but_hash.bind("<Enter>",on_enter14)
        but_hash.bind("<Leave>",on_leave14)

        but_call=Button(keyframe,text="Call",width=7,font=('times new roman',15),cursor="hand2",command=calling)
        but_call.place(x=98,y=295)
        but_call.bind("<Enter>",on_enter15)
        but_call.bind("<Leave>",on_leave15)










if __name__=="__main__":
    root=Tk()
    Shreyas(root)
    root.mainloop()