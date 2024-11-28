import math
import ISO


def forBearing(pkt, mms):
    machineType = pkt['machineType']
    Gear = pkt['Gear']
    Support = pkt['Support']
    Power = pkt['Power']
    Speed = pkt['Speed']
    Critical = pkt['Critical']

    if machineType == "Steam Turbine":
        if Power > 50000000:
            if 1400 < Speed <1600 or 1700 < Speed <1900:
                if mms < 0.28: 
                    return "still"
                elif 0.28<= mms < 2.8: 
                    return "good"
                elif 2.8<= mms < 5.3: 
                    return "satisfactory"
                elif 5.3 <= mms < 6.6: 
                    return "unsatisfactory"
                elif 6.6 <= mms < 8.5: 
                    return "unsatisfactory - alarm"
                elif 8.5 <= mms < 10.6: 
                    return "unacceptable"
                elif 10.6 <= mms: 
                    return "unacceptable - trip"
                else: return "unknown"
            elif 2900 < Speed <3100 or 3500 < Speed <3700:
                if mms < 0.28: 
                    return "still"
                elif 0.28<= mms < 3.8: 
                    return "good"
                elif 3.8<= mms < 7.5: 
                    return "satisfactory"
                elif 7.5 <= mms < 9.3: 
                    return "unsatisfactory"
                elif  9.3 <= mms < 11.8: 
                    return "unsatisfactory - alarm"
                elif 11.8 <= mms < 14.8: 
                    return "unacceptable"
                elif 14.8 <= mms: 
                    return "unacceptable - trip"
                else: return "unknown"
            else: return "unknown"
        elif 300000<Power <50000000: return ISO.ISO10816_3(1, mms)
        else: return ISO.ISO10816_3(2, mms)

    elif machineType == "Gas Turbine":
        if Power > 3000000:
            if 120 < Speed <15000:
                if mms < 0.28: 
                    return "still"
                elif 0.28<= mms < 4.5: 
                    return "good"
                elif 4.5<= mms < 9.3: 
                    return "satisfactory"
                elif 9.3 <= mms < 11.625: 
                    return "unsatisfactory"
                elif  11.625 <= mms < 14.7: 
                    return "unsatisfactory - alarm"
                elif 14.7 <= mms < 18.375: 
                    return "unacceptable"
                elif 18.375 <= mms: 
                    return "unacceptable - trip"
                else: return "unknown"
            else: return "unknown"
        else: return ISO.ISO10816_3(2, mms)
  
    elif machineType == "Pump" or machineType == "Fan" or machineType == "Generator" or machineType == "Compressor" or machineType == "Motor" or machineType == "Blower":
        if 120 < Speed <15000:
            if Support == "Rigid": 
                if 300000<Power < 50000000:
                    if mms < 0.28: 
                        return "still"
                    elif 0.28<= mms < 2.3: 
                        return "good"
                    elif 2.3<= mms < 4.5: 
                        return "satisfactory"
                    elif 4.5 <= mms < 5.625: 
                        return "unsatisfactory"
                    elif 5.625 <= mms < 7.1: 
                        return "unsatisfactory - alarm"
                    elif 7.1 <= mms < 8.875: 
                        return "unacceptable"
                    elif 8.875 <= mms: 
                        return "unacceptable - trip"
                    else: return "unknown"
                elif 15000<Power < 300000:
                    if mms < 0.28: 
                        return "still"
                    elif 0.28<= mms < 1.4: 
                        return "good"
                    elif 1.4<= mms < 2.8: 
                        return "satisfactory"
                    elif 2.8 <= mms < 3.5: 
                        return "unsatisfactory"
                    elif 3.5 <= mms < 4.5: 
                        return "unsatisfactory - alarm"
                    elif 4.5 <= mms < 5.625: 
                        return "unacceptable"
                    elif 5.625 <= mms: 
                        return "unacceptable - trip"
                    else: return "unknown"
            elif Support == "flexible": 
                if 300000<Power < 50000000:
                    if mms < 0.28: 
                        return "still"
                    elif 0.28<= mms < 3.5: 
                        return "good"
                    elif 3.5<= mms < 7.1: 
                        return "satisfactory"
                    elif 7.1 <= mms < 8.875: 
                        return "unsatisfactory"
                    elif 8.875 <= mms < 11.0: 
                        return "unsatisfactory - alarm"
                    elif 11.0 <= mms < 13.75: 
                        return "unacceptable"
                    elif 13.75 <= mms: 
                        return "unacceptable - trip"
                    else: return "unknown"
                elif 15000<Power < 300000:
                    if mms < 0.28: 
                        return "still"
                    elif 0.28<= mms < 2.3: 
                        return "good"
                    elif 2.3<= mms < 4.5: 
                        return "satisfactory"
                    elif 4.5 <= mms < 5.625: 
                        return "unsatisfactory"
                    elif 5.625 <= mms < 7.1: 
                        return "unsatisfactory - alarm"
                    elif 7.1 <= mms < 8.875: 
                        return "unacceptable"
                    elif 8.875 <= mms: 
                        return "unacceptable - trip"
                    else: return "unknown"
                else: return "unknown"
            else: return "unknown"
        else: return "unknown"
    else: return "unknown"


