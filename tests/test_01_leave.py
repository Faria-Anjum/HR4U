from models.landing import Dashboard
from models.leave import LeaveRequest, AcceptRequest, VerifyAccepted

#add weekend valdation

def test_navigateToLogin(page):
    #page.pause()
    '''User can navigate to login'''
    dash = Dashboard(page)
    dash.navigate()
    
def test_enterEmployeeCredentials(page, employeeLogin):
    '''User can login'''
    login = LeaveRequest(page, employeeLogin)
    login.loginUser()
    login.loginPass()
    login.clickLogIn()

def test_requestLeave(page, today, three, employeeLogin):
    leave = LeaveRequest(page, employeeLogin)
    leave.navigateToLeaveRequest()
    leave.requestNewLeave()
    leave.selectAnnualLeave()
    leave.checkRemaining()
    leave.selectDate(today, three)
    leave.getDuration()
    leave.confirmLeaveRequest()

def test_logout(page, employeeLogin):
    logout = LeaveRequest(page, employeeLogin)
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
    test_enterEmployeeCredentials(page, employeeLogin)
    leave.navigateToLeaveRequest()
    leave.checkRemaining(readUpdatedLeave)