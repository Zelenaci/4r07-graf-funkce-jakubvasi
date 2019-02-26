#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:46:34 2019

@author: vas35137
"""

from random import randint
import tkinter as tk

class App(): 
    def __init__(self, master):        
        self.funSelect_vals = []
        self.used_operators = []
        
        self.x = 1
        self.y = 1
        self.oper = ""
        self.res = 0
        
        self.formula_labels = ["", "", "", "="]
        self.formula_label_objects = []
        
        self.score = [0, 0]
        self.score_labels = ["Správně: ", self.score[0], "Špatně: ", self.score[1]]
        self.score_label_objects = []
               
        #_________________________________W I D G E T S_________________________________#
        # Výběr funkce
        funSelect_frame = tk.Frame(master)
        funSelect_frame.grid(row = 0, sticky = "W")
        
        funSelect_label = tk.Label(funSelect_frame, text = "Výběr funkce:", font = ("Arial Black",16))
        funSelect_label.grid(row = 0, column = 0, columnspan = 4, sticky = "W")
        
        funSelect_labels = ["sin(x)", "cos(x)", "tan(x)", "x^2", "sqrt(x)", "log(x)", "10^x"]
        funSelect_rbuts = []
        
        for i in range(len(funSelect_labels)):
            self.funSelect_vals.append(tk.BooleanVar())
            funSelect_rbuts.append(
                    tk.Radiobutton(funSelect_frame, text = funSelect_labels[i], 
                                   variable = self.funSelect_vals[i], height=0, width = 5,
                                   font = ("Arial Black",12)))
            funSelect_rbuts[i].grid(row = 1+i//2, column = i%2, sticky = "W")
            
    def sth(self):
        pass
            


root = tk.Tk()
root.title("Pocitani pro ZS")
app = App(root)
root.mainloop()