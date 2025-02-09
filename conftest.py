import pytest, math, calendar, json, datetime

#all test functions in a test file run on the same browser context
@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

#setting certificate effective date
@pytest.fixture
def effectiveDate():
    today = datetime.date.today()

    month = calendar.month_name[today.month]
    day = today.day

    day = f'{day} {month}'
    return day

@pytest.fixture
def expDate():
    today = datetime.date.today()

    month = (today.month + 3)%12
    month, year = monthlogic(today, month)

    if today.day in [28,29,30,31]:
        day = 1
        month = (month + 1)%12
        monthlogic(month, year)
    else:
        day = today.day

    month = calendar.month_name[month]
    # day = f'{day} {month} {year}'
    return str(day), str(month), str(year)

def monthlogic(today, month):
    if month == 0:
        month = 12
    if month < today.month:
        year = today.year + 1
    else:
        year = today.year

    return month, year

#for calculating slot percentage
# @pytest.fixture
# def calculatePercentage():
#     with open(r"files\data.json",'r') as f:
#         json_data = json.load(f)
#         total = json_data['pms']['total_slots']
#         eachslot = 100/total
#         percentage1 = math.floor(eachslot)
#         extra = int(100 - (percentage1*total))
#         return percentage1, extra

#getting current year
@pytest.fixture(scope="session")
def currentYear():
    today = datetime.date.today()
    year = today.year
    return year

#setting date
@pytest.fixture(scope="session")
def today():
    result = datetime.date.today() + datetime.timedelta(days=0)

    year = result.year
    month = calendar.month_name[result.month]
    day = result.day

    date = f'{day} {month} {year}'
    return date

@pytest.fixture(scope="session")
def tomorrow():
    result = datetime.date.today() + datetime.timedelta(days=1)

    year = result.year
    month = calendar.month_name[result.month]
    day = result.day

    date = f'{day} {month} {year}'
    return date

@pytest.fixture(scope="session")
def threeDays():
    result = datetime.date.today() + datetime.timedelta(days=3)

    year = result.year
    month = calendar.month_name[result.month]
    day = result.day

    date = f'{day} {month} {year}'
    return date
    
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