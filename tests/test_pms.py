from models.landing import Dashboard
from models.pms import IndividualPMS

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

def test_navigateToPMS(page):
    pms = IndividualPMS(page)
    page.pause()
    pms.navigateToPmsPlanning()
    pms.chooseIndividualKpi()
    pms.createKPI()
