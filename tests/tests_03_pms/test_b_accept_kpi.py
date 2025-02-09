from tests.tests_01_landing.test_a_profile import test_navigateToLogin as navigate
from tests.tests_02_leave.test_a_leave import test_loginAsManager as managerlogin
from models.pms import PMSApproval

def test_acceptKPI(page):
    navigate(page)
    managerlogin(page)
    pms = PMSApproval(page)
    pms.navigateToManagerDashboard()
    pms.navigateToPmsApproval()
    pms.acceptKpi()