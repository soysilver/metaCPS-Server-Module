import json



input = {"pid": 5,"category": 2, "mms": 7}
st = json.dumps(input, sort_keys=True)




def diagnosis(category, mms): 
    if category==1: 
        if mms < 0.28: 
            return "still"
        elif 0.28<= mms < 0.71: 
            return "good"
        elif 0.71<= mms < 1.80: 
            return "satisfactory"
        elif 1.80 <= mms < 4.50: 
            return "unsatisfactory"
        elif 4.50 <= mms: 
            return "unacceptable"
    if category==2: 
        if mms < 0.28: 
            return "still"
        elif 0.28<= mms < 1.12: 
            return "good"
        elif 1.12<= mms < 2.8: 
            return "satisfactory"
        elif 2.8 <= mms < 7.1: 
            return "unsatisfactory"
        elif 7.1 <= mms: 
            return "unacceptable"
    if category==3: 
        if mms < 0.28: 
            return "still"
        elif 0.28<= mms < 1.8: 
            return "good"
        elif 1.8<= mms < 4.5: 
            return "satisfactory"
        elif 4.5 <= mms < 11.2: 
            return "unsatisfactory"
        elif 11.2 <= mms: 
            return "unacceptable"
    if category==4: 
        if mms < 0.28: 
            return "still"
        elif 0.28<= mms < 2.8: 
            return "good"
        elif 2.8<= mms < 7.10: 
            return "satisfactory"
        elif 7.10 <= mms < 18.00: 
            return "unsatisfactory"
        elif 18.00 <= mms: 
            return "unacceptable"

    return "unknown"

pkt = json.loads(st)

pid = pkt['pid']
category = pkt['category']
mms = pkt['mms']

if pid == 5: 
    rslt = diagnosis(pid, category, mms)
    print(rslt)
