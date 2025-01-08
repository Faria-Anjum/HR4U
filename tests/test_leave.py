from models.landing import Dashboard
from models.leave import LeaveRequest, AcceptRequest

def test_navigateToLogin(page):
    #page.pause()
    '''User can navigate to login'''
    dash = Dashboard(page)
    dash.navigate()
    
def test_enterCredentials(page):
    '''User can login'''
    dash = Dashboard(page)
    dash.loginUser()
    dash.loginPass()
    dash.clickLogIn()
    #dash.checkLoggedIn()

def test_requestLeave(page, today, three):
    leave = LeaveRequest(page)
    leave.navigateToLeaveRequest()
    leave.requestNewLeave()
    leave.selectAnnualLeave()
    leave.selectDate(today, three)
    leave.confirmLeaveRequest()

def test_logout(page):
    dash = Dashboard(page)
    dash.logout()
    dash.loginShortcut()

def test_loginAsManager(page):
    response = AcceptRequest(page)
    response.loginUser()
    response.loginPass()
    response.clickLogIn()

def test_acceptRequest(page):
    response = AcceptRequest(page)
    response.navigateToAllPendingRequests()