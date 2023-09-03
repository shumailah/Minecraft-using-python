from tkinter import Button, Label, messagebox
#import tkMessageBox
import random
import minesweepsetting
import ctypes
import sys

class Cell:
    all=[]
    cellcount=minesweepsetting.cellscount
    cellcountlabelobject=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.isopened=False
        self.cellbuttonobj=None
        self.possiblemine=False
        self.x=x
        self.y=y
        #Append the object to the cell.all list 
        Cell.all.append(self)
    def createbuttonobj(self, location):
        btn=Button(
            #bg='Red',
            location,
            width=12,
            height=4,
            #chaning the text to be displayed from simply"Text" 
            # to a formatted string that prints the range imported from minesweeper
            #text=f"{self.x},{self.y}" 
        )  
#need to make the buttons left and right clickable also        
        btn.bind('<Button-1>', self.leftclick) 
        btn.bind('<Button-2>', self.rightclick)
        self.cellbuttonobj=btn
    
    @staticmethod
    def createcellcountlabel(location):
        lbl= Label(
            location,
            bg='RosyBrown2',
            text=f" Cells Left : {Cell.cellcount}",
            width=12,
            height=4,
            font=("", 30)
        )
        #return lbl
        Cell.cellcountlabelobject= lbl 
           
 #simple display of a message when we left-click       
    '''def leftclick(self, event):
        print(event)
        print("I am left clicked")'''
#if the chosen cell is a mine it turns background red
    def leftclick(self, action):
        if self.is_mine:
            self.showmine()
        else:
            if self.surroundedcellsmineslength==0:
                for cellobj in self.suroundedcells:
                    cellobj.showcell()
            self.showcell()
            #if no of mines is equal to the cells left, player won
            if Cell.cellcount==minesweepsetting.Minescount:
                messagebox.showerror("YOU WON", "Congratulations! You Won!")
                 
        #cancel left and right click events if cell is already opened:
        self.cellbuttonobj.unbind('<Button-1>')
        self.cellbuttonobj.unbind('<Button-2>')       
            
    def getcellbyaxis(self,x,y):
        #Return cell object based on a value of x and y
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell
    
    @property
    def suroundedcells(self):
        #print(self.getcellbyaxis(0,0))
        cells=[
            self.getcellbyaxis(self.x,self.y+1),
            self.getcellbyaxis(self.x,self.y-1),
            self.getcellbyaxis(self.x+1,self.y),
            self.getcellbyaxis(self.x-1,self.y),
            self.getcellbyaxis(self.x+1,self.y+1),
            self.getcellbyaxis(self.x+1,self.y-1),
            self.getcellbyaxis(self.x-1,self.y-1),
            self.getcellbyaxis(self.x-1,self.y+1)
        ]
        cells=[cell for cell in cells if cell is not None]
        #print(surroundedcells)
        return cells
    
    @property
    def surroundedcellsmineslength(self):
        count=0
        for cell in self.suroundedcells:
            if cell.is_mine:
                count+=1
        return count        
        
               
    def showcell(self):
        if not self.isopened:
            
        #decrease cell count each time, but only is cell not open
            Cell.cellcount-=1
#we started by printing the no.of mines in the console. Now we show it on the button.
        #print(self.surroundedcellsmineslength)
            self.cellbuttonobj.configure(text=self.surroundedcellsmineslength)
         #replace cell count with new count
            if Cell.cellcountlabelobject:
                Cell.cellcountlabelobject.configure(
                text=f" Cells Left : {Cell.cellcount}")
            #after marking it yello, but then left clicking, it should revert to normal color:
            self.cellbuttonobj.configure(
                highlightbackground='SystemButtonFace'
            )    
        #mark the cell as opened
            self.isopened= True
        
    def showmine(self):
        self.cellbuttonobj.config(highlightbackground='red')
        messagebox.showerror("GAME OVER", "Woops...you clicked on a mine!! GAME OVER")
        sys.exit() 
    
    def rightclick(self,event):
        if not self.possiblemine:
            self.cellbuttonobj.configure(
                highlightbackground='orange'
            ) 
            self.possiblemine=True
        else:
            self.cellbuttonobj.configure(
                highlightbackground='SystemButtonFace'
            )
            self.possiblemine=False    
        #print(event)
        #print("I am right clicked")  
    
#self.cellbuttonobj=btn  
    @staticmethod
    def randomisemines():
        #random.sample accepts the list first and then the number of objects to be chosen randomly
        '''mlist = ['a','b','c','d']
        name=random.sample(mlist, 2)    
        print(name)'''
        minecells=random.sample(Cell.all, minesweepsetting.Minescount)
        #print(minecells)
        #(Converting some cells into mines):
        for minecells in minecells:
            minecells.is_mine = True
        
    
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
        
      
         