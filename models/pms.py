from models.landing import Dashboard
from models.writeToJson import increaseTestCounter as updateTestNo
from playwright.sync_api import expect
import re, time

#core and sub kpi configuration hardcoded, dynamic needs work

class IndividualPMS(Dashboard):
    def __init__(self, page):
        self.page = page

    def navigateToPmsPlanning(self):
        expect(self.page.get_by_text("PMS (B21-F14)")).to_be_visible()
        self.page.get_by_text("PMS (B21-F14)").click()
        expect(self.page.get_by_role("link", name="PMS Planning")).to_be_visible()
        self.page.get_by_role("link", name="PMS Planning").click()

    def chooseYear(self):
        # choose 2024 for PMS
        self.page.locator("#mat-select-value-5").click()
        self.page.get_by_text("2024").click()

    def configureCoreKPI(self, readNewKpiNameJson):
        self.page.get_by_label("config profile").click() #config core kpi
        
        self.page.get_by_role("button", name="Add").click()
        self.page.get_by_label("Profile Title").nth(1).click()
        self.page.get_by_label("Profile Title").nth(1).fill(readNewKpiNameJson)

        self.page.get_by_label("Profile Weightage *").first.click()
        self.page.get_by_label("Profile Weightage *").first.fill('80')
        self.page.get_by_label("Profile Weightage *").nth(1).click()
        self.page.get_by_label("Profile Weightage *").nth(1).fill('20')

        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Success", exact = True)).to_be_visible()
        self.page.get_by_role("button", name="Ok").click()

    def configureSubKPI(self, slots):

        self.page.get_by_label("config slot").click()
        self.page.get_by_text("Individual KPI, weightage:").click()
        self.page.get_by_role("option").filter(has_text="Test KPI").click()
        for i in range(1, slots+1):
            self.page.get_by_role("button", name="Add").click()

        self.page.get_by_label("Test KPI 2.1 Weightage *").click()
        self.page.get_by_label("Test KPI 2.1 Weightage *").fill("33.5")
        self.page.get_by_label("Test KPI 2.2 Weightage *").click()
        self.page.get_by_label("Test KPI 2.2 Weightage *").fill("33.5")
        self.page.get_by_label("Test KPI 2.3 Weightage *").click()
        self.page.get_by_label("Test KPI 2.3 Weightage *").fill("33")

        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Success", exact = True)).to_be_visible()
        self.page.get_by_role("button", name="Ok").click()

    def createKPI(self, readNewKpiNameJson, slots, count):
        kpiButton = self.page.get_by_role("button").filter(has_text=re.compile(fr"{readNewKpiNameJson}"))
        expect(kpiButton).to_be_visible()
        kpiButton.click()

        kpino = 2

        for kpi in range(1, slots+1):
            self.page.get_by_text(f"{readNewKpiNameJson} {kpino}.{kpi}").click()
            self.page.get_by_role("button", name="Create KPI").click()
            self.page.get_by_label("KPI Name *").fill(f"Sub {readNewKpiNameJson} {count}_{kpi} (Automated)")
            self.page.get_by_label("KPI Definition *").click()
            self.page.get_by_placeholder("Write Your Kpi Definition").fill(f"Sub {readNewKpiNameJson} {kpi}")

            var = 80
            for l in range(1,6):
                self.page.get_by_label(f"L{l} *").click()
                self.page.get_by_label(f"L{l} *").fill(f"{var}")
                var+=5

                self.page.get_by_label(f"L{l} Definition *").click()
                self.page.get_by_label(f"L{l} Definition *").fill(f"L{l} def")

            expect(self.page.get_by_role("button", name="Save")).to_be_visible()
            self.page.get_by_role("button", name="Save").click()

            expect(self.page.get_by_text("Success", exact = True)).to_be_visible()
            self.page.get_by_role("button", name="Ok").click()

        updateTestNo()
        
    def submitKPI(self):
        expect(self.page.get_by_role("button", name="Send to Supervisor")).to_be_visible()
        self.page.get_by_role("button", name="Send to Supervisor").click()

        expect(self.page.get_by_role("button", name="Confirm")).to_be_visible()
        self.page.get_by_role("button", name="Confirm").click()
        self.page.screenshot()

        self.page.get_by_role("button", name="Ok").click()