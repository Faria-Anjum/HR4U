from models.landing import Dashboard
from models.profile import ProfilePage, TrainingPage

def test_navigateToLogin(page):
    # page.pause()
    '''User can navigate to login'''
    dash = Dashboard(page)
    dash.navigate()
    
def test_enterEmployeeCredentials(page):
    '''User can login'''
    login = ProfilePage(page)
    login.loginUser()
    login.loginPass()
    login.clickLogIn()

def test_navigateToProfile(page):
    profile = ProfilePage(page)
    profile.navigateToProfilePage()
    profile.verifyProfilePage()

def test_addTraining(page, effectiveDate, expDate):
    profile = ProfilePage(page)
    profile.editProfile()
    training = TrainingPage(page, effectiveDate, expDate)
    training.addTraining()
    training.confirmSuccessPopup()

def test_confirmEditedTraining(page, effectiveDate, expDate):
    training = TrainingPage(page, effectiveDate, expDate)
    training.confirmTrainingAdd()

def test_deleteTraining(page, effectiveDate, expDate):
    training = TrainingPage(page, effectiveDate, expDate)
    profile = ProfilePage(page)
    profile.editProfile()
    training.deleteTraining()

def test_closeBrowser(page):
    page.close()