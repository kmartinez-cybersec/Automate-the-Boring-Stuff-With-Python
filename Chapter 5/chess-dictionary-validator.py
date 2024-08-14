def isValidChessBoard(board): # Function to check if a dictionary for a chessboard is valid
    # Set starting values for white and black pieces, kings, and pawns
    wPieceCount = 0
    bPieceCount = 0
    bKingCount = 0
    wKingCount = 0
    bPawnCount = 0
    wPawnCount = 0

    # Setting list values for valid coordindates' second character, valid teams, and valid piece types
    coords2ndcharacter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    teams = ['b', 'w']
    validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    # Checking if coordinates are valid
    for k in board.keys():
        coords = list(k)
        # Checking if first character of coordinates between 1 and 8
        if 0 > int(coords[0]) or int(coords[0]) > 8:
            return False
        # Checking if second character of coordinates between 'a' and 'h'
        if str(coords[1]) not in coords2ndcharacter:
            return False

    # Checking if pieces are valid
    for v in board.values():
        piece = list(v)
        #Checking if piece types are valid
        if len(piece) == 5:
            if str(piece[1] + piece[2] + piece[3] + piece[4]) not in validPieces:
                return False
        if len(piece) == 6:
            if str(piece[1] + piece[2] + piece[3] + piece[4] + piece[5]) not in validPieces:
                return False
        if len(piece) == 7:
            if str(piece[1] + piece[2] + piece[3] + piece[4] + piece[5] + piece[6]) not in validPieces:
                return False
        # Counting pieces for each team
        if piece[0] == 'b':
            bPieceCount += 1
        if piece[0] == 'w':
            wPieceCount += 1
        # Counting pawns for each team
        if v == 'bpawn':
            bPawnCount += 1
        if v == 'wpawn':
            wPawnCount += 1
        # Checking if pieces have valid teams
        if piece[0] not in teams:
            return False

    # Checking if piece counts for either team is more than 16
    if bPieceCount > 16 or wPieceCount > 16:
        return False
    # Checking if pawn counts for either team is more than 8
    if bPawnCount > 8 or wPawnCount > 8:
        return False
    # Checking if each team has a king
    if 'bking' not in board.values():
        return False
    if 'wking' not in board.values():
        return False
    else:
        return True

# Board to be checked if valid
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '3e': 'wking'}

print(isValidChessBoard(chessBoard))
