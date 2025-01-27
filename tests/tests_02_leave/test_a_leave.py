from tests.tests_01_landing.test_b_handset_claim import test_loginAsEmployee as employeelogin
from tests.tests_01_landing.test_a_profile import test_enterEmployeeCredentials as employeeCredentials
from models.profile import ProfilePage
from models.leave import LeaveRequest, AcceptRequest, VerifyAccepted

#add weekend valdation

def test_employeeLogin(page):
    employeelogin(page)

def test_requestLeave(page, tomorrow, threeDays):
    leave = LeaveRequest(page)
    leave.navigateToLeaveRequest()
    leave.requestNewLeave()
    leave.selectAnnualLeave()
    leave.checkRemaining()
    leave.selectDate(tomorrow, threeDays)
    leave.getDuration()
    leave.confirmLeaveRequest()

def test_logout(page):
    logout = ProfilePage(page)
    logout.logout()
    logout.loginShortcut()

def test_loginAsManager(page):
    response = AcceptRequest(page)
    response.loginUser()
    response.loginPass()
    response.clickLogIn()

def test_acceptRequest(page):
    response = AcceptRequest(page)
    response.navigateToAllPendingRequests()
    response.findRequest()
    response.acceptRequest()

def test_managerLogout(page):
    response = AcceptRequest(page)
    response.logout()
    response.loginShortcut()

def test_verifyRemaining(page):
    leave = VerifyAccepted(page)
    employeeCredentials(page)
    leave.navigateToLeaveRequest()
    leave.checkRemaining()

def test_closeBrowser(page):
    page.close()