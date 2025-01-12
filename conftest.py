import pytest
from datetime import datetime, date
import calendar

#all test functions in a test file run on the same browser context
@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

@pytest.fixture
def readUpdated():
    with open(r"files\remaining.txt",'r') as f:
        st = float(f.readlines()[1])
    return str(st)

@pytest.fixture
def readRemaining():
    with open(r"files\remaining.txt",'r') as f:
        st = float(f.readlines()[0])
    return str(st)

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