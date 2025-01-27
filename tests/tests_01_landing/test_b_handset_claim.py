from tests.tests_01_landing.test_a_profile import test_navigateToLogin as navigate, test_enterEmployeeCredentials as employeeLogin
from models.benefitsAndClaims import Benefits

def test_loginAsEmployee(page):
    navigate(page)
    employeeLogin(page)

def test_navigationToHandset(page):
    bnc = Benefits(page)
    # page.pause()
    bnc.navigateToHandsetClaim()
