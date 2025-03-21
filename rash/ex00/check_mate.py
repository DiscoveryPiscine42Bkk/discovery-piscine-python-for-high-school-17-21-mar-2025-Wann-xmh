#!/bin/env python3

def check_num_K(board):
    num_K=sum(row.count('K') for row in board)  # นับ 'K' ในแต่ละแถวแล้วรวมกัน
    if num_K != 1:
        print("Error!!")
    else :
        return True
def check_square(board):
    row_length = len(board[0])  # Get the length of the first row
    if all(len(row) == row_length for row in board):
        True
        # print("The board is a square.")
    else:
        print("The board is not a square.")

def checkmate(board):
    check_num_K(board)
    check_square(board)
    success_or_fail=[]
    S_list=[]
    F_list=[]

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                Ky = i 
                Kx = j
                break
    # #เช็ค Pawn        
    for i in range(0,1):
        cell = board[Ky+1][Kx + 1]
        cell1 = board[Ky+1][Kx + 1]
        if cell in ('P'):
           success_or_fail.append("Success")
        if cell1 in ('P'):
           success_or_fail.append("Success")
        else:
            success_or_fail.append("Fail")
            break

    # เช็คแกนy=ค่าคงที่
    for i in range(1, len(board[0])):  # ตรวจสอบแนวนอน (ขวา)
        if(Kx + i) < len(board[0]):  # ป้องกัน index out of range
            cell = board[Ky][Kx + i]
            if cell in ('P', 'B', '.'):
                True #fail
            else:
                success_or_fail.append("Success")
                break 
    for i in range(1, len(board[0])):  # ตรวจสอบนอน (ซ้าย)
        if Kx - i >= 0:
                cell = board[Ky][Kx - i]
                if cell in ('P', 'B', '.'):
                    True
                else:
                    success_or_fail.append("Success")
                    break
        #   เจอตัวขวางที่ไม่ใช่ P, B หรือ . ก็จบการเช็ค
        
    # เช็คแกนx=ค่าคงที่
    #ขึ้น
    for i in range(1, len(board[0])):  # ตรวจสอบแนวนอน (ขวา)
        if Ky - i >= -1:  # ป้องกัน index out of range
            cell = board[Ky-i][Kx]
            if cell in ('P', 'B', '.'):
                True #fail
            else:
                success_or_fail.append("Success")
                break 
    #ลง
    for i in range(1, len(board[0])):  # ตรวจสอบแนวนอน (ขวา)
        if Ky + i < len(board):  # ป้องกัน index out of range
            cell = board[Ky+i][Kx]
            if cell in ('P', 'B', '.'):
                True #fail
            else:
                success_or_fail.append("Success")
                break 
                # เจอตัวขวางที่ไม่ใช่ P, B หรือ . ก็จบการเช็ค

    #ตรวจเส้นแนวแทยงด้วยความชัน=1
    #Q1
    for i in range(1, len(board)):  
        if (Ky + i <= len(board)) and (Kx - i >= 0 ):  # ป้องกัน IndexError
            cell = board[Ky + i][Kx - i]
            if cell in ('P', 'R', '.'):  # ถ้าเจอ P, R, หรือ . ให้ล้มเหลว
                #faile
                #Q2
                for i in range(1, len(board)):  
                   if ((Ky - i >= 0)) and (Kx - i >= 0 ):  # ป้องกัน IndexError
                        cell = board[Ky - i][Kx - i]
                        if cell in ('P', 'R', '.'):  # ถ้าเจอ P, R, หรือ . ให้ล้มเหลว
                           True #faile
                           #Q3
                           for i in range(1, len(board)):
                               if ((Ky - i >= 0)) and (Kx + i <= len(board)):  # ป้องกัน IndexError
                                    cell = board[Ky - i][Kx + i]
                                    if cell in ('P', 'R', '.'):  # ถ้าเจอ P, R, หรือ . ให้ล้มเหลว
                                        True #faile
                                        #Q4
                                        for i in range(1, len(board)): 
                                            if ((Ky + i <= len(board))) and (Ky + i <= len(board)):  # ป้องกัน IndexError
                                                cell = board[Ky + i][Kx + i]
                                                if cell in ('P', 'R', '.'):  # ถ้าเจอ P, R, หรือ . ให้ล้มเหลว
                                                    True #faile
                                                    success_or_fail.append("Fail")
                                                    break
                                                else:
                                                    success_or_fail.append("Success")
                                                    break
                                    else:
                                        success_or_fail.append("Success")
                                        break
                        else:
                           success_or_fail.append("Success")
                           break
            else:
                success_or_fail.append("Success")
                break
        for i in range(len(success_or_fail)):
            if success_or_fail[i] == 'Success':
              S_list.append(success_or_fail[i])
            else:
              F_list.append(success_or_fail[i])
    if len(S_list) > 0 :
        print("Success")
    elif len(S_list) == 0 :
        print("Fail")