def checkmate(board_str):
    # 1.ตัดช่องว่างหัวท้าย และกรองบรรทัดว่างออก
    rows = [line.strip() for line in board_str.strip().split('\n') if line.strip()]
    
    if not rows:
        return
    
    size = len(rows)
    # แปลงเป็น List 2 มิติ
    board = [list(row) for row in rows]
    
    # 2. ค้นหาตำแหน่ง King (K)
    king_pos = None
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos: break

    if not king_pos:
        return # ถ้าหา King ไม่เจอไม่ต้องทำต่อ [cite: 58]

    kr, kc = king_pos

    # 3. เช็ค Pawn (P) - กรณีบุกจากล่างขึ้นบน
    pawn_checks = [(1, -1), (1, 1)]
    for dr, dc in pawn_checks:
        nr, nc = kr + dr, kc + dc
        if 0 <= nr < size and 0 <= nc < size:
            if board[nr][nc] == 'P':
                print("Success")
                return

    # 4. เช็คหมากทางไกล (B, R, Q) [cite: 80, 83, 96, 104]
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