def forAxis(pkt, microS):
    machineType = pkt['machineType']
    Gear = pkt['Gear']
    Support = pkt['Support']
    Power = pkt['Power']
    Speed = pkt['Speed']
    Critical = pkt['Critical']

    if machineType == "Steam Turbine":
        if Power > 50000000:
            if 1400 < Speed <1600:
                if microS < 10: 
                    return "still"
                elif 10<= microS < 100: 
                    return "good"
                elif 100<= microS < 200: 
                    return "satisfactory"
                elif 200 <= microS < 250: 
                    return "unsatisfactory"
                elif 250 <= microS < 320: 
                    return "unsatisfactory - alarm"
                elif 320 <= microS < 400: 
                    return "unacceptable"
                elif 400 <= microS: 
                    return "unacceptable - trip"
                else: return "unknown"
            if 1700 < Speed <1900:
                if microS < 9: 
                    return "still"
                elif 9<= microS < 90: 
                    return "good"
                elif 90<= microS < 220: 
                    return "satisfactory"
                elif 220 <= microS < 275: 
                    return "unsatisfactory"
                elif 275 <= microS < 290: 
                    return "unsatisfactory - alarm"
                elif 290 <= microS < 325: 
                    return "unacceptable"
                elif 325 <= microS: 
                    return "unacceptable - trip"
                else: return "unknown"
            elif 2900 < Speed <3100:
                if microS < 8: 
                    return "still"
                elif 8<= microS < 80: 
                    return "good"
                elif 80<= microS < 165: 
                    return "satisfactory"
                elif 165 <= microS < 206.25: 
                    return "unsatisfactory"
                elif  206.25 <= microS < 260: 
                    return "unsatisfactory - alarm"
                elif 260 <= microS < 325: 
                    return "unacceptable"
                elif 325 <= microS: 
                    return "unacceptable - trip"
                else: return "unknown"
            elif 3500 < Speed <3700:
                if microS < 7.5: 
                    return "still"
                elif 7.5<= microS < 75: 
                    return "good"
                elif 75<= microS < 150: 
                    return "satisfactory"
                elif 150 <= microS < 187.5: 
                    return "unsatisfactory"
                elif  187.5 <= microS < 240: 
                    return "unsatisfactory - alarm"
                elif 240 <= microS < 300: 
                    return "unacceptable"
                elif 300 <= microS: 
                    return "unacceptable - trip"
                else: return "unknown"
            else: return "unknown"
        else: return ISO.ISO7919_3(Speed, microS)

    elif machineType == "Gas Turbine":
        if 3000 < Speed <30000:
            return ISO.ISO7919_3(Speed, microS)
        else: return "unknown"

    elif machineType == "Pump" or machineType == "Fan" or machineType == "Generator" or machineType == "Compressor" or machineType == "Motor" or machineType == "Blower":
        if 120 < Speed <15000:
            if microS < 4800/math.sqrt(Speed): 
                return "still"
            elif 4800/math.sqrt(Speed) <= microS < 4800/math.sqrt(Speed): 
                return "good"
            elif 4800/math.sqrt(Speed) <= microS < 9000/math.sqrt(Speed): 
                return "satisfactory"
            elif 9000/math.sqrt(Speed) <= microS < 11250/math.sqrt(Speed): 
                return "unsatisfactory"
            elif 11250/math.sqrt(Speed) <= microS < 16500/math.sqrt(Speed): 
                return "unsatisfactory - alarm"
            elif 16500/math.sqrt(Speed) <= microS: 
                return "unacceptable"
        else: return ISO.ISO7919_3(Speed, microS)
    else: return "unknown"

def getAlarm(pkt):
    machineType = pkt['machineType']
    Gear = pkt['Gear']
    Support = pkt['Support']
    Power = pkt['Power']
    Speed = pkt['Speed']
    Critical = pkt['Critical']
    if machineType == "Steam Turbine":
        if Power > 50000000:
            if 1400 < Speed <1600 or 1700 < Speed <1900:
                return 6.6
            elif 2900 < Speed <3100 or 3500 < Speed <3700:
                return 9.3
        elif 300000<Power <50000000: return 2.25
        else: return 3.5

    elif machineType == "Gas Turbine":
        if Power > 3000000:
            if 120 < Speed <15000:
                    return  11.625
        else: return 3.5
  
    elif machineType == "Pump" or machineType == "Fan" or machineType == "Generator" or machineType == "Compressor" or machineType == "Motor" or machineType == "Blower":
        if 120 < Speed <15000:
            if Support == "Rigid": 
                if 300000<Power < 50000000:
                    return 5.625
                elif 15000<Power < 300000:
                    return 3.5
            elif Support == "flexible": 
                if 300000<Power < 50000000:
                    return 8.875
                elif 15000<Power < 300000:
                    return 5.625
                else: return "unknown"
            else: return "unknown"
        else: return "unknown"
    else: return "unknown"

