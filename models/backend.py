from models.landing import Dashboard
from files.readFromJson import adminLogin, readEmployeeName
from playwright.sync_api import expect
import time

class Admin(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = 'https://test-hris.robi.com.bd'
        self.user, self.password = adminLogin()

    def clickAccept(self):
        self.page.get_by_role("button", name="Accept").click()

    def adminUser(self):
        expect(self.page.get_by_label("Email")).to_be_visible()
        self.page.get_by_label("Email").click()
        self.page.get_by_label("Email").fill(self.user)

    def adminPass(self):
        expect(self.page.get_by_label("Password")).to_be_visible()
        self.page.get_by_label("Password").click()
        self.page.get_by_label("Password").fill(self.password)

    def clickLogIn(self):
        self.page.get_by_label("LOG IN").click()

    def navigateToAssignProfile(self):
        self.page.get_by_text("PMSkeyboard_arrow_right", exact=True).hover()
        expect(self.page.get_by_role("link", name="Assign Profile (B-G)")).to_be_visible()
        self.page.get_by_role("link", name="Assign Profile (B-G)").click()

    def assignCvaToEmployee(self):
        self.page.get_by_role("button", name="Assign New PMS").click()
        self.page.get_by_label("Select To Assign").locator("span").click()
        self.page.get_by_role("option", name="Individual Employee").click()

        self.page.get_by_label("Year", exact=True).locator("span").click()
        self.page.get_by_role("option", name="2024").click()

        self.page.get_by_label("Select Employee").locator("span").click()
        self.page.get_by_placeholder("Search here").fill(readEmployeeName())
        self.page.get_by_role("option", name=readEmployeeName()).locator("span").click()
        self.page.get_by_role("heading", name="Assign New Profile").click(force=True)

        self.page.get_by_label("Select Group").locator("span").click()
        self.page.get_by_text("Individual KPI (weightage:").click()
        time.sleep(0.25)
        self.page.locator("mat-label").filter(has_text="Add Performance Profile Template").click(force=True)
        
        self.page.get_by_role("option", name="Core Value Assessment (").click()
        self.page.get_by_role("heading", name="Assign New Profile").click(force=True)

        
    def selectDates(self):
        self.page.locator("mat-form-field").filter(has_text="PMS Planning End date").get_by_label("Open calendar").click()
        self.page.get_by_label("Next month").click()
        self.page.get_by_text("28", exact=True).click()

        self.page.locator("mat-form-field").filter(has_text="Choose Start Date").get_by_label("Open calendar").click()
        self.page.get_by_label("Previous month").click()
        self.page.get_by_text("1", exact=True).click()

        self.page.locator("mat-form-field").filter(has_text="Choose End date").get_by_label("Open calendar").click()
        self.page.get_by_label("Previous month").click()
        self.page.get_by_text("28", exact=True).click()

    def clickSaveButton(self):
        self.page.get_by_role("button", name="Save").click()
        time.sleep(0.5)
        self.page.get_by_role("button", name="Close").click()



#     self.page.locator(".mat-form-field-infix").first.click()
#     self.page.get_by_placeholder("Search here").fill("Salman")
#     self.page.get_by_text("Salman Ahmed (10005947)").click()
#     self.page.get_by_label("Year Filter").locator("div").nth(1).click()
#     self.page.get_by_text("2024").click()
#     self.page.get_by_role("button", name="Assign New PMS").click()
#     self.page.get_by_label("Assign New Profile").locator("div").filter(has_text="Select To Assign").nth(4).click()
#     self.page.get_by_text("Individual Employee").click()
#     self.page.get_by_label("Select To Assign").locator("div").nth(1).click()
#     self.page.get_by_role("option", name="Individual Employee").click()
#     self.page.get_by_label("Year", exact=True).locator("span").click()
#     self.page.get_by_role("option", name="2024").click()
#     self.page.get_by_label("Select Employee").locator("span").click()
#     self.page.get_by_placeholder("Search here").fill("salman")
#     self.page.get_by_text("Salman Ahmed 10005947").click()
#     self.page.get_by_label("Clear").click()
#     self.page.get_by_placeholder("Search here").fill("salman")
#     self.page.get_by_role("option", name="Salman Ahmed").locator("span").click()
#     self.page.get_by_label("Select Group").locator("span").click()
#     self.page.get_by_text("Individual KPI (weightage:").click()
#     self.page.get_by_label("Assign New Profile").locator("div").filter(has_text="Add Performance Profile").nth(4).click()
#     self.page.get_by_role("option", name="Core Value Assessment   (").click()
#     self.page.locator(".cdk-overlay-container > div:nth-child(3)").click()
#     self.page.locator("mat-form-field").filter(has_text="PMS Planning End date").get_by_label("Open calendar").click()
#     self.page.get_by_label("Next month").click()
#     self.page.get_by_text("28", exact=True).click()
#     self.page.locator("mat-form-field").filter(has_text="Choose Start Date").get_by_label("Open calendar").click()
#     self.page.get_by_label("Previous month").click()
#     self.page.get_by_text("1", exact=True).click()
#     self.page.locator("mat-form-field").filter(has_text="Choose End date").get_by_label("Open calendar").click()
#     self.page.get_by_label("Next month").click()
#     self.page.get_by_label("Previous month").dblclick()
#     self.page.get_by_text("31", exact=True).click()
#     self.page.get_by_role("button", name="Save").click()
#     self.page.get_by_text("Your Assign Profile Create").click()
#     self.page.get_by_text("check_circle").click()
#     self.page.get_by_role("button", name="Close").click()
#     self.page.get_by_role("row", name="Salman Ahmed Back Office").get_by_role("button").nth(1).click()
#     self.page.get_by_role("button", name="Ok").click()
#     self.page.get_by_role("button", name="Close").click()

