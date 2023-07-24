import os

"""
create small basic maze
    - function for player movement with collision detection
    - function for printing/updating the map
    - funciton for winning
    - potential function for welcome screen
"""

board = [
    '|', '‾', '‾', '‾','‾', '‾' ,'‾','‾', '‾', '‾','‾', '‾', '‾', '|',
    '|', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ', '|',
    '|', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ', '|',
    '|', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ', '|',
    '|', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ', '|',
    '|', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ', '|',
    '|', '_', '_', '_','_', '_','_','_', '_', '_','_', '_', '_', '|'
]

count = 0
for i in board:
    if count % 14 == 0:
        print()
    print(i, end='')
    count += 1