import tkinter

def place_symbol(i,j):
    print ("click",i,j)

    clicked_button = listButton[i][j]
    clicked_button.config(text="X")

def draw_grid():
    for i in range(3):
        buttons_in_cols = []  
      
        for j in range(3):
            button = tkinter.Button(root, width=5, height=2 , font=("Arial", 50),command=lambda r=i, c=j:place_symbol(r,c))
            button.grid(row=i, column=j,)
            
            buttons_in_cols.append(button)
        listButton.append(buttons_in_cols)              
            
   

#stockages button

listButton = [

]





#fenetre jeu

root = tkinter.Tk()


root.title=("TICTACTOE")
root.minsize(500,500)


draw_grid()

root.mainloop()