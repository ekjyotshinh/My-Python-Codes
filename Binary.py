#card locate
def check_lowest(cards,query,mid):
    if cards[mid]==query:
        if mid-1>0 and cards[mid-1]==query:
            return ('left')
        else:
            return ('found')
    elif cards[mid]<query:
        return ('left')
    elif cards[mid]>query:
        return ('right')

def locate_cards(cards,query):
    hi=len(cards)-1
    lo=0
    while lo<=hi:
        mid=(hi+lo)//2
        mid_number=cards[mid]
        #print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        result=check_lowest(cards,query,mid)
        if result==('found'):
            return mid
        elif result==('left'):
            hi=mid-1
        elif result==('right'):
            lo=mid+1

    return -1
# card rotation
def card_rotation(cards):
    hi=len(cards)-1
    lo=0
    while lo<=hi:
        mid=(hi+lo)//2
        mid_number=cards[mid]
        #print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid>0 and cards[mid]>cards[mid-1]:
           return mid
        elif cards[mid]>cards[hi]:
           hi=mid-1
        else:
            lo=mid+1
    return 0
#sorting cards for finding the card in rotated list
def card_rotation_locate(cards,query):pass
#locate card problem


test =[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}]

for n in range (len(test)):
   print (n)
   print(locate_cards(**test[n]['input']))
   print(locate_cards(**test[n]['input']) == test[n]['output'])


# card rotation problem
test_2 =[{'input': {'cards': [ 3, 1, 0, 13, 11, 10, 7, 4]}, 'output': 3},
 {'input': {'cards': [10, 7, 4, 3, 1, 0, 13, 11 ]}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1]}, 'output': 0},
 {'input': {'cards': [ 3, 3, 3, 2, 0, 0, 9, 9, 9, 6, 6, 5, 4, 4, 3]}, 'output':6},
 {'input': {'cards': [6]},'output':0},
{'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]},'output': 0}
 ]

for n in range (len(test_2)):
    print(n)
    print(card_rotation(**test_2[n]['input']))
    print(card_rotation(test_2[n]['input']['cards']) == test_2[n]['output'])
    #print (test[n]['output'])


