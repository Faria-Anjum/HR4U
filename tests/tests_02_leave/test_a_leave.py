from tests.tests_01_landing.test_a_profile import test_navigateToLogin as navigate, test_enterEmployeeCredentials as loginemployee
from models.leave import LeaveRequest, AcceptRequest, VerifyAccepted
from models.profile import ProfilePage

#add weekend valdation

def test_employeeLogin(page, employeeLogin):
    navigate(page)
    loginemployee(page, employeeLogin)

def test_requestLeave(page, today, threedays):
    leave = LeaveRequest(page)
    leave.navigateToLeaveRequest()
    leave.requestNewLeave()
    leave.selectAnnualLeave()
    leave.checkRemaining()
    leave.selectDate(today, threedays)
    leave.getDuration()
    leave.confirmLeaveRequest()

def test_logout(page, employeeLogin):
    logout = ProfilePage(page, employeeLogin)
    logout.logout()
    logout.loginShortcut()

def test_loginAsManager(page, managerLogin):
    response = AcceptRequest(page, managerLogin)
    response.loginUser()
    response.loginPass()
    response.clickLogIn()

def test_acceptRequest(page, managerLogin):
    response = AcceptRequest(page, managerLogin)
    response.navigateToAllPendingRequests()
    response.findRequest()
    response.acceptRequest()
    response.logout()
    response.loginShortcut()

def test_verifyRemaining(page, readUpdatedLeave, employeeLogin):
    leave = VerifyAccepted(page)
    loginemployee(page, employeeLogin)
    leave.navigateToLeaveRequest()
    leave.checkRemaining(readUpdatedLeave)