from models.landing import Dashboard
from playwright.sync_api import expect
import re, time

class IndividualPMS(Dashboard):
    def __init__(self, page):
        self.page = page

    def navigateToPmsPlanning(self):
        expect(self.page.get_by_text("PMS (B21-F14)")).to_be_visible()
        self.page.get_by_text("PMS (B21-F14)").click()
        expect(self.page.get_by_role("link", name="PMS Planning")).to_be_visible()
        self.page.get_by_role("link", name="PMS Planning").click()

    def chooseIndividualKpi(self):
        self.page.locator("#mat-select-value-5").click()
        self.page.get_by_text("2024").click()
        expect(self.page.get_by_role("button", name="Individual KPI * Open")).to_be_visible()
        self.page.get_by_role("button", name="Individual KPI * Open").click()

    def createKPI(self):
        pass
        # self.page.get_by_label("config profile").click()
        # self.page.get_by_label("Profile Weightage *").click()
        # self.page.get_by_label("Profile Title").click()

        # self.page.get_by_label("config slot").click()
        # self.page.get_by_label("Individual KPI, weightage:").click()
        # self.page.locator(".cdk-overlay-container > div:nth-child(3)").click()
        # self.page.get_by_role("button").nth(2).click()
        # self.page.get_by_role("button", name="Add").click()

        # for i in range(4):


#     self.page.locator(".ng-tns-c128-16 > .fuse-vertical-navigation-item-wrapper > .mat-tooltip-trigger").click()
#     self.page.get_by_role("link", name="PMS Planning").click()
#     self.page.locator("#mat-select-value-5").click()
#     self.page.get_by_text("2024").click()
#     self.page.get_by_role("button", name="Individual KPI * Open").click()
#     self.page.get_by_text("Individual KPI 1.2").click()
#     self.page.get_by_role("button", name="Create KPI").click()
#     self.page.get_by_label("KPI Name *").fill("Sub KPI 2")
#     self.page.get_by_label("KPI Definition *").click()
#     self.page.get_by_placeholder("Write Your Kpi Definition").fill("Sub KPI 2")
#     self.page.get_by_label("L1 *").click()
#     self.page.get_by_label("L1 *").fill("90")
#     self.page.get_by_label("L2 *").click()
#     self.page.get_by_label("L2 *").fill("85")
#     self.page.get_by_label("L3 *").click()
#     self.page.get_by_label("L3 *").fill("100")
#     self.page.get_by_label("L4 *").click()
#     self.page.get_by_label("L4 *").fill("80")
#     self.page.get_by_label("L5 *").click()
#     self.page.get_by_label("L5 *").fill("85")
#     self.page.get_by_label("L1 Definition *").click()
#     self.page.get_by_label("L1 Definition *").fill("L! def")
#     self.page.get_by_label("L2 Definition *").click()
#     self.page.get_by_label("L1 Definition *").click()
#     self.page.get_by_label("L1 Definition *").fill("L1 def")
#     self.page.get_by_label("L2 Definition *").click()
#     self.page.get_by_label("L2 Definition *").fill("L2 def")
#     self.page.get_by_label("L3 Definition *").click()
#     self.page.get_by_label("L3 Definition *").fill("L3 def")
#     self.page.get_by_label("L4 Definition *").click()
#     self.page.get_by_label("L4 Definition *").fill("L4 def")
#     self.page.get_by_label("L5 Definition *").click()
#     self.page.get_by_label("L5 Definition *").fill("L5 def")
#     expect(self.page.get_by_role("button", name="Save")).to_be_visible()
#     self.page.locator("button").filter(has_text="close").click()
#     self.page.get_by_text("PMS (B21-F14)").click()

#     self.page.get_by_role("link", name="PMS Planning").click()
#     self.page.locator("#mat-select-value-5").click()
#     self.page.get_by_text("2024").click()
#     self.page.get_by_label("config profile").click()
#     self.page.get_by_label("Profile Weightage *").click()
#     self.page.get_by_label("Profile Title").click()
#     self.page.locator("button").filter(has_text="close").click()
#     self.page.get_by_label("config slot").click()
#     self.page.get_by_label("Individual KPI, weightage:").click()
#     self.page.locator(".cdk-overlay-container > div:nth-child(3)").click()
#     self.page.get_by_role("button").nth(2).click()
#     self.page.get_by_role("button", name="Add").click()
#     self.page.get_by_label("Individual KPI 1.5 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.5 Weightage *").fill("20")
#     self.page.get_by_label("Individual KPI 1.1 Weightage *").click()
#     self.page.get_by_role("button").nth(2).click()
#     self.page.get_by_label("Individual KPI 1.1 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.1 Weightage *").fill("25")
#     self.page.get_by_label("Individual KPI 1.2 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.2 Weightage *").fill("25")
#     self.page.get_by_label("Individual KPI 1.3 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.3 Weightage *").fill("25")
#     self.page.get_by_label("Individual KPI 1.4 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.4 Weightage *").fill("25")
#     self.page.locator("button").filter(has_text="close").click()
#     self.page.get_by_role("button", name="Individual KPI * Open").click()
#     self.page.get_by_role("button", name="Individual KPI * Open").click()
#     self.page.get_by_label("config slot").click()
#     self.page.get_by_label("Individual KPI, weightage:").click()
#     self.page.get_by_label("Individual KPI, weightage:").click()
#     self.page.locator(".cdk-overlay-container > div:nth-child(3)").click()
#     self.page.get_by_label("Individual KPI 1.1 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.1 Weightage *").fill("25")
#     self.page.get_by_label("Individual KPI 1.2 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.2 Weightage *").fill("25")
#     self.page.get_by_label("Individual KPI 1.3 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.3 Weightage *").fill("25")
#     self.page.get_by_label("Individual KPI 1.4 Weightage *").click()
#     self.page.get_by_label("Individual KPI 1.4 Weightage *").fill("25")
#     self.page.get_by_role("button").nth(2).click()
#     self.page.get_by_label("KPI Slot Configuration Total").locator("div").filter(has_text="Save").click()
#     self.page.get_by_role("button", name="Ok").click()
#     self.page.get_by_role("button", name="Individual KPI * Open").click()
#     self.page.get_by_text("Individual KPI 1.1").click()
#     self.page.get_by_role("button", name="Create KPI").click()
#     self.page.locator("button").filter(has_text="close").click()