from tkinter import *

class AnimalApp:
    def __init__(self):
        self.animals = {'dog': '',
                        'cow':'',
                        'sheep':'',
                        'horse':'',
                        'cat':'',
                        'dog':''}
        self.image= None
        self.animal_choice = None
        self.enter_button = None
        self.animal_canvas = None
        self.main = Tk()
        
    def SetUpScreen(self):
        self.animal_choice = Entry(self.main)
        self.animal_choice.insert(0,'Favorite animal?')
        self.animal_choice.grid(row = 1, column=1 )
        
        #creates Button.
        self.enter_button = Button(self.main, text='Enter',command=self.ShowPic)
        self.enter_button.grid(row=1, column=2,sticky=W)
        self.animal_canvas= Canvas(self.main, width=400, height=400, background='purple')
        self.animal_canvas.grid(row=2,column=1,columnspan=2,rowspan=2)
        self.main.mainloop()
        
    def ShowPic(self):
        animal = self.animal_choice.get()
        animal_filename = self.amimals[animal]
        self.image=PhotImage(file=animal_filename)
        self.animal_canvas.delete(ALL)
        self.animal_canavas.create_image(200,200,image=self.image)
        
app=AnimalApp()
app.SetUpScreen()
        