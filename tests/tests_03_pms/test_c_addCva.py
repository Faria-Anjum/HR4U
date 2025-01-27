from models.backend import Admin

def test_navigate(page):
    admin = Admin(page)
    admin.navigate()
    admin.clickAccept()

def test_loginAsAdmin(page):
    backend = Admin(page)
    backend.adminUser()
    backend.adminPass()
    backend.clickLogIn()

def test_assignCVA(page):
    backend = Admin(page)
    backend.navigateToAssignProfile()
    # page.pause()
    backend.assignCvaToEmployee()
    backend.selectDates()
    backend.clickSaveButton()

