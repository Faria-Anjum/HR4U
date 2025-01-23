from models.backend import Admin

def test_navigate(page, adminLogin):
    admin = Admin(page, adminLogin)
    admin.navigate()
    admin.clickAccept()

def test_loginAsAdmin(page, adminLogin):
    backend = Admin(page, adminLogin)
    backend.adminUser()
    backend.adminPass()
    backend.clickLogIn()

def test_assignCVA(page, adminLogin):
    backend = Admin(page, adminLogin)
    backend.navigateToAssignProfile()
    # page.pause()
    backend.assignCvaToEmployee()
    backend.selectDates()
    backend.clickSaveButton()

