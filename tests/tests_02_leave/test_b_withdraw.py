from tests.tests_01_landing.test_b_handset_claim import test_loginAsEmployee as loginemployee
from tests.tests_02_leave.test_a_leave import test_loginAsManager as manager, test_acceptRequest as acceptRequest, test_logout as logout
from models.leave import Withdraw

def test_withdrawLeaveRequest(page, employeeLogin, managerLogin):
    loginemployee(page, employeeLogin)

    withdraw = Withdraw(page)
    withdraw.navigateToLeaveRequest()
    withdraw.withdrawRequest()

    logout(page, employeeLogin)
    manager(page, managerLogin)
    acceptRequest(page, managerLogin)
    # logout(page, managerLogin)