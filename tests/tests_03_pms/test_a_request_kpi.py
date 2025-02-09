from tests.tests_01_landing.test_b_handset_claim import test_loginAsEmployee as employeelogin
from tests.tests_01_landing.test_a_profile import test_enterEmployeeCredentials as employeeCredentials
from tests.tests_02_leave.test_a_leave import test_loginAsManager as managerlogin, test_logout as logout, test_managerLogout as FLMlogout
from models.pms import IndividualPMS, PMSApproval
import time

def test_employeeLogin(page):
    employeelogin(page)

def test_navigateToPMS(page, currentYear):
    pms = IndividualPMS(page)
    # page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseYear(currentYear)

def test_fillupSlotsKPI(page):
    pms = IndividualPMS(page)
    pms.configureKPISlots()
    pms.navigateToKPI()
    pms.fillupSubKPIs(1, 5)
    pms.submitKPI()
    logout(page)

def test_revertKPI(page):
    managerlogin(page)
    pms = PMSApproval(page)
    # pms.navigateToManagerDashboard()
    pms.navigateToPmsApproval()
    pms.revertKPI()
    pms.enterRevertReason()
    FLMlogout(page)
    
def test_editRevertedKPI(page, currentYear):
    employeeCredentials(page)
    pms = IndividualPMS(page)
    test_navigateToPMS(page, currentYear)
    add = PMSApproval(page)
    pms.navigateToKPI()
    add.editSlot()
    pms.submitKPI()
    # logout(page, employeeLogin)

def test_closeBrowser(page):
    page.close()