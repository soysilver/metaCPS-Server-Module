import sqlite3
import packets
from itertools import chain


'''
This file just sets up server and returns optimal combination 
pretty much original code
may be modified
'''



db = './database.db'

b1Rows = []
b2Rows = []
b3Rows = []
b4Rows = []
b7Rows = []
b8Rows = []
b9Rows = []

sGroup = []
mGroup = []
lGroup = []

listBlowerIds = []

selectedBlowers = {}

def clearAllContainers():
    b1Rows.clear()
    b2Rows.clear()
    b3Rows.clear()
    b4Rows.clear()
    b7Rows.clear()
    b8Rows.clear()
    b9Rows.clear()
    sGroup.clear()
    mGroup.clear()
    lGroup.clear()
    listBlowerIds.clear()
    selectedBlowers.clear()


def combination2(list1, list2):
    if list1 is None or list2 is None:
        raise ValueError("Both lists must be non-null")
    return [(item1, item2) for item1 in list1 for item2 in list2]


def chooseMost2():
    # Generate combinations between pairs of lists
    combinations_list = list(chain(
        combination2(b1Rows, b7Rows),
        combination2(b1Rows, b8Rows),
        combination2(b1Rows, b9Rows),
        combination2(b2Rows, b7Rows),
        combination2(b2Rows, b8Rows),
        combination2(b2Rows, b9Rows),
        combination2(b3Rows, b7Rows),
        combination2(b3Rows, b8Rows),
        combination2(b3Rows, b9Rows),
        combination2(b4Rows, b7Rows),
        combination2(b4Rows, b8Rows),
        combination2(b4Rows, b9Rows),
        [[item] for item in b1Rows],
        [[item] for item in b2Rows],
        [[item] for item in b3Rows],
        [[item] for item in b4Rows],
        [[item] for item in b7Rows],
        [[item] for item in b8Rows],
        [[item] for item in b9Rows]
    ))
    return combinations_list

def combination3(list1, list2, list3):
    if list1 is None or list2 is None or list3 is None:
        raise ValueError("all lists must be non-null")
    return [(item1, item2, item3) for item1 in list1 for item2 in list2 for item3 in list3]


def chooseMost3():
    # Generate combinations between pairs of lists
    combinations_list = list(chain(
        combination3(b1Rows, b2Rows, b7Rows),
        combination3(b1Rows, b3Rows, b7Rows),
        combination3(b1Rows, b4Rows, b7Rows),
        combination3(b2Rows, b3Rows, b7Rows),
        combination3(b2Rows, b4Rows, b7Rows),
        combination3(b3Rows, b4Rows, b7Rows),
        combination3(b1Rows, b2Rows, b8Rows),
        combination3(b1Rows, b3Rows, b8Rows),
        combination3(b1Rows, b4Rows, b8Rows),
        combination3(b2Rows, b3Rows, b8Rows),
        combination3(b2Rows, b4Rows, b8Rows),
        combination3(b3Rows, b4Rows, b8Rows),
        combination3(b1Rows, b2Rows, b9Rows),
        combination3(b1Rows, b3Rows, b9Rows),
        combination3(b1Rows, b4Rows, b9Rows),
        combination3(b2Rows, b3Rows, b9Rows),
        combination3(b2Rows, b4Rows, b9Rows),
        combination3(b3Rows, b4Rows, b9Rows),
        combination3(b1Rows, b7Rows, b8Rows),
        combination3(b1Rows, b7Rows, b9Rows),
        combination3(b1Rows, b8Rows, b9Rows),
        combination3(b2Rows, b7Rows, b8Rows),
        combination3(b2Rows, b7Rows, b9Rows),
        combination3(b2Rows, b8Rows, b9Rows),
        combination3(b3Rows, b7Rows, b8Rows),
        combination3(b3Rows, b7Rows, b9Rows),
        combination3(b3Rows, b8Rows, b9Rows),
        combination3(b4Rows, b7Rows, b8Rows),
        combination3(b4Rows, b7Rows, b9Rows),
        combination3(b4Rows, b8Rows, b9Rows),      
        combination2(b1Rows, b7Rows),
        combination2(b1Rows, b8Rows),
        combination2(b1Rows, b9Rows),
        combination2(b2Rows, b7Rows),
        combination2(b2Rows, b8Rows),
        combination2(b2Rows, b9Rows),
        combination2(b3Rows, b7Rows),
        combination2(b3Rows, b8Rows),
        combination2(b3Rows, b9Rows),
        combination2(b4Rows, b7Rows),
        combination2(b4Rows, b8Rows),
        combination2(b4Rows, b9Rows),
        [[item] for item in b1Rows],
        [[item] for item in b2Rows],
        [[item] for item in b3Rows],
        [[item] for item in b4Rows],
        [[item] for item in b7Rows],
        [[item] for item in b8Rows],
        [[item] for item in b9Rows]
    ))
    return combinations_list

def sum_first_elements(set_data):
    return sum(int(item[0]) for item in set_data)


