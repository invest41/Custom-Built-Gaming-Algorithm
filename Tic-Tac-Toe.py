# Positional Dictionary
dct = {
	1: (0,0),
	2: (1,0),
	3: (2,0),
	4: (0,1),
	5: (1,1),
	6: (2,1),
	7: (0,2),
	8: (1,2),
	9: (2,2)
}



def move(column, row, value = 'Y'):
 global a,b,c,d,e,f,g,h,i,j,r1,r2,r3,template
 b[row][column] = value
 r1,r2,r3 = b[0],b[1],b[2]
 [a,j,c],[d,e,f],[g,h,i] = r1, r2, r3
 print(f'''
+-------------------------+
|  {a}         {j}         {c}  |
|                         |
|                         |
|  {d}         {e}         {f}  |
|                         |
|                         |
|  {g}         {h}         {i}  |
+-------------------------+
''')



def cg():
 global check
 x = [1,2,3][:]
 while True:
   c1 = random.choice(x)-1
   c2 = random.choice(x)-1
   if check[c2][c1] == 'OCCUPIED': continue
   break
 move(c1, c2, 'X')
 check[c2][c1] = 'OCCUPIED'



def fc(col,ro):
 global check
 if not check[ro][col] == 'OCCUPIED':
  move(col,ro,'X')
  check[ro][col] = 'OCCUPIED'
 else: cg()



def id_win():
   # Identify Winner
   global w
   if a==j==c: w = a
   if d==e==f: w = d
   if g==h==i: w = g
   if a==d==g: w = a
   if j==e==h: w = j
   if c==f==i: w = c
   if a==e==i: w = a
   if c==e==g: w = c




import random
human = input('\nInput your name... ')
if len(human) < 1: human = 'Human'
comp, hum, interest, il,er = 0, 0, 0, 3, None
tme = f'''
   
   
+--------------------+
| Too many Errors... |
+--------------------+
   
   
   '''
nre = f'''
  
  
+----------------------------+
| No more room for Errors... |
+----------------------------+
   
   
   '''

while True:
 try:
  empty_board = [[1,2,3],[4,5,6],[7,8,9]]
  b = empty_board[:]
  check = [[1,2,3],[4,5,6],[7,8,9]]
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
 
 
 
  print(f'Welcome {human}, to this game of Tic-Tac-Toe...')
  print('''
RULES:
1) Input Number to make a valid move to that Number (i.e. input 9 to make a move to number 9)
2) Computer's symbol is always X, Your symbol is always Y
3) When same symbols occupy, 3 adjacent spaces the owner of the symbol, WINS... 
 ''')
  co,w= 0, None
  while True:
   if co == 0:
    move(1,1,'X')
    check[1][1] = 'OCCUPIED'
  
  
  
   #FINISHER  Code 😆🤤🤤
   # Loop hole: If there are 2 doubles, it gives preference to the first one's elif that it meets and if third space is occupied, it randomly selects instead of winning the game with that other double
   
   elif a==j: fc(2,0)
   elif a==c: fc(1,0)
   elif j==c: fc(0,0)
   elif d==e: fc(2,1)
   elif d==f: fc(1,1)
   elif e==f: fc(0,1)
   elif g==h: fc(2,2)
   elif g==i: fc(1,2)
   elif h==i: fc(0,2)
   elif a==d: fc(0,2)
   elif a==g: fc(0,1)
   elif d==g: fc(0,0)
   elif j==e: fc(1,2)
   elif j==h: fc(1,1)
   elif e==h: fc(1,0)
   elif c==f: fc(2,2)
   elif c==i: fc(2,1)
   elif f==i: fc(2,0)
   elif a==e: fc(2,2)
   elif a==i: fc(1,1)
   elif e==i: fc(0,0)
   elif c==e: fc(0,2)
   elif c==g: fc(1,1)
   elif e==g: fc(2,0)
  
   else: cg()
  
  
   # Identify Winner
   id_win()
   if w == 'X':
    comp +=1
    print(end='\n\n\n')
    print ('------- You LOST! ---------')
    break
   if w == 'Y':
    print(end='\n\n\n')
    print ('------- You WON! ---------')
    hum += 1
    break
  
  
   
   co += 1
   T = co == 5
   while True:
    try:
     if T : break
     m = int(input('Make your move to which number? '))
     c3,c4 = dct[m]
     if not check[c4][c3] == 'OCCUPIED': break
     print('\n\nOccupied!  Try again...\n\n')
     
 
     [a,j,c],[d,e,f],[g,h,i] = r1, r2, r3
    
    except KeyboardInterrupt: break
    except:
     if interest == il:
      print(tme)
   
      break
     interest+=1
     er = il-interest
     if er == 0:
      print(nre)
      continue
     else:
      print(f'''2.0


+------------------------------+
|  {er} more room for Errors...   |
+------------------------------+


   ''')
      continue
  
   move(c3, c4, 'Y'.upper())
   check[c4][c3] = 'OCCUPIED'
  
   
   # Identify Winner
   id_win()
   if w == 'X':
    comp +=1
    print(end='\n\n\n')
    print ('------- You LOST! ---------')
    break
   if w == 'Y':
    print(end='\n\n\n')
    print ('------- You WON! ---------')
    hum += 1
    break
   if T:
    print(end='\n\n\n')
    print ("------- It's a TIE! ---------")
    break
  
  
  
  print(end='\n\n\n')
  print(f'{human} {hum} - Computer {comp}')
  print(end='\n\n\n')
  que = input('Play Again? ').lower()
  if que.startswith('n') or que.startswith('do'): break
  elif not que.startswith('y') or que.startswith('pl'): lol
 
 
 except KeyboardInterrupt: break
 except:
  if interest == il:
   print(tme)
   
   break
  interest+=1
  er = il-interest
  if er == 0: print(nre)
  else: print(f'''


+------------------------------+
|  {er} more room for Errors...   |
+------------------------------+


   ''')
  continue


print(end='\n\n\n')
print ('------- GAME OVER ---------')
print(end='\n\n\n')
if hum > comp: print(f'{human} {hum} - Computer {comp}')
elif comp > hum: print(f'Computer {comp} - Human {hum}')
else: print(f'{human} {hum} - Computer {comp}')
