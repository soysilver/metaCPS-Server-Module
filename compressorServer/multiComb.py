import sqlite3
import packets
from itertools import product
import statistics

db = db = './database.db'
sGroup = []
mGroup = []
lGroup = []


targetPressure = 25
target = 600


def clearAllContainers():
    sGroup.clear()
    mGroup.clear()
    lGroup.clear()


def list_to_binary(lst):
    binary_str = ''.join(str(x) for x in lst)
    return int(binary_str, 2)

def sum_first_elements(set_data):
    return sum(int(item[0]) for item in set_data)

clearAllContainers()

def find_min_combination(valid_combinations):

    
    
    if not valid_combinations:
        return None     
    sorted_combinations = sorted(valid_combinations, key=lambda item: sum(subitem[1] for subitem in item))
    
    min_combination = sorted_combinations[0]  
    _index = len(sorted_combinations) // 2
    mid_combination = sorted_combinations[_index ]
    #max_combination = max(valid_combinations, key=lambda item: sum(subitem[1] for subitem in item))
    #min_combination = min(valid_combinations, key=lambda item: sum(subitem[1] for subitem in item))
    return min_combination, mid_combination

def optimalOp(targetPressure, target):
    scO = packets.SCOptData()
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    query = """
        SELECT Q, W, igv, "1", "2", "3", "4", "5", "6", "7", "8", "9"
        FROM pred 
        WHERE p = ? 
    """
    params = [targetPressure]
    cursor.execute(query, params)
    rows = cursor.fetchall()
    connection.close()

    clearAllContainers() 
    
    numList = [False, False, False, False, False, False, False, False, False]

    for row in rows:
        Q, W, igv, numList[0],numList[1],numList[2],numList[3],numList[4],numList[5],numList[6],numList[7],numList[8] = row
        n = list_to_binary(numList)

        if n<4:
            pass
            #lGroup.append((Q, W, igv, numList))
        elif 32>n>=4:
            mGroup.append((Q, W, igv, numList.copy()))
        elif  512>n>=32:
            sGroup.append((Q, W, igv, numList.copy()))

    #lGroup = [(308.106414794922, 8338.33203125, '0.0', [0, 0, 0, 0, 0, 0, 0, 1, 1]), (190.249298095703, 4130.66162109375, '0.0', [0, 0, 0, 0, 0, 0, 0, 1, 0]),(190.665145874023, 4173.97802734375, '0.0', [0, 0, 0, 0, 0, 0, 0, 0, 1])]
    lGroup = [(308.106414794922, 8338.33203125, '0.0', [0, 0, 0, 0, 0, 0, 0, 1, 1])]

    sGroup.append((0.0, 0.0, 0.0, numList))
    mGroup.append((0.0, 0.0, 0.0, numList))
    lGroup.append((0.0, 0.0, 0.0, numList))
    combinations = list(product(sGroup, mGroup, lGroup))

    if len(combinations)==0: 
        return scO
        
    listBlowerIds = []

    valid_combinations = [item for item in combinations if  target+50 > sum(subitem[0] for subitem in item) > target]
    if len(valid_combinations) ==0:
        return scO

    min_c, max_c = find_min_combination(valid_combinations)
    mQ = sum(subitem[0] for subitem in min_c)
    mW = sum(subitem[1] for subitem in min_c)
    for subitem in (item[3] for item in min_c):
        if subitem[0]==1:
            listBlowerIds.append(1)
        if subitem[1]==1:
            listBlowerIds.append(2)
        if subitem[2]==1:
            listBlowerIds.append(3)
        if subitem[3]==1:
            listBlowerIds.append(4)
        if subitem[4]==1:
            listBlowerIds.append(7)        
        if subitem[5]==1:
            listBlowerIds.append(8)  
        if subitem[6]==1:
            listBlowerIds.append(9)  
        if subitem[7]==1:
            listBlowerIds.append(5)  
        if subitem[8]==1:
            listBlowerIds.append(6)  

    scO.optSP = mW/mQ
    scO.optFlowrate = mQ
    scO.optTotalPowerConsumption =mW


    scO.listBlowerIds = listBlowerIds
    scO.optLengthOfSolution = len(listBlowerIds)

    mQ = sum(subitem[0] for subitem in max_c)
    mW = sum(subitem[1] for subitem in max_c)
    scO.randSP = mW/mQ
    scO.randFlowrate = mQ
    scO.randTotalPowerConsumption = mW

    lenth = 0

    for subitem in (item[3] for item in max_c):
        if subitem[0]==1:
            lenth =lenth +1
        if subitem[1]==1:
            lenth =lenth +1
        if subitem[2]==1:
            lenth =lenth +1
        if subitem[3]==1:
            lenth =lenth +1
        if subitem[4]==1:
            lenth =lenth +1       
        if subitem[5]==1:
            lenth =lenth +1
        if subitem[6]==1:
            lenth =lenth +1
        if subitem[7]==1:
            lenth =lenth +1
        if subitem[8]==1:
            lenth =lenth +1

    scO.randLengthOfSolution = lenth

    print(scO.__dict__)
    print("min: "+str(min_c))
    print("mid: "+str(max_c))
    return(scO)
        

ii = optimalOp(targetPressure, 750)
#print(ii.__dict__)