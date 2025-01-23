from models.landing import Dashboard
from models.profile import ProfilePage, TrainingPage
import pytest

def test_navigateToLogin(page):
    #page.pause()
    '''User can navigate to login'''
    dash = Dashboard(page)
    dash.navigate()
    
def test_enterEmployeeCredentials(page, employeeLogin):
    '''User can login'''
    login = ProfilePage(page, employeeLogin)
    login.loginUser()
    login.loginPass()
    login.clickLogIn()

def test_navigateToProfile(page, employeeLogin):
    profile = ProfilePage(page, employeeLogin)
    profile.navigateToProfilePage()
    profile.verifyProfilePage()

def test_addTraining(page, readCertificateInfo, employeeLogin):
    profile = ProfilePage(page, employeeLogin)
    profile.editProfile()
    training = TrainingPage(page, readCertificateInfo)
    training.addTraining()
    training.confirmSuccessPopup()

def test_confirmEditedTraining(page, readCertificateInfo, readTrainingUrl):
    training = TrainingPage(page, readCertificateInfo)
    training.confirmTrainingAdd(readTrainingUrl)

def test_deleteTraining(page, readCertificateInfo, employeeLogin):
    training = TrainingPage(page, readCertificateInfo)
    profile = ProfilePage(page, employeeLogin)
    profile.editProfile()
    training.deleteTraining()