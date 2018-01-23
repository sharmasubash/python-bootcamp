
# create a board
board = [['(0,0)','(0,1)','(0,2)'],['(1,0)','(1,1)','(1,2)'],['(2,0)','(2,1)','(2,2)']]


# Rules of the Game


def rules():
    # Diagonally
    if board[0][0]==board[1][1]==board[2][2]:
        return 1
    elif board[2][0]==board[1][1]==board[0][2]:
        return  1
    # Horizontally    
    elif board[0][0]==board[1][0]==board[2][0]:
        return  1
    elif board[0][0]==board[0][1]==board[0][2]:
        return  1
    elif board[1][0]==board[1][1]==board[1][2]:
        return  1
    elif board[2][0]==board[2][1]==board[2][2]:
        return  1                           
    # Vertically
    elif board[0][0]==board[1][0]==board[2][0]:
        return  1
    elif board[0][1]==board[1][1]==board[2][1]:
        return  1
    elif board[0][2]==board[1][2]==board[2][2]:
        return  1
    else:
        lst = []
        for i in range(3):
            for j in range(3):
                lst.append(board[i][j])
        lst = set(lst)
        lst = list(lst)
        if len(lst)==2:
            return 0
        else:
            return 2
            

def moves():
    str_var = []
    for z in range(9):
        # first move
        if z == 0 or z == 1:
            print ("enter value")
            filler = raw_input()
            print ("enter the place, 0<=x<=2, 0<=y<=2")
            x = int(raw_input());
            y = int(raw_input());
            for i in range(3):
                if i==x:
                    for j in range(3):
                        if j == y:
                            board[i][j]=filler
                            str_var.append(filler); 
                            print str_var
                            for rows in board:
                                print rows       
        elif z >= 2:
            print ("enter value")
            filler = raw_input()
            str_var.append(filler);
            if str_var[z]!=str_var[z-1]:
                print ("enter the place, 1<=x<=3, 1<=y<=3")
                x = int(raw_input());
                y = int(raw_input());
                for i in range(3):
                    if i==x:
                        for j in range(3):
                            if j == y:
                                board[i][j]=filler
                                for rows in board:
                                    print rows
                                blank = rules()
                                if int(blank) == 1:
                                    print ("Game Own")
                                elif int(blank)== 2:
                                    print ("Please Continue")
                                elif int(blank)==0:
                                    print ("Game Draw")
                                else:
                                    continue;
            else:
                print ("Wrong Move")
            if int(blank) == 1:
                break; 
            elif int(blank)==0:
                print ("Game Draw")

moves()  

                  
            