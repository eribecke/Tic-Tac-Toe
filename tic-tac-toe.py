table = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def tic_table(table):
    count = 0
    
    while table:
        if count%2 == 0:
            p1 = str(input("Player 1, please indicate which spot on the board you would like to take. Options: TopL, TopM, TopR, MidL, MidM, MidR, BotL, BotM, BotR: "))
            if p1 == "TopL":
                table[0][0] = "X"
            if p1 == "TopM":
                table[0][1] = "X"
            if p1 == "TopR":
                table[0][2] = "X"
            if p1 == "MidL":
                table[1][0] = "X"
            if p1 == "MidM":
                table[1][1] = "X"
            if p1 == "MidR":
                table[1][2] = "X"
            if p1 == "BotL":
                table[2][0] = "X"
            if p1 == "BotM":
                table[2][1] = "X"
            if p1 == "BotR":
                table[2][2] = "X"
        if count%2 == 1:
            p2 = input("Player 2, please indicate which spot on the board you would like to take. Options: TopL, TopM, TopR, MidL, MidM, MidR, BotL, BotM, BotR: ")
            if p2 == "TopL":
                table[0][0] = "O"
            if p2 == "TopM":
                table[0][1] = "O"
            if p2 == "TopR":
                table[0][2] = "O"
            if p2 == "MidL":
                table[1][0] = "O"
            if p2 == "MidM":
                table[1][1] = "O"
            if p2 == "MidR":
                table[1][2] = "O"
            if p2 == "BotL":
                table[2][0] = "O"
            if p2 == "BotM":
                table[2][1] = "O"
            if p2 == "BotR":
                table[2][2] = "O"

        for row in range(len(table)):
            if table[row][0] == table[row][1] == table[row][2] and table[row][0] != "-":
                return "Game Over"
            if table[0][row] == table[1][row] == table[2][row] and table[0][row] != "-":
                return "Game Over"
            if table[0][0] == table[1][1] == table[2][2] and table [0][0] != "-" or table[0][2] == table [1][1] == table[2][0] and table[0][2] != "-":
                return "Game Over"
        print(table[0])
        print(table[1])
        print(table[2])
        count += 1
    
print(tic_table(table))