from tests.test_01_leave import test_navigateToLogin as navigate, test_enterEmployeeCredentials as loginemployee, test_loginAsManager as loginmanager, test_logout as logout
from models.profile import ProfilePage, TrainingPage
import pytest

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

def test_employeeLogin(page, employeeLogin):
    navigate(page)
    loginemployee(page, employeeLogin)

def test_navigateToProfile(page):
    profile = ProfilePage(page)
    profile.navigateToProfilePage()
    profile.verifyProfilePage()

def test_addTraining(page, readCertificateInfo):
    profile = ProfilePage(page)
    profile.editProfile()
    training = TrainingPage(page, readCertificateInfo)
    training.addTraining()
    training.confirmSuccessPopup()

def test_confirmEditedTraining(page, readCertificateInfo, readTrainingUrl):
    training = TrainingPage(page, readCertificateInfo)
    training.confirmTrainingAdd(readTrainingUrl)

def test_deleteTraining(page,readCertificateInfo):
    training = TrainingPage(page, readCertificateInfo)
    profile = ProfilePage(page)
    profile.editProfile()
    training.deleteTraining()





