# add withdraw for leave
# add weekend check for automatic leave date selection

from models.landing import Dashboard
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

            def writeRemaining(rem):
                with open(r"files\remaining.txt",'w') as f:
                    f.write(rem)
            writeRemaining(rem)

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

        def writeRemaining(rem):
                with open(r"files\remaining.txt",'r') as f:
                    curr = float(f.read())
                newrem = curr - float(rem)
                print(rem, newrem)
                if str(newrem)[-1] == '0':
                    newrem = int(newrem)
                with open(r"files\remaining.txt",'w') as f:
                    f.write(str(curr) +'\n'+str(newrem))
        writeRemaining(duration)

    def confirmLeaveRequest(self):
        self.page.get_by_label("Leave Reason *").click()
        self.page.get_by_placeholder("Reason (Max limit: 190").fill("Test Leave")

        self.page.get_by_role("button", name="Request Now").click()
        self.page.get_by_role("button", name="Ok").click()

class AcceptRequest(Dashboard):
    def __init__(self, page, managerLogin):
        self.page = page
        self.url = "https://test-pub-hris.robi.com.bd/"
        self.email, self.password, self.name = managerLogin

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

class VerifyAccepted(LeaveRequest):
    def __init__(self, page):
        self.page = page

    def checkRemaining(self, readUpdated):
        self.page.get_by_text("More").click()
        self.page.get_by_role("menuitem", name="Leave Balance").click()
        expect(self.page.locator("#automat_leave_table")).to_contain_text("Remaining " + readUpdated)
        self.page.get_by_role("button").click()

    def withdrawRequest(self):
        expect(self.page.get_by_role("button", name="Withdraw")).to_be_visible()
        # expect()
    
    # page.get_by_text("More").click()
    # page.get_by_role("menuitem", name="Leave Balance").click()
    # page.get_by_text("41").click()
    # page.get_by_text("38.5").click()
    # page.get_by_text("Remaining 38.5").click()
    # page.get_by_text("38.5").click()
    # page.get_by_text("Annual Leave Entitled 41").click(button="right")
    # page.get_by_role("button").click()
    # page.get_by_role("button", name="New Leave Request").click()
    # page.get_by_text("*You have 38.5 days of annual").click()
    # page.get_by_text("out of 41 days").click()
    # page.get_by_placeholder("Duration").click()
    # page.locator("button").filter(has_text="close").click()