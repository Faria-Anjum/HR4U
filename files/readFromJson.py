import json

# login

def employeeLogin():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['employee_email'], json_data['login']['pass'], json_data['login']['employee_name']

def readEmployeeName():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['employee_name']

def firstLMLogin():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['first_lm_email'], json_data['login']['pass'], json_data['login']['first_lm_name']

def secondLMLogin():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['second_lm_email'], json_data['login']['pass']

def adminLogin():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['admin_email'], json_data['login']['admin_pass']

#profile

def readCertificateInfo(effectiveDate, expDate):
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    name = json_data['profile']['training_name'] + str(json_data['profile']['test_count_profile'])
    expDay, expMonth, expYear = expDate
    return name, json_data['profile']['training_institution'], effectiveDate, expDay, expMonth, expYear, json_data['profile']['training_skills']

def readTrainingUrl():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['profile']['training_url']

#leave

def readRemainingLeave():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['leave']['remaining_leave']

def readUpdatedLeave():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['leave']['updated_leave']

#pms

# KPI already there in profile - Individual KPI by default
def readCurrentKpiName():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['pms']['current_kpi_profile']

def readKpiYear():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['pms']['current_kpi_year']

# Counter for how many times Sub KPIs have been created
def readKpiCount():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['pms']['test_count_pms']

# def readSlotCount():
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#     return json_data['pms']['totalSlots']

# def readAddSlots():
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#     return json_data['pms']['add_slots']

# def readDeleteSlots():
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#     return json_data['pms']['delete_slots']