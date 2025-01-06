# import random
# from tkinter import *

# class GameApplication(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.grid()
#         self.master.title("2048")

#         self.main_frame = Frame(
#             self, bg = GameApplication.grid_color, bd = 3, width = 600, height = 600
#         )

#         self.main_frame.grid(pady = (120,0))

#         self.app_GUI()
#         self.start()

#         self.master.bind("<Left>",self.left_key)
#         self.master.bind("<Right>",self.right_key)
#         self.master.bind("<Up>",self.up_key)
#         self.master.bind("<Down>",self.down_key)

#         self.mainloop()

# #--- Color Chart ----

# grid_color = "#bbb0a9"
# emptyCelll_color = "#ffd1ae"
# winner_bg_color = "#ffcd06"
# loser_bg_color = "#a4958b"
# gameOver_fontColor = "#ffffff"

# cell_colors = {  
#     2: "#fcece1",  
#     4: "#f4e9cb",  
#     8: "#efb07c",  
#     16: "#f49444",  
#     32: "#ff7357",  
#     64: "#e54b2d",  
#     128: "#ece18f",  
#     256: "#fbe02c",  
#     512: "#ffda47",  
#     1024: "#ebb41e",  
#     2048: "#fbd84c"      
# }  

# cellNumber_color = {  
#     2: "#61544f",  
#     4: "#61544f",  
#     8: "#ffffff",  
#     16: "#ffffff",  
#     32: "#ffffff",  
#     64: "#ffffff",  
#     128: "#ffffff",  
#     256: "#ffffff",  
#     512: "#ffffff",  
#     1024: "#ffffff",  
#     2048: "#ffffff"  
# }

# scoreLabel_font = ("Grandview", 20)
# score_font = ("Verdana", 32, "bold")
# gameOver_font = ("Verdana", 48, "bold")
    
# cellNumber_font = {  
#     2: ("Verdana", 55, "bold"),  
#     4: ("Verdana", 55, "bold"),  
#     8: ("Verdana", 55, "bold"),  
#     16: ("Verdana", 50, "bold"),  
#     32: ("Verdana", 50, "bold"),  
#     64: ("Verdana", 50, "bold"),  
#     128: ("Verdana", 40, "bold"),  
#     256: ("Verdana", 40, "bold"),  
#     512: ("Verdana", 40, "bold"),  
#     1024: ("Verdana", 30, "bold"),  
#     2048: ("Verdana", 30, "bold"),  
# }  

# # --- App GUI ---

# def app_GUI(self):
#     self.cells = []
#     for i in range(4):
#         rows = []
#         for j in range(4):
#             frameCells = Frame(
#                 self.main_frame,
#                 bg = GameApplication.emptyCelll_color,
#                 width = 150,
#                 height = 150 
#             ) 
#             frameCells.grid(row = i, column = j, padx = 5, pady = 5)
#             cellNumber = Label(
#                 self.main_frame,
#                 bg = GameApplication.emptyCell_color
#             )
#             cellData = {"frame" : frameCells, "number" : cellNumber}
#             cellNumber.grid(row = i, column = j)
#             rows.append(cellData)
#         self.cells.append(rows)


# # --- Scoreboard ---

# score_frame = Frame(self)
# score_frame.place(relx = 0.5, y = 60, anchor = "center")
# Label(
#     score_frame,
#     text = "Score: ",
#     font = GameApplication.scoreLabel_font
# ).grid(row = 0)

# self.score_label = Label(score_frame, text = "0", font = GameApplication.score_font)
# self.score_label.grid(row = 1)


# # -- Start Game ---

# def start(self):
#     self.matrix = [[0] * 4 for _ in range(4)]

#     row = random.randint(0,3)
#     col = random.randint(0,3)

#     self.matrix[row][col] = 2
#     self.cells[row][col]["frame"].configure(bg = GameApplication.cell_colors[2])
#     self.cells[row][col]["number"].configure(
#         bg = GameApplication.cell_colors[2],
#         fg = GameApplication.cellNumber_color[2],   
#         font = GameApplication.cellNumber_font[2],
#         text = "2"
#     )

#     while(self.matrix[row][col] != 0):
#         row = random.randint(0,3)
#         col = random.randint(0,3)

#     self.matrix[row][col] = 2
#     self.cells[row][col]["frame"].configure(bg = GameApplication.cell_colors[2])
#     self.cells[row][col]["number"].configure(
#         bg = GameApplication.cell_colors[2],
#         fg = GameApplication.cellNumber_color[2],   
#         font = GameApplication.cellNumber_font[2],
#         text = "2"
#     )

#     self.score = 0

# def compress_cells(self):
#     matrixOne = [[0] * 4 for _ in range(4)]
#     for i in range(4):
#         positionFill = 0
#         for j in range(4):
#             if self.matrix[i][j] != 0:
#                 matrixOne[i][positionFill] = self.matrix[i][j]
#                 positionFill += 1
#     self.matrix = matrixOne

# def combine_cells(self):
#     for i in range(4):
#         for j in range(3):
#             if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j+1]:
#                 self.matrix[i][j] *= 2
#                 self.matrix[i][j+1] = 0
#                 self.score += self.matrix[i][j]

# def reverse_order(self):
#     matrixOne = []
#     for i in range(4):
#         matrixOne.append([])
#         for j in range(4):
#             matrixOne[i].append(self.matrix[i][3-j])
#     self.matrix = matrixOne


# def transpose_matrix(self):
#     matrixOne = [[0] * 4 for _ in range(4)]
#     for i in range(4):
#         for j in range(4):
#             matrixOne[i][j] = self.matrix[j][i]
#     self.marix = matrixOne

# # --- Add New Random Cell ---

# def insert_tile(self):
#     row = random.randint(0,3)
#     col = random.randint(0,3)

#     while(self.matrix[row][col] != 0):
#         row = random.randint(0,3)
#         col = random.randint(0,3)

#     self.matrix[row][col] = random.choice([2,4])

# # --- Update GUI ---

# def update_GUI(self):
#     for i in range(4):
#         for j in range(4):
#             cellValue = self.matrix[i][j]

#             if cellValue == 0:
#                 self.cells[i][j]["frame"].configure(bg = GameApplication.emptyCell_color)
#                 self.cells[i][j]["number"].configure(
#                     bg = GameApplication.emptyCell_color,
#                     text = ""
#                 )

#             else:
#                 self.cells[i][j]["frame"].configure(bg = GameApplication.cell_colors[cellValue])
#                 self.cells[i][j]["number"].cofigure(
#                     bg = GameApplication.cell_colors[cellValue],
#                     fg = GameApplication.cellNumber_color[cellValue],
#                     font = GameApplication.cellNumber_font[cellValue],
#                     text = str(cellValue)
#                 )

#     self.score_label.configure(text = self.score)
#     self.update_idletasks()

# # --- Key Bindings ---

# def left_key(self,event):
#     self.compress_cells()
#     self.combine_cells()
#     self.compress_cells()
#     self.insert_tile()

#     self.update_GUI()
#     self.gameover()

# def right_key(self,event):
#     self.reverse_order()
#     self.compress_cells()
#     self.combine_cells()
#     self.compress_cells()
#     self.reverse_order()
#     self.insert_tile()

#     self.update_GUI()
#     self.gameocer()

# def up_key(self,event):
#     self.transpose_matrix()
#     self.compress_cells()
#     self.combine_cells()
#     self.compress_cells()
#     self.transpose_matrix()
#     self.insert_tile()

#     self.update_GUI()
#     self.gameover()

# def down_key(self,event):
#     self.transpose_matrix()
#     self.reverse_order()
#     self.compress_cells()
#     self.combine_cells()
#     self.compress_cells()
#     self.reverse_order()
#     self.transpose_matrix()
#     self.insert_tile()

#     self.update_GUI()
#     self.gameover()

# def horizonta_move_exits(self):
#     for i in range(4):
#         for j in range(3):
#             if self.matrixp[i][j] == self.matrix[i][j+1]:
#                 return True
#             return False
        
# def vertical_move_exits(self):
#     for i in range(3):
#         for j in range(4):
#             if self.matrix[i][j] == self.matrix[i+1][j]:
#                 return True
#             return False

# def gameover(self):
#     if any(2048 in row for row in self.matrix):
#         gameOver_frame = Frame(
#             self.main_frame,
#             borderwidth=3
#         )
#         gameOver_frame.place(relx=0.5, rely=0.5, anchor="center")
#         Label(
#             gameOver_frame,
#             text="You Win!",
#             font=GameApplication.gameOver_font,
#             bg = GameApplication.winner_bg_color,
#             fg = GameApplication.gameOver_fontColor,
#         ).pack()

#     elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exits() and not self.vertical_move_exists():
#         gameOver_Frame = Frame(
#             self.main_frame,
#             borderwidth=3
#         )
#         gameOver_Frame.place(relx = 0.5, rely = 0.5, anchor = "center")
#         Label(
#             gameOver_Frame,
#             text = "Game Over!!",
#             bg = GameApplication.loser_bg_color,
#             fg = GameApplication.gameOver_fontColor,
#             font = GameApplication.gameOver_font
#         ).pack()


# def game():
#     GameApplication()

# if __name__ == "__main__":
#     game()

from tkinter import *

main = Tk()
main.mainloop()
