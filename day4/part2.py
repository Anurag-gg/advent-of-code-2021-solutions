a = ['63', '23', '2', '65', '55', '94', '38', '20', '22', '39', '5', '98', '9', '60', '80', '45', '99', '68', '12', '3', '6', '34', '64', '10', '70', '69', '95', '96', '83', '81', '32', '30', '42', '73', '52', '48', '92', '28', '37', '35', '54', '7', '50', '21', '74', '36', '91', '97', '13', '71', '86', '53', '46', '58', '76', '77', '14', '88', '78', '1', '33', '51', '89', '26', '27', '31', '82', '44', '61', '62', '75', '66', '11', '93', '49', '43', '85', '0', '87', '40', '24', '29', '15', '59', '16', '67', '19', '72', '57', '41', '8', '79', '56', '4', 
'18', '17', '84', '90', '47', '25']

boards = []

with open("day4/data.txt", 'r') as data:
    temp_board = []
    for x in data:
        if(x.split()):
            temp_board.append(x.split())
        else:
            boards.append(temp_board)
            temp_board = []

def calc(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != '*':
                sum += int(board[i][j])
    return sum

def isSolved(board):
    for i in range(5):
        flag = True
        for j in range(5):
            if board[i][j] != '*':
                flag = False
                break
        if(flag):
            return True

    for i in range(5):
        flag = True
        for j in range(5):
            if board[j][i] != '*':
                flag = False
                break
        if (flag):
            return True
    return False

def main():
    for number in a:
        for board in reversed(boards):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == number:
                        board[i][j] = '*'
            if isSolved(board):
                if(len(boards)==1):
                    print(calc(board) * int(number))
                    return
                boards.remove(board)
        


if __name__ == "__main__":
    main()
