from tests.test_03_pms import test_employeeLogin as loginAsEmployee
from models.benefitsAndClaims import Benefits

def test_loginAsEmployee(page, employeeLogin):
    loginAsEmployee(page, employeeLogin)

def testNavigationToHandset(page):
    bnc = Benefits(page)
    page.pause()
    bnc.navigateToHandsetClaim()
