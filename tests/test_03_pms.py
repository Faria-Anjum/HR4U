from tests.test_01_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as loginemployee, test_loginAsManager as loginmanager, test_logout as logout
# from models.writeToJson import readAddSlots, readSlotCount
from models.pms import IndividualPMS, PMSApproval
#import time

def test_employeeLogin(page, employeeLogin):
    navigate(page)
    loginemployee(page, employeeLogin)

def test_navigateToPMS(page, kpiYear, readCurrentKpiNameJson, currentYear):
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    #page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseYear(currentYear)

def test_fillupSlotsKPI(page, employeeLogin, readCurrentKpiNameJson, kpiYear, count):
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    pms.configureKPISlots()
    pms.navigateToKPI()
    pms.fillupSubKPIs(count, 1, 5)
    pms.submitKPI()
    logout(page, employeeLogin)

def test_revertKPI(page, managerLogin, readEmployeeName, readCurrentKpiNameJson, kpiYear):
    loginmanager(page, managerLogin)
    pms = PMSApproval(page, readCurrentKpiNameJson, kpiYear)
    pms.navigateToPmsApproval(readEmployeeName)
    pms.revertKPI()
    pms.enterRevertReason()

    logout(page, managerLogin)
    
def test_editRevertedKPI(page, employeeLogin, kpiYear, readCurrentKpiNameJson, count, currentYear):
    loginemployee(page, employeeLogin)
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    test_navigateToPMS(page, kpiYear, readCurrentKpiNameJson, currentYear)
    add = PMSApproval(page, readCurrentKpiNameJson, kpiYear)
    # add.addSlot(1)
    # page.pause()
    # pms.configureKPISlots()
    # pms.fillupSubKPIs(count, readSlotCount()+1, readSlotCount()+readAddSlots()+1)
    pms.navigateToKPI()
    add.editSlot()
    pms.submitKPI()
    logout(page, employeeLogin)

def test_acceptKPI(page, managerLogin, readEmployeeName, readCurrentKpiNameJson, kpiYear):
    loginmanager(page, managerLogin)
    pms = PMSApproval(page, readCurrentKpiNameJson, kpiYear)
    pms.navigateToPmsApproval(readEmployeeName)
    pms.acceptKpi()
    logout(page, managerLogin)