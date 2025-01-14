from playwright.sync_api import expect
import time

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        expect(self.page.get_by_text("One app for Human Resources")).to_be_visible()
    
    def loginUser(self):
        #expect(self.page.get_by_role("text", name="Login to Your Account")).to_be_visible()

        expect(self.page.get_by_label("Email address *")).to_be_visible()
        self.page.get_by_label("Email address *").click()
        self.page.get_by_label("Email address *").fill(self.email)
        
    def loginPass(self):
        expect(self.page.get_by_label("Password *")).to_be_visible()
        self.page.get_by_label("Password *").click()
        self.page.get_by_label("Password *").fill(self.password)

    def clickLogIn(self):
        expect(self.page.get_by_role("button", name="Log In")).to_be_visible()
        self.page.get_by_role("button", name="Log In").click()

class Dashboard(LoginPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://test-pub-hris.robi.com.bd/"
    
    def checkLoggedIn(self):
        expect(self.page.locator("app-breadcrumb").get_by_text("Dashboard")).to_be_visible()
        expect(self.page.locator("user").get_by_text(self.name)).to_be_visible()
        

    def logout(self):
        # self.page.pause()
        self.page.locator("user").get_by_text(self.name).click()
        self.page.get_by_role("button", name="Log out").click()
        expect(self.page.get_by_text("You have signed out!")).to_be_visible()
        #time.sleep(2)

    def loginShortcut(self):
        self.page.get_by_role("link", name="sign in").click()

    def clickConfirm(self):
        expect(self.page.get_by_text("Confirm action")).to_be_visible()
        self.page.get_by_role("button", name="Confirm").click()

    def confirmSuccessPopup(self):
        expect(self.page.get_by_text("Success", exact = True)).to_be_visible()
        self.page.get_by_role("button", name="Ok").click()


#     page.locator("app-breadcrumb").get_by_text("Dashboard").click()
#     page.locator("user").get_by_text("Riyad Salehdin").click()
#     page.locator(".cdk-overlay-backdrop").click()
#     page.locator("user").get_by_text("Riyad Salehdin").click()
#     page.locator("#mat-dialog-1").click()
#     page.locator(".cdk-overlay-backdrop").click()
#     page.locator("fuse-fullscreen").get_by_role("button").click()
#     page.locator("fuse-fullscreen").get_by_role("button").click()
#     page.locator("fuse-fullscreen").get_by_role("button").click()
#     page.get_by_text("Tuesday, 7 January,").click()
#     expect(page.get_by_role("button", name="PMS Manual play")).to_be_visible()
#     page.locator("#automat_dashboard div").filter(has_text="0 Pending Leave").nth(3).click()
#     page.locator("#automat_dashboard div").filter(has_text="0 Pending Medical Claim").nth(3).click()
#     page.locator("#automat_dashboard div").filter(has_text="-- PMS Rating(2024)").nth(3).click()
#     page.locator("#automat_dashboard").get_by_text("Attendance").click()
#     page.locator("span").filter(has_text="Today").click()
#     page.get_by_text("Jan 7,").click()
#     page.get_by_text("In Time").click()
#     page.get_by_text("Out Time").click()
#     page.get_by_text("Today").first.click()
#     page.get_by_role("menuitem", name="Last 7 Days").click()
#     page.get_by_text("Last 7 Days").click()
#     page.get_by_role("menuitem", name="Today").click()
#     page.get_by_text("Today").first.click()
#     page.get_by_role("menuitem", name="Last 7 Days").click()
#     page.get_by_role("columnheader", name="Date").click()
#     page.get_by_role("columnheader", name="In Time").click()
#     page.get_by_role("columnheader", name="Out Time").click()
#     page.get_by_role("columnheader", name="Status").click()
#     page.get_by_text("All Benefits").click()
#     page.get_by_text("Benefit Title").click()
#     page.get_by_text("(Approved amount/Total limit)").click()
#     page.get_by_text("Useful Links").click()
#     expect(page.get_by_role("button", name="FSD")).to_be_visible()
#     with page.expect_popup() as page1_info:
#         page.get_by_role("button", name="Workflow").click()
#     page1 = page1_info.value
#     expect(page.get_by_role("button", name="Workflow")).to_be_visible()
#     expect(page.get_by_role("button", name="ServiceDesk Plus")).to_be_visible()
#     expect(page.get_by_role("button", name="Robi eApproval")).to_be_visible()
#     expect(page.get_by_role("button", name="Download iOS App")).to_be_visible()
#     expect(page.get_by_role("button", name="Download Android App")).to_be_visible()
#     expect(page.locator("#automat_dashboard").get_by_text("My Salary")).to_be_visible()
#     expect(page.get_by_text("My Salary 2025Select")).to_be_visible()
#     page.locator("span").filter(has_text="Select Year").click()
#     page.locator(".cdk-overlay-backdrop").click()
#     expect(page.locator("span").filter(has_text="Select Year")).to_be_visible()
#     expect(page.locator("span").filter(has_text="Select Month")).to_be_visible()
#     expect(page.get_by_text("Organogram")).to_be_visible()
#     expect(page.get_by_text("Announcements")).to_be_visible()
#     page.get_by_text("Today").click()
#     page.get_by_role("menuitem", name="Last 7 Days").click()
#     expect(page.get_by_text("last 7 Days", exact=True)).to_be_visible()
#     page.get_by_text("Announcements").click()
#     expect(page.get_by_text("Announcements last 7 Days")).to_be_visible()
#     expect(page.get_by_text("Organogram")).to_be_visible()

# <div class="flex flex-row sm:flex-col items-center sm:ml-4"><span class="text-md text-[#6c7177] font-semibold">Remaining</span><span class="text-xl ml-auto sm:ml-0 font-bold sm:mt-5"> 38.5 </span></div>
