# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:00:29 2019

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for the 'cannibal problem', the river is upstream and the boat is floated back

Suggested citation as computer software for reference:
Pan, Alan J. (2019). Cannibal Problem [Computer software]. Github repository <https://github.com/alanjpan/Cannibal-Problem>
"""

sideA = ['cannibal', 'cannibal', 'cannibal', 'vegetarian', 'vegetarian', 'vegetarian']
sideB = []
boat = []

actions = ['cannibal', 'vegetarian']

#action 1, action 2
memory = [[50, 50]]

select = 0
turn = 0
party = len(sideA)

while len(sideB) != party:
    cannibal_count = 0
    vegetarian_count = 0
    print('people on side A')
    for i in sideA:
        if i == 'cannibal':
            cannibal_count += 1
        elif i == 'vegetarian':
            vegetarian_count += 1
    print(sideA)
    if cannibal_count > vegetarian_count:
        print('the vegetarians were eaten by the cannibals on side A')
        break

    cannibal_count = 0
    vegetarian_count = 0
    print('people on side B')
    for i in sideB:
        if i == 'cannibal':
            cannibal_count += 1
        elif i == 'vegetarian':
            vegetarian_count += 1    
    print(sideB)
    if cannibal_count > vegetarian_count:
        print('the vegetarians were eaten by the cannibals on side B')
        break

    select = input()

    if select.startswith('can'):
        boat.append('cannibal')
        sideA.remove('cannibal')
    elif select.startswith('veg'):
        boat.append('vegetarian')
        sideA.remove('vegetarian')
    print(sideA)
    print(boat)

    if len(boat) == 2:
        sideB.append(boat[0])
        sideB.append(boat[1])
        boat.pop(0)
        boat.pop(0)
    print(sideB)
    print(boat)
