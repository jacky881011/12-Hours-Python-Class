# widgets = GUI elements : buttons, textboxes , labels , images
# windows = serves as a container to hold or contain these widgets


from tkinter import *       # all features we need to use
window1 = Tk()              # instantiate an instance of a window
window1.geometry("500x500")        # set the windows size 
window1.title("Bro code first GUI program")

#icon = PhotoImage(file = 'logo1.jpg')      # change the icon from the window icon
#window1.iconphoto(True , icon )

window1.config(background= "#4167d9")      # can use google find "hex color picker" to choice the color you want ( copy the hex code )
window1.mainloop()          # place window on computer screen , listen for events 
