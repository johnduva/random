# Determine fewest number of moves it takes to get a knight at location [6,6] to the bishop at [4,4] 
# without landing on any of the diagonal spaces threatened by the bishop.
# If there is no solution then return -1.
# Note: Size of chess board is 8x8 (base 0)

import numpy as np

bishopRow = 4
bishopCol = 4

startRow = 6
startCol = 6

# Determine which spaces are threatened by the Bish[op
unmovable = []
for i in range(0,7):
    
    if bishopRow-i < 0 or bishopCol-i <0:
        continue
    else:
        unmovable.append([bishopRow-i, bishopCol-i])
                 
    if bishopRow+i > 7 or bishopCol+i > 7:
        continue
    else:
        unmovable.append([bishopRow+i, bishopCol+i])
    
    if bishopRow-i < 0 or bishopCol+i > 7:
        continue
    else:
        unmovable.append([bishopRow-i, bishopCol+i])
        
    if bishopRow+i > 7 or bishopCol-i < 0:
        continue
    else:
        unmovable.append([bishopRow+i, bishopCol-i])
    
    while [4,4] in unmovable:
        unmovable.remove([4,4])
    
# Determine all allowable moves by the knight that either move it closer to the bishop or maintain the same distance.
# Note:: Remember that you cannot land on a threatened spot
knight = [[startRow, startCol]]
bishop = [bishopRow, bishopCol]
count = 1
while bishop not in knight:
    possible = len(knight)
    for i,locations in enumerate(knight):
        row = locations[0]
        col =locations[1]
        dist = [bishop[0]-row, bishop[1]-col] 
                
        new = [bishopRow-(row+2), bishopCol-(col+1)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row+2, col+1])
        
        new = [bishopRow-(row+1), bishopCol-(col+2)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row+1, col+2])
        
        new = [bishopRow-(row+2), bishopCol-(col-1)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row+2, col-1])
        
        new = [bishopRow-(row+1), bishopCol-(col-2)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row+1, col-2])
        
        new = [bishopRow-(row-2), bishopCol-(col+1)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row-2, col+1])
        
        new = [bishopRow-(row-1), bishopCol-(col+2)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row-1, col+2])
        
        new = [bishopRow-(row-2), bishopCol-(col-1)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row-2, col-1])
        
        new = [bishopRow-(row-1), bishopCol-(col-2)]
        if abs(sum(new)) <= abs(sum(dist)) and new not in unmovable:
            knight.append([row-1, col-2])
            
        for i in range(0,possible):
            knight.pop(0)
    count += 1
    print(count)
        
    if count == 10:
        break
print("No solution")
            
