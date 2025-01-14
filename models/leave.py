# add withdraw for leave
# add weekend check for automatic leave date selection

from models.landing import Dashboard
from models.writeToJson import writeRemainingLeave, writeLeaveDuration, updateRemainingLeave
from playwright.sync_api import expect
import re, time

class LeaveRequest(Dashboard):
    def __init__(self, page, employeeLogin):
        self.page = page
        self.email, self.password, self.name = employeeLogin

    def navigateToLeaveRequest(self):
        expect(self.page.get_by_role("link", name="Leave Request")).to_be_visible()
        self.page.get_by_role("link", name="Leave Request").click()
        expect(self.page.get_by_text("My Leave")).to_be_visible()

    def requestNewLeave(self):
        self.page.get_by_role("button", name="New Leave Request").click()
        expect(self.page.get_by_label("Leave Requestclose").get_by_text("Leave Request")).to_be_visible()

    def selectAnnualLeave(self):
        self.page.locator("div").filter(has_text=re.compile(r"^Leave Type \*$")).nth(3).click()
        self.page.get_by_role("option", name="Annual Leave").locator("span").click()

    def checkRemaining(self):

        def getRemaining(text):
            text = re.search('You have (.*?) days', text)
            rem = text.group(1)
            writeRemainingLeave(float(rem))

        rem = self.page.locator("#automat_leave_form div").get_by_text("You have").inner_text()
        getRemaining(rem)

    def selectDate(self, today, three):
        self.page.get_by_label("Start Date *").click()
        self.page.locator("#automat_start_date").get_by_label("Open calendar").click()
        self.page.get_by_label(today, exact=True).click()
        self.page.locator("#automat_end_date").get_by_label("Open calendar").click()
        self.page.get_by_label(three, exact=True).click()

    def getDuration(self):
        time.sleep(0.25)
        duration = self.page.eval_on_selector('#automat_duration_input', 'element => element.value')
        writeLeaveDuration(float(duration))
        updateRemainingLeave()

    def confirmLeaveRequest(self):
        self.page.get_by_label("Leave Reason *").click()
        self.page.get_by_placeholder("Reason (Max limit: 190").fill("Test Leave")

        self.page.get_by_role("button", name="Request Now").click()
        self.confirmSuccessPopup()


class AcceptRequest(Dashboard):
    def __init__(self, page, managerLogin):
        self.page = page
        self.url = "https://test-pub-hris.robi.com.bd/"
        self.email, self.password, self.name = managerLogin

    def navigateToAllPendingRequests(self):
        # uncomment if logging in to manager defaults to employee dashboard
        # self.page.get_by_text("Manager", exact=True).click()
        # self.page.get_by_text("Manager Dashboard", exact=True).click()
        # expect(self.page.get_by_text("Pending Leave History", exact=True)).to_be_visible()

        # open all requests
        self.page.get_by_text("View Details").click()
        expect(self.page.get_by_text("All Pending Requests")).to_be_visible()

    def findRequest(self):
        # finding accept and reject buttons for top request
        row = self.page.locator("tr:first-child")
        global cell
        cell = row.locator("td:nth-child(10)")

    def acceptRequest(self):
        # accepting request
        cell.get_by_role("button", name="Accept").click()
        self.clickConfirm()
        self.confirmSuccessPopup()

class VerifyAccepted(LeaveRequest):
    def __init__(self, page):
        self.page = page

    def checkRemaining(self, readUpdatedLeave):
        # ensure accepted leave has been deducted
        self.page.get_by_text("More").click()
        self.page.get_by_role("menuitem", name="Leave Balance").click()
        expect(self.page.locator("#automat_leave_table")).to_contain_text("Remaining " + str(readUpdatedLeave))
        self.page.get_by_role("button").click()

class Withdraw(LeaveRequest):
    def __init__(self, page):
        self.page = page

    def withdrawRequest(self):
        expect(self.page.get_by_role("button", name="Withdraw")).to_be_visible()
        self.page.get_by_role("button", name="Withdraw").click()
        self.clickConfirm()