from models.landing import Dashboard
from files.readFromJson import employeeLogin, readCertificateInfo, readTrainingUrl
from files.writeToJson import writeTrainingTestCount
from playwright.sync_api import expect
import re, time

class ProfilePage(Dashboard):
    def __init__(self, page):
        self.page = page
        self.email, self.password, self.name = employeeLogin()

    def navigateToProfilePage(self):
        expect(self.page.locator("user div").first).to_be_visible()
        self.page.locator("user div").first.click()
        expect(self.page.get_by_role("button", name="Profile")).to_be_visible()
        self.page.get_by_role("button", name="Profile").click()

    def verifyProfilePage(self):
        expect(self.page.get_by_role("link", name="Basic Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Employee Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Contact Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Family Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Education Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Career Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Training Info")).to_be_visible()
        expect(self.page.get_by_role("link", name="Talent Info")).to_be_visible()

    def editProfile(self):
        expect(self.page.get_by_role("button", name="Edit Profile")).to_be_visible()
        self.page.get_by_role("button", name="Edit Profile").click()


class TrainingPage(Dashboard):
    def __init__(self, page, effectiveDate, expDate):
        self.page = page
        self.certificate, self.institution, self.effective, self.expDay, self.expMonth, self.expYear, self.skill = readCertificateInfo(effectiveDate, expDate)

    def addTraining(self):
        self.page.get_by_role("link", name="Training Info").click()
        expect(self.page.get_by_role("button", name="Add Trainings")).to_be_visible()
        self.page.get_by_role("button", name="Add Trainings").click()

        self.page.get_by_label("Certification Name *").click()
        self.page.get_by_label("Certification Name *").fill(self.certificate)

        self.page.get_by_label("Institution Name *").click()
        self.page.get_by_label("Institution Name *").fill(self.institution)

        expect(self.page.get_by_label("Effective Date *")).to_be_visible()
        self.page.locator("mat-form-field").filter(has_text="Effective Date *").get_by_label("Open calendar").click()
        self.page.get_by_label(self.effective).click()

        expect(self.page.get_by_label("Expiration Date *")).to_be_visible()
        self.page.locator("mat-form-field").filter(has_text="Expiration Date *").get_by_label("Open calendar").click()
        self.page.get_by_label("Choose month and year").click()
        self.page.get_by_label(self.expYear).click()
        self.page.get_by_label(self.expMonth).click()
        self.page.get_by_label(f'{self.expDay} {self.expMonth} {self.expYear}', exact=True).click()

        self.page.get_by_label("Skill Acquired *").click()
        self.page.get_by_label("Skill Acquired *").fill(self.skill)

        # expect(self.page.get_by_role("button", name="Add Trainings")).not_to_be_disabled()
        # self.page.get_by_role("button", name="Add Trainings").click()

        self.page.get_by_role("button", name="Save & Next").click()
        writeTrainingTestCount(1)
        
    def confirmTrainingAdd(self):
        self.page.goto(readTrainingUrl())
        # expect(self.page.get_by_role("button", name="View Profile")).to_be_visible()
        # self.page.get_by_role("button", name="View Profile").click()
        # global trainingDiv
        # trainingDiv = self.page.locator("div").filter(has_text=re.compile(r"^closeCertificate - 1$")).locator("div")
        # expect(trainingDiv).to_be_visible()
        # expect(self.certificate).to_be_visible()

    def deleteTraining(self):
        trainingDiv = self.page.locator("div").filter(has_text=re.compile(r"^closeCertificate - 1$")).locator("div")
        expect(trainingDiv.get_by_role("button").filter(has_text="close")).to_be_visible()
        trainingDiv.get_by_role("button").filter(has_text="close").click()
        self.page.get_by_role("button", name="Save & Next").click()
        self.confirmSuccessPopup()




    # self.page.get_by_role("button", name="Save & Next").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_role("link", name="Training Info").click()
    # self.page.get_by_role("button", name="View Profile").click()
    # self.page.get_by_role("button", name="Edit Profile").click()
    # self.page.locator("div").filter(has_text=re.compile(r"^closeCertificate - 1$")).locator("div").click()
    # self.page.locator("div").filter(has_text=re.compile(r"^closeCertificate - 2$")).get_by_role("button").click()
    # self.page.locator("button").filter(has_text="close").click()
    # self.page.get_by_role("button", name="Save & Next").click()
    # self.page.get_by_role("button", name="Ok").click()

