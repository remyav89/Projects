'''Bg_Size=int(input("enter the size"))

i=0
for i in range(Bg_Size):
    hl = (" --" * Bg_Size)
    vl = (" |" * Bg_Size)
print(hl)
print(vl)'''
board_size = int(input("What size of game board? "))

def print_horiz_line():
    print(" --- " * board_size)

 def print_vert_line():
     print("|   " * (board_size)+1)
    board_size = int(input("What size of game board? "))

  if __name__ == "__main__":
    board_size = int(input("What size of game board? "))

    for index in range(board_size):
      print_horiz_line()
      print_vert_line()
    #print horiz_line()