# Program to check if queen can attack on opponent

def attack(Q,O):
    if Q[0]==O[0]:                                  # same row
        return True
    if Q[1]==O[1]:                                  # same column
        return True
    if abs(Q[0]-O[0]) == abs(Q[1]-O[1]):            # diagonally
        return True
      
Q=(1,1)                                             # Queen's position
O=(3,3)                                             # Opponent's position

if __name__ == "__main__":
    val = attack(Q,O)
    if val :
        print("Queen can attack")
    else:
        print("Queen can not attack")
