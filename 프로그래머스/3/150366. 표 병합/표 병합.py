def solution(commands):
    answer = []
    
    arr = [["EMPTY" for i in range(51)] for i in range(51)]
    merge = [[(i, j) for j in range(51)] for i in range(51)]
    
    for command in commands:
        command = command.split()
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r, c = int(command[1]), int(command[2])
                x, y = merge[r][c]
                arr[x][y] = command[3]
            else:
                for i in range(1, 51):
                    for j in range(1, 51):
                        if arr[i][j] == command[1]:
                            arr[i][j] = command[2]
            
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            x1, y1 = merge[r1][c1]
            x2, y2 = merge[r2][c2]
            if arr[x1][y1] == "EMPTY":
                arr[x1][y1] = arr[x2][y2]
            
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] == (x2, y2):
                        merge[i][j] = (x1, y1)
            
            
        elif command[0] == 'UNMERGE':
            r, c = int(command[1]), int(command[2])
            x, y = merge[r][c]
            temp = arr[x][y]
            
            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] == (x, y):
                        merge[i][j] = (i, j)
                        arr[i][j] = "EMPTY"
            arr[r][c] = temp
            
        else:
            r, c = int(command[1]), int(command[2])
            x, y = merge[r][c]
            answer.append(arr[x][y])
    
    return answer