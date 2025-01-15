from models.landing import Dashboard
from models.writeToJson import writeTotalSlots, writeAddSlots, calculatePercentage, increaseTestCounter as updateTestNo
from playwright.sync_api import expect
import re, time

#core and sub kpi configuration hardcoded, dynamic needs work

class IndividualPMS(Dashboard):
    def __init__(self, page, readCurrentKpiNameJson):
        self.page = page
        self.kpiname = readCurrentKpiNameJson

    def navigateToPmsPlanning(self):
        expect(self.page.get_by_text("PMS (B21-F14)")).to_be_visible()
        self.page.get_by_text("PMS (B21-F14)").click()
        expect(self.page.get_by_role("link", name="PMS Planning")).to_be_visible()
        self.page.get_by_role("link", name="PMS Planning").click()

    def chooseYear(self, kpiYear):
        # choose 2024 for PMS
        self.page.locator("#mat-select-value-5").click()
        self.page.get_by_text(kpiYear).click()

    def configureKPISlots(self, kpiYear, readAddSlots, readDeleteSlots):
        self.page.get_by_label("config slot").click()

        if readAddSlots:
            for i in range(1, readAddSlots+1):
                self.page.get_by_role("button", name="Add").click()

        if readDeleteSlots:
            for i in range(1, readDeleteSlots+1):
                self.page.get_by_role("button").nth(2).click()

        slotFields = "#mat-dialog-0 > app-slot-configure > div.mat-dialog-content.flex.flex-col.gap-3.ps.ps--active-y > form > div"
        totalSlots = self.page.locator(slotFields).count()

        if totalSlots == 0:
            slotFields = "#mat-dialog-0 > app-slot-configure > div.mat-dialog-content.flex.flex-col.gap-3.ps > form > div"
            totalSlots = self.page.locator(slotFields).count()
        
        writeTotalSlots(totalSlots)
        percentage, extra = calculatePercentage()

        for i in range(1, totalSlots+1):
            self.page.get_by_label(f"{self.kpiname} {kpiYear} 1.{i} Weightage *").click()
            self.page.get_by_label(f"{self.kpiname} {kpiYear} 1.{i} Weightage *").fill(str(percentage))
            if i == totalSlots:
                self.page.get_by_label(f"{self.kpiname} {kpiYear} 1.{i} Weightage *").click()
                self.page.get_by_label(f"{self.kpiname} {kpiYear} 1.{i} Weightage *").fill(str(percentage+extra))

        self.page.get_by_role("button", name="Save").click()
        self.confirmSuccessPopup()

    def fillupSubKPIs(self, count, readSlotCount, kpiYear):
        kpiButton = self.page.get_by_role("button").filter(has_text=re.compile(fr"{self.kpiname} {kpiYear}"))
        expect(kpiButton).to_be_visible()
        kpiButton.click()

        for kpi in range(1, readSlotCount+1):
            self.page.get_by_text(f"{self.kpiname} {kpiYear} 1.{kpi}").click()
            self.page.get_by_role("button", name="Create KPI").click()
            self.page.get_by_label("KPI Name *").fill(f"Sub {self.kpiname} {count}_{kpi} (Automated)")
            self.page.get_by_label("KPI Definition *").click()
            self.page.get_by_placeholder("Write Your Kpi Definition").fill(f"Sub {self.kpiname} {kpi}")

            var = 80
            for l in range(1,6):
                self.page.get_by_label(f"L{l} *").click()
                self.page.get_by_label(f"L{l} *").fill(f"{var}")
                var+=5

                self.page.get_by_label(f"L{l} Definition *").click()
                self.page.get_by_label(f"L{l} Definition *").fill(f"L{l} def")

            expect(self.page.get_by_role("button", name="Save")).to_be_visible()
            self.page.get_by_role("button", name="Save").click()

            self.confirmSuccessPopup()

    def submitKPI(self):
        expect(self.page.get_by_role("button", name="Send to Supervisor")).to_be_visible()
        self.page.get_by_role("button", name="Send to Supervisor").click()

        self.clickConfirm()
        self.confirmSuccessPopup()

class PMSApproval(Dashboard):
    def __init__(self, page):
        self.page = page

    def navigateToPmsApproval(self, readEmployeeName):
        self.page.get_by_text("Manage PMS").click()
        self.page.get_by_role("link", name="PMS Planning Approval").click()
        self.page.get_by_label("2025").locator("div").first.click()
        self.page.get_by_text("2024").click()
        self.page.get_by_role("cell").filter(has_text=re.compile(fr"{readEmployeeName}")).click()
    
    def revertKPI(self):
        self.page.get_by_role("button", name="Accept/Revert").click()
        self.page.get_by_text("Individual Kpi 2024", exact=True).click()
        self.page.get_by_role("button", name="Revert", exact=True).click()
        self.page.get_by_label("Provide clear and").click()
        self.page.get_by_placeholder("Max 1000 characters").fill("Reverting for test")
        self.page.get_by_role("button", name="Save").click()

        self.confirmSuccessPopup()

    # def changeRevertedKPI(self):



#If creating a new KPI from user dashboard
class NewPMS(IndividualPMS):
    def __init__(self, page):
        self.page = page

    def configureNewCoreKPI(self, readNewKpiNameJson):
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

    #When creating a new KPI from user dashboard
    def configureThreeKPISlots(self, slots):
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

    #When creating a new KPI from user dashboard
    def createNewSubKPI(self, readNewKpiNameJson, slots, count):
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

            self.confirmSuccessPopup()

        updateTestNo()