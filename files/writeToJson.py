import json, math

#profile

def writeTrainingTestCount(val):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        json_data['profile']['test_count_profile'] == val

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))
        
#leave

def writeRemainingLeave(rem):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
        json_data['leave']['remaining_leave'] = rem

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
        curr = json_data['leave']['remaining_leave']
        duration = json_data['leave']['duration']

        newrem = curr - float(duration)
        if str(newrem)[-1] == '0':
            newrem = int(newrem)
        json_data['leave']['updated_leave'] = newrem

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

#pms

# for conftest.py
# def calculatePercentage():
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#         total = json_data['pms']['totalSlots']
#         eachslot = 100/total
#         percentage1 = math.floor(eachslot)
#         extra = int(100 - (percentage1*total))
#         return percentage1, extra

def increaseTestCounter():
    with open(r"files\data.json", 'r') as f:
        json_data = json.load(f)
        json_data['pms']['test_count_pms'] += 1

    with open(r"files\data.json", 'w') as f:
        f.write(json.dumps(json_data))

# def writeTotalSlots(total):
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#         json_data['pms']['totalSlots'] = total

#     with open(r"files\data.json", 'w') as f:
#         f.write(json.dumps(json_data))

# def writeAddSlots(num):
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#         json_data['pms']['add_slots']+=num

#     with open(r"files\data.json", 'w') as f:
#         f.write(json.dumps(json_data))

# def writeDeleteSlots(num):
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#         json_data['pms']['delete_slots']+=num

#     with open(r"files\data.json", 'w') as f:
#         f.write(json.dumps(json_data))