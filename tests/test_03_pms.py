from models.landing import Dashboard
from tests.test_01_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as loginemployee, test_loginAsManager as loginmanager, test_logout as logout
from models.pms import IndividualPMS, PMSApproval
import time

def test_employeeLogin(page, employeeLogin):
    navigate(page)
    loginemployee(page, employeeLogin)

def test_navigateToPMS(page, kpiYear, readCurrentKpiNameJson):
    pms = IndividualPMS(page, readCurrentKpiNameJson)
    #page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseYear(kpiYear)

def test_fillupSlotsKPI(page, readCurrentKpiNameJson, kpiYear, readAddSlots, readDeleteSlots, readSlotCount, count):
    pms = IndividualPMS(page, readCurrentKpiNameJson)
    pms.configureKPISlots(kpiYear, readAddSlots, readDeleteSlots)
    pms.fillupSubKPIs(count, readSlotCount, kpiYear)
    pms.submitKPI()

def test_revertKPI(page, employeeLogin, managerLogin, readEmployeeName):
    logout(page, employeeLogin)
    loginmanager(page, managerLogin)
    pms = PMSApproval(page)
    pms.navigateToPmsApproval(readEmployeeName)
    pms.revertKPI()
    logout(page, managerLogin)
    
# def test_editRevertedKPI(page, employeeLogin, kpiYear, readCurrentKpiNameJson):
#     loginemployee(page, employeeLogin)
#     pms = IndividualPMS(page, readCurrentKpiNameJson)
#     test_navigateToPMS(page, kpiYear, readCurrentKpiNameJson)
