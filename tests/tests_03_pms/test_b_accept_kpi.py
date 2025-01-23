from tests.tests_01_landing.test_a_profile import test_navigateToLogin as navigate
from tests.tests_02_leave.test_a_leave import test_loginAsManager as loginmanager
# from models.writeToJson import readAddSlots, readSlotCount
from models.pms import PMSApproval

def test_acceptKPI(page, managerLogin, readEmployeeName, readCurrentKpiNameJson, kpiYear):
    navigate(page)
    loginmanager(page, managerLogin)
    pms = PMSApproval(page, readCurrentKpiNameJson, kpiYear)
    pms.navigateToManagerDashboard()
    pms.navigateToPmsApproval(readEmployeeName)
    pms.acceptKpi()