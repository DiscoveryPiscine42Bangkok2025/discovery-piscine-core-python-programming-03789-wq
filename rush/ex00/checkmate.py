def checkmate(board_str):
   rows = [line for line in board_str.strip().split('\n') if line.strip()]
  
   if not rows:
       print("Fail")
       return
  
   size_r = len(rows)    
  
   for row in rows:
       if len(row) != size_r:
           print("NOT Square")
           return


   # ถ้าผ่านการตรวจสอบ ให้สร้างบอร์ดและเริ่มหา King ต่อไป
   board = [list(row) for row in rows]
   size = size_r
  
   # 2. ค้นหาตำแหน่ง King (K)
   king_pos = None
   for r in range(size):
       for c in range(size):
           if board[r][c] == 'K':
               king_pos = (r, c)
               break
       if king_pos: break 


   if not king_pos:
       return 


   kr, kc = king_pos


   pawn_checks = [(1, -1), (1, 1)]
   for dr, dc in pawn_checks:
       nr, nc = kr + dr, kc + dc
       if 0 <= nr < size and 0 <= nc < size:
           if board[nr][nc] == 'P':
               print("Success")
               return


   directions = {
       'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
       'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
       'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
   }


   for piece_type, dirs in directions.items():
       for dr, dc in dirs:
           nr, nc = kr + dr, kc + dc
           while 0 <= nr < size and 0 <= nc < size:
               target = board[nr][nc]
               if target != '.':
                   # ถ้าเจอหมากที่รุกได้ในทิศทางนั้น [cite: 51, 55]
                   if target == piece_type or target == 'Q':
                       print("Success")
                       return
                   else:
                       # เจอหมากตัวอื่นขวางทาง [cite: 51]
                       break
               nr += dr
               nc += dc


   # 5. ถ้าไม่โดนรุกเลย
   print("Fail")