def optimalOp(targetPressure, target):
    scO = packets.SCOptData()
    clearAllContainers()   
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    clearAllContainers()
    # Query for blowers with specific conditions
    cursor.execute(f"SELECT Q, W, igv, num FROM pred2 WHERE p = {targetPressure} AND num IN (5, 6) AND igv = 0")
    rows = cursor.fetchall()
    for row in rows:
        Q, W, igv, num = row
        selectedBlowers[num] = (Q, W, igv)
        lGroup.append((Q, W, igv, num))

    # Fetch data for other blowers
    num_list = [1, 2, 3, 4]
    for num in num_list:
        cursor.execute(f"SELECT Q, W, igv FROM pred2 WHERE p = {float(targetPressure)} AND num = {int(num)} AND igv > 0.0 AND igv <= 50")
        rows = cursor.fetchall()
        print(rows, targetPressure, num)
        for row in rows:
            Q, W, igv= row
            if num == 1:
                b1Rows.append((Q, W, igv, num))
            elif num == 2:
                b2Rows.append((Q, W, igv, num))
            elif num == 3:
                b3Rows.append((Q, W, igv, num))
            elif num == 4:
                b4Rows.append((Q, W, igv, num))
            sGroup.append((Q, W, igv, num))


    # Fetch data for mGroup blowers
    m_num_list = [7, 8, 9]
    for num in m_num_list:
        cursor.execute(f"SELECT Q, W, igv, num FROM pred2 WHERE p = ? AND num = ? AND igv > 0.0 AND igv <= 50", (targetPressure, num))
        rows = cursor.fetchall()
        for row in rows:
            Q, W, igv, num = row
            if num == 7:
                b7Rows.append((Q, W, igv, num))
            elif num == 8:
                b8Rows.append((Q, W, igv, num))
            elif num == 9:
                b9Rows.append((Q, W, igv, num))
            mGroup.append((Q, W, igv, num))

    connection.close()

    base = 0
    if 5 in selectedBlowers and 6 in selectedBlowers:
        base = float(selectedBlowers[5][0]) + float(selectedBlowers[6][0])
        print(f"Base value: {base}")

    if target > base:
        diff = target-base
        step2 = None
        step3 = None
        random = None
        valid = []
        min2W = float('inf')
        min3W = float('inf')
        nowQ = 1000
        
        for combo in chooseMost2():
            total_Q = sum(float(row[0]) for row in combo)
            total_W = sum(float(row[1]) for row in combo)

            if total_Q >= diff and total_Q <= diff+10 and total_W < min2W:
                nowQ = total_Q
                min2W = total_W
                step2 = combo
                    
        for combo in chooseMost3():
            total_Q = sum(float(row[0]) for row in combo)
            total_W = sum(float(row[1]) for row in combo)


            if total_Q >= diff and total_Q <= diff+10 and total_W < min3W:
                min3W = total_W
                nowQ = total_Q
                step3 = combo
                valid.append(combo)

        if len(valid)!=0:
           max_sum = -1
           for v in valid:
                total_sum = sum(int(item[0]) for item in v)  # Item1 값들의 합을 계산

                if total_sum > max_sum:
                    max_sum = total_sum
                    random =v
               

        if step2 is None and step3 is None:
            print("No Solution Found")
        elif step2 is None:
            step3 = list(step3) + lGroup

            #print("step3 Best Combination:")
            Q = 0.0
            W = 0.0

            # step3에 l_group을 추가하고, 각 row의 값 처리
            for row in step3:
                Q += float(row[0])
                W += float(row[1])
                listBlowerIds.append(row[3])
                #print(f"Key: {row[3]}, Values: Q={row[0]}, W={row[1]}, Igv={row[2]}")

            scO.optSP = W / Q
            scO.optFlowrate = Q
            scO.optTotalPowerConsumption = W
            scO.optLengthOfSolution = len(step3)
                    
        elif step3 is None:         
            step2 = list(step2) + lGroup

            #print("step3 Best Combination:")
            Q = 0.0
            W = 0.0

            # step3에 l_group을 추가하고, 각 row의 값 처리
            for row in step2:
                Q += float(row[0])
                W += float(row[1])

                #print(f"Key: {row[3]}, Values: Q={row[0]}, W={row[1]}, Igv={row[2]}")

            scO.optSP = W / Q
            scO.optFlowrate = Q
            scO.optTotalPowerConsumption = W
            scO.optLengthOfSolution = len(step2)

        elif step2 is not None and min3W >= min2W: 
            step2 = list(step2) + lGroup

            #print("1step3 Best Combination:")
            Q = 0.0
            W = 0.0

            # step3에 l_group을 추가하고, 각 row의 값 처리
            for row in step2:
                Q += float(row[0])
                W += float(row[1])
                listBlowerIds.append(row[3])
                #print(f"Key: {row[3]}, Values: Q={row[0]}, W={row[1]}, Igv={row[2]}")

            scO.optSP = W / Q
            scO.optFlowrate = Q
            scO.optTotalPowerConsumption = W
            scO.optLengthOfSolution = len(step2)

        elif step3 is not None and min3W < min2W: 
            step3 = step3 + lGroup

            #print("step3 Best Combination:")
            Q = 0.0
            W = 0.0

            # step3에 l_group을 추가하고, 각 row의 값 처리
            for row in step3:
                Q += float(row[0])
                W += float(row[1])
                listBlowerIds.append(row[3])
                #print(f"Key: {row[3]}, Values: Q={row[0]}, W={row[1]}, Igv={row[2]}")

            scO.optSP = W / Q
            scO.optFlowrate = Q
            scO.optTotalPowerConsumption = W
            scO.optLengthOfSolution = len(step3)

        if random is not None:
            Q = 0.0
            W = 0.0
            random = list(random) + lGroup
            # step3에 l_group을 추가하고, 각 row의 값 처리
            for row in random:
                Q += float(row[0])
                W += float(row[1])
                #print(f"Key: {row[3]}, Values: Q={row[0]}, W={row[1]}, Igv={row[2]}")

            scO.randSP = W / Q
            scO.randFlowrate = Q
            scO.randTotalPowerConsumption = W
            scO.randLengthOfSolution = len(random)
        
        scO.listBlowerIds = listBlowerIds
    return scO
a = optimalOp(40, 700)
print(a.__dict__)