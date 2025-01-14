from models.landing import Dashboard
from tests.test_01_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as login
from models.pms import IndividualPMS
import time

def test_employeeLogin(page):
    navigate(page)
    login(page)

def test_navigateToPMS(page):
    pms = IndividualPMS(page)
    # page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseYear()

def test_createKPI(page, readNewKpiNameJson, slots, count):
    pms = IndividualPMS(page)
    pms.configureCoreKPI(readNewKpiNameJson)
    time.sleep(1) #to let new kpi profile load
    pms.configureSubKPI(slots)
    pms.createKPI(readNewKpiNameJson, slots, count)
    #pms.submitKPI()
