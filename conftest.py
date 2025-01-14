import pytest
from datetime import datetime, date
import calendar, json

#all test functions in a test file run on the same browser context
@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

@pytest.fixture
def employeeLogin():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['employeeEmail'], json_data['login']['employeePass'], json_data['login']['employeeName']

@pytest.fixture
def managerLogin():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['login']['managerEmail'], json_data['login']['managerPass'], json_data['login']['managerName']

# KPI already there in profile - Individual KPI by default
@pytest.fixture
def readCurrentKpiNameJson():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['kpi']['current_profile']

# New created KPI
@pytest.fixture
def readNewKpiNameJson():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['kpi']['new_profile']

# slots for new KPI
@pytest.fixture
def slots():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['kpi']['slotcount']

# Counter for how many times Sub KPIs have been created
@pytest.fixture
def count():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['kpi']['testcounter']

# @pytest.fixture
# def increaseTestCounter():
#     with open(r"files\data.json", 'r') as f:
#         json_data = json.load(f)
#         json_data['testcounter'] += 1

#     with open(r"files\data.json", 'w') as f:
#         f.write(json.dumps(json_data))

@pytest.fixture
def readRemainingLeave():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['leave']['remainingLeave']

@pytest.fixture
def readUpdatedLeave():
    with open(r"files\data.json",'r') as f:
        json_data = json.load(f)
    return json_data['leave']['updatedLeave']

#setting today's date
@pytest.fixture(scope="session")
def today():
    today = datetime.now()

    year = today.year
    month = calendar.month_name[today.month]
    day = today.day + 1

    day = f'{day} {month} {year}'
    return day

#three day date
@pytest.fixture(scope="session")
def three():
    today = datetime.now()

    year = today.year
    month = calendar.month_name[today.month]
    day = today.day + 2

    day = f'{day} {month} {year}'
    return day


#setting tomorrow's date
@pytest.fixture(scope="session")
def tomorrow():
    today = datetime.now()

    if today.day in [28,29,30,31]:
        if today.month == 12:
            month = 1
            year = today.year + 1
        else:
            month = today.month + 1
            year = today.year
        day = 1
    else:
        year = today.year
        month = today.month
        day = today.day + 1

    if len(str(today.day))==1:
        day = "0"+str(day)
    if len(str(today.month))==1:
        month = "0"+str(month)

    day = f'{year}-{month}-{day}'
    return day
    
#customizing html report
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    #cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    #cells.insert(1, f'<td class="col-time">{datetime.now()}</td>')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)