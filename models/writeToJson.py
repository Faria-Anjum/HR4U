import json, math

def writeRemainingLeave(rem):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        json_data['leave']['remainingLeave'] = rem

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

def writeLeaveDuration(duration):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        json_data['leave']['duration'] = duration

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

def updateRemainingLeave():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        curr = json_data['leave']['remainingLeave']
        duration = json_data['leave']['duration']

        newrem = curr - float(duration)
        if str(newrem)[-1] == '0':
            newrem = int(newrem)
        json_data['leave']['updatedLeave'] = newrem

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

def writeTotalSlots(total):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        json_data['pms']['totalSlots'] = total

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

def writeAddSlots(num):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        json_data['pms']['add_slots']+=num

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

def calculatePercentage():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        total = json_data['pms']['totalSlots']
        eachslot = 100/total
        percentage1 = math.floor(eachslot)
        extra = int(100 - (percentage1*total))
        return percentage1, extra

def increaseTestCounter():
    with open(r"files\data.json", 'r') as f:
        json_data = json.load(f)
        json_data['pms']['testcounter'] += 1

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))