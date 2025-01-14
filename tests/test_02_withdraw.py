from tests.test_01_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as employee, test_loginAsManager as manager, test_acceptRequest as acceptRequest, test_logout as logout
from models.leave import Withdraw

def test_withdrawLeaveRequest(page, employeeLogin, managerLogin):
    navigate(page)
    employee(page, employeeLogin)

    withdraw = Withdraw(page)
    withdraw.navigateToLeaveRequest()
    withdraw.withdrawRequest()

    logout(page, employeeLogin)
    manager(page, managerLogin)
    acceptRequest(page, managerLogin)