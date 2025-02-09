from tests.tests_01_landing.test_b_handset_claim import test_loginAsEmployee as employeelogin
from tests.tests_02_leave.test_a_leave import test_loginAsManager as managerlogin, test_acceptRequest as acceptRequest, test_logout as logout
from models.leave import Withdraw

def test_withdrawLeaveRequest(page):
    employeelogin(page)

    withdraw = Withdraw(page)
    withdraw.navigateToLeaveRequest()
    withdraw.withdrawRequest()

    logout(page)
    managerlogin(page)
    acceptRequest(page)
    # logout(page, managerLogin)