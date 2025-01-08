from models.landing import Dashboard
from playwright.sync_api import expect
import re

class LeaveRequest:
    def __init__(self, page):
        self.page = page

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

    def selectDate(self, today, three):
        self.page.get_by_label("Start Date *").click()
        self.page.locator("#automat_start_date").get_by_label("Open calendar").click()
        self.page.get_by_label(today, exact=True).click()
        self.page.locator("#automat_end_date").get_by_label("Open calendar").click()
        self.page.get_by_label(three, exact=True).click()

    def confirmLeaveRequest(self):
        self.page.get_by_label("Leave Reason *").click()
        self.page.get_by_placeholder("Reason (Max limit: 190").fill("Test Leave")

        self.page.get_by_role("button", name="Request Now").click()
        self.page.get_by_role("button", name="Ok").click()

class AcceptRequest(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://test-pub-hris.robi.com.bd/"
        self.email = "rafat.kamal@robi.com.bd"
        self.password = "Robi@12345$$"
        self.name = "Mohammad Rafat Kamal"

    def navigateToAllPendingRequests(self):
        # self.page.get_by_text("Manager", exact=True).click()
        # self.page.get_by_text("Manager Dashboard", exact=True).click()

        #expect(self.page.get_by_heading("Pending Leave History")).to_be_visible()
        self.page.get_by_text("View Details").click()

        expect(self.page.get_by_text("All Pending Requests")).to_be_visible()
        row = self.page.locator("tr:first-child")
        cell = row.locator("td:nth-child(10)")
        # expect(cell).to_contain_text("Accept")
        # expect(cell).to_contain_text("Reject")

        cell.get_by_role("button", name="Accept").click()
        expect(self.page.get_by_text("Confirm action")).to_be_visible()
        self.page.get_by_role("button", name="Confirm").click()
        expect(self.page.get_by_text("Success", exact = True)).to_be_visible()
        self.page.get_by_role("button", name="Ok").click()