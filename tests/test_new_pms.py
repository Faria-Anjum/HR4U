from models.landing import Dashboard
from tests.test_01_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as login
from models.pms import NewPMS
import time

def test_employeeLogin(page, employeeLogin):
    navigate(page)
    login(page, employeeLogin)

def test_navigateToPMS(page):
    pms = NewPMS(page)
    # page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseYear()

def test_createKPI(page, readNewKpiNameJson, slots, count):
    pms = NewPMS(page)
    pms.configureCoreKPI(readNewKpiNameJson)
    time.sleep(1) #to let new kpi profile load
    pms.configureSubKPI(slots)
    pms.createNewSubKPI(readNewKpiNameJson, slots, count)
    pms.submitKPI()
    page.pause()
