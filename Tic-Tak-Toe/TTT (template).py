def DisplayBoard(empty_board=''):
 empty_board = [[1,2,3],[4,5,6],[7,8,9]]
 b = empty_board[:]
 r1,r2,r3 = b[0],b[1],b[2]
 [a,j,c],[d,e,f],[g,h,i] = r1, r2, r3
 template = f'''
+-------------------------+
|  {a}         {j}         {c}  |
|                         |
|                         |
|  {d}         {e}         {f}  |
|                         |
|                         |
|  {g}         {h}         {i}  |
+-------------------------+
'''

co = 1
while True:
 b = ''
 break
 DisplayBoard()
 EnterMove(b)
 MakeListOfFreeFields(b)
 VictoryFor(b,sign)
 
