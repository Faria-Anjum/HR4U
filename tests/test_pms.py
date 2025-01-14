from models.landing import Dashboard
from tests.test_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as login
from models.pms import IndividualPMS
import time

def test_employeeLogin(page):
    navigate(page)
    login(page)

def test_navigateToPMS(page, readNewKpiNameJson, slots, count, increaseTestCounter):
    pms = IndividualPMS(page)
    # page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseIndividualKpi()
    pms.configureCoreKPI(readNewKpiNameJson)
    time.sleep(1)
    pms.configureSubKPI(slots)
    pms.createKPI(readNewKpiNameJson, slots, count, increaseTestCounter)
    #pms.submitKPI()
