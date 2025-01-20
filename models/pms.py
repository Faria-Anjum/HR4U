from models.landing import Dashboard
from models.writeToJson import writeTotalSlots, writeAddSlots, writeDeleteSlots, calculatePercentage, increaseTestCounter as updateTestNo
# from models.writeToJson import readAddSlots, readDeleteSlots, readSlotCount
from playwright.sync_api import expect
import re, time, random

#core and sub kpi configuration hardcoded, dynamic needs work

class IndividualPMS(Dashboard):
    def __init__(self, page, readCurrentKpiNameJson, kpiYear):
        self.page = page
        self.kpiname = readCurrentKpiNameJson
        self.kpiYear = kpiYear

    def navigateToPmsPlanning(self):
        expect(self.page.get_by_text("PMS (B21-F14)")).to_be_visible()
        self.page.get_by_text("PMS (B21-F14)").click()
        expect(self.page.get_by_role("link", name="PMS Planning")).to_be_visible()
        self.page.get_by_role("link", name="PMS Planning").click()

    def chooseYear(self, currentYear):
        # choose 2024 for PMS
        self.page.get_by_label(f"{currentYear}").click()
        self.page.get_by_text(self.kpiYear).click()
        time.sleep(0.5)

        #resetting total default slots
        writeTotalSlots(5)

    def configureKPISlots(self):
        self.page.get_by_label("config slot").click()

        # if readAddSlots():
        #     for i in range(1, readAddSlots()+1):
        #         self.page.get_by_role("button", name="Add").click()

        # if readDeleteSlots():
        #     for i in range(1, readDeleteSlots()+1):
        #         self.page.get_by_role("button").nth(2).click()
    
        #slotFields = "#mat-dialog-0 > app-slot-configure > div.mat-dialog-content.flex.flex-col.gap-3.ps.ps--active-y > form > div"
        # slotFields = "app-slot-configure > div.mat-dialog-content.flex.flex-col.gap-3.ps.ps--active-y > form > div"
        # totalSlots = self.page.locator(slotFields).count()

        # if totalSlots == 0:
        #     slotFields = "app-slot-configure > div.mat-dialog-content.flex.flex-col.gap-3.ps > form > div"
        #     totalSlots = self.page.locator(slotFields).count()
        
        # writeTotalSlots(totalSlots)
        # print(totalSlots)
        # percentage, extra = calculatePercentage()

        # for i in range(1, totalSlots+1):
        #     self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *").click()
        #     self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *").fill(str(percentage))
        #     if i == totalSlots:
        #         self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *").click()
        #         self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *").fill(str(percentage+extra))

        for i in range(1, 6):
            self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *").click()
            self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *").fill('20')

        self.page.get_by_role("button", name="Save").click()
        self.confirmSuccessPopup()

    def navigateToKPI(self):
        kpiButton = self.page.get_by_role("button").filter(has_text=re.compile(fr"{self.kpiname} {self.kpiYear}"))
        expect(kpiButton).to_be_visible()
        
        kpiButton.click()

    def fillupSubKPIs(self, count, start, stop):
        #print(count, start, stop)
        # self.page.get_by_text("Close").click()

        for kpi in range(start, stop+1):
            #print(kpi, stop)
            self.page.get_by_text(f"{self.kpiname} {self.kpiYear} 1.{kpi}").click()
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

        updateTestNo()

    def submitKPI(self):
        expect(self.page.get_by_role("button", name="Send to Supervisor")).to_be_visible()
        self.page.get_by_role("button", name="Send to Supervisor").click()

        self.clickConfirm()
        self.confirmSuccessPopup()

class PMSApproval(Dashboard):
    def navigateToPmsApproval(self, readEmployeeName):
        self.page.get_by_text("Manage PMS").click()
        self.page.get_by_role("link", name="PMS Planning Approval").click()
        self.page.get_by_label("2025").locator("div").first.click()
        self.page.get_by_text(f"{self.kpiYear}").click()
        self.page.get_by_role("cell").filter(has_text=re.compile(fr"{readEmployeeName}")).click()
    
    def revertKPI(self, action="Revert"):
        self.page.get_by_role("button", name="Accept/Revert").click()
        self.page.locator("label").filter(has_text=f"{self.kpiName}").click()
        # self.page.get_by_role("checkbox", name=f"{self.kpiName} {self.kpiYear}").click()
        self.page.get_by_role("button", name=action, exact=True).click()
        
    def enterRevertReason(self):
        self.page.get_by_label("Provide clear and").click()
        self.page.get_by_placeholder("Max 1000 characters").fill(f"Reverting for test")
        self.page.get_by_role("button", name="Save").click()

        self.confirmSuccessPopup()
        self.page.goto("https://test-pub-hris.robi.com.bd/")

    def acceptKpi(self):
        self.revertKPI(action="Accept")
        self.confirmSuccessPopup()
        # writeDeleteSlots(readAddSlots())
        #making sure addSlots is reset
        # if readAddSlots()!=0:
        #     writeAddSlots(readAddSlots() * (-1))
        time.sleep(0.25)
        #self.page.get_by_text("Back").click()
        self.page.goto("https://test-pub-hris.robi.com.bd/")

    # def addSlot(self, val):
    #     writeAddSlots(val)

    def editSlot(self):
        self.page.get_by_text("Individual KPI 2024 1.1").click()
        self.page.locator(".seconddiv > div > button").first.click()
        self.page.get_by_label("L2 *").click()
        self.page.get_by_label("L2 *").fill("88")
        self.page.get_by_label("L4 *").click()
        self.page.get_by_label("L4 *").fill("97")
        self.page.get_by_text("Cancel Save").click()
        self.page.get_by_role("button", name="Save").click()
        self.page.get_by_role("button", name="Ok").click()

class PMSSelfEvaluation(Dashboard):
    def __init__(self, page, readCurrentKpiNameJson, kpiYear):
        self.page = page
        self.kpiname = readCurrentKpiNameJson
        self.kpiYear = kpiYear

    def navigateToPmsSelfEvaluation(self):
        expect(self.page.get_by_text("PMS (B21-F14)")).to_be_visible()
        self.page.get_by_text("PMS (B21-F14)").click()
        expect(self.page.get_by_role("link", name="PMS Evaluation")).to_be_visible()
        self.page.get_by_role("link", name="PMS Evaluation").click()

    def enterIndividualAchievement(self):
        expect(self.page.get_by_label("Individual Achievement *")).to_be_visible()
        # val =  "body > app-root > layout > classic-layout > div > div.flex.flex-col.flex-auto > app-ess-pms-evaluation > div > div > div > div:nth-child(2) > div > div.seconddiv-ev.min-w-\[328px\].min-h-\[calc\(100vh-150px\)\] > div.p-1.pr-2.ng-star-inserted > app-pms-dtog-slot-view > div:nth-child(9) > div:nth-child(1)"
        val = "div.p-1.pr-2.ng-star-inserted > app-pms-dtog-slot-view > div:nth-child(9) > div:nth-child(1)"
        expect(self.page.locator(val)).to_be_visible()
        self.page.get_by_label("Individual Achievement *").click()
        self.page.get_by_label("Individual Achievement *").fill(self.page.locator(val).inner_text()[-3:])
        self.page.get_by_text("Save").click()
        self.page.get_by_text("Ok").click()

    def fillupKpiEvals(self):
        for kpi in range(1, 6):
            self.page.get_by_text(f"{self.kpiname} {self.kpiYear} 1.{kpi}").click()
            self.enterIndividualAchievement()
        
    def submitToSupervisor(self):
        expect(self.page.get_by_role("button", name="Bulk Send to Supervisor")).to_be_visible()
        self.page.get_by_role("button", name="Bulk Send to Supervisor").click()

        expect(self.page.get_by_role("button", name="Confirm")).to_be_visible()
        self.page.get_by_role("button", name="Confirm").click()

        self.confirmSuccessPopup()

class PMSEvaluationApproval(Dashboard):
    def __init__(self, page):
        self.page = page

    def navigateToPmsEvaluationApproval(self, readEmployeeName):
        self.page.get_by_text("Manage PMS").click()
        self.page.get_by_role("link", name="PMS Evaluation Approval").click()
        self.page.get_by_role("cell").filter(has_text=re.compile(fr"{readEmployeeName}")).click()

    def evaluateEvaluation(self):
        for kpi in range(1, 6):
            self.page.get_by_text(f"{self.kpiname} {self.kpiYear} 1.{kpi}").click()

            self.selectTheHow()
            self.page.get_by_placeholder("Did the employee take").click()
            self.page.get_by_placeholder("Did the employee take").fill("Test Remark")

            self.page.get_by_role("button", name="Save").click()
            self.confirmSuccessPopup()

    def selectTheHow(self):
        expect(self.page.locator("span").filter(has_text="LM Evaluation: The 'How' *")).to_be_visible()
        self.page.locator("span").filter(has_text="LM Evaluation: The 'How' *").click()
        score = str(random.randint(3,5))
        self.page.get_by_text(score, exact=True).click()

    def fillupManagerForms(self):
        self.page.get_by_role("button", name="Form (2)").click()
        self.page.get_by_text("Core Value Assessment * Pending")
        self.page.get_by_role("button", name="OK").click()
        self.page.locator("label").filter(has_text="Living the Values").click()

    # self.page.get_by_role("button", name="Form (2)").click()
    # self.page.get_by_text("Core Value Assessment * Pending").click()
    # self.page.locator("#mat-radio-3 > .mat-radio-label > .mat-radio-container").click()
    # self.page.locator("#mat-radio-4 > .mat-radio-label > .mat-radio-container > .mat-radio-outer-circle").click()
    # self.page.locator("label").filter(has_text="Obsession For Customers").click()
    # self.page.get_by_text("Below Par").click()
    # self.page.locator("#mat-radio-3 > .mat-radio-label > .mat-radio-container").click()
    # self.page.locator("a").filter(has_text="See Core Value Description").click()
    # self.page.get_by_label("Close dialog").click()
    # self.page.locator("a").filter(has_text="Core Values Rating Scale").click()
    # self.page.get_by_role("button", name="OK").click()
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_text("Individual Development Plan").click()
    # self.page.get_by_text("Development Plan [T&D]: Manager").click()
    # self.page.get_by_role("button", name="Accept/Revert").click()
    # self.page.get_by_text("Individual Kpi 2024", exact=True).click()
    # self.page.locator("#mat-menu-panel-2 div").filter(has_text="Core Value Assessment").nth(1).click()
    # self.page.locator("#mat-menu-panel-2 div").filter(has_text="Core Value Assessment").nth(1).click()
    # self.page.locator("#mat-checkbox-3 > .mat-checkbox-layout > .mat-checkbox-inner-container").click()
    # self.page.locator("#mat-checkbox-4 > .mat-checkbox-layout > .mat-checkbox-inner-container").click()
    # self.page.get_by_role("button", name="Accept", exact=True).click()
    # self.page.locator(".cdk-overlay-backdrop").click()
    # self.page.get_by_text("Individual Development Plan 2024 * Pending").click()
    # self.page.get_by_text("Development Plan [T&D]: Employee").click()
    # self.page.get_by_role("tab", name="Development Plan [T&D]: Manager").locator("div").click()
    # self.page.get_by_text("Development Plan [T&D]: Employee").click()
    # self.page.get_by_role("tab", name="Development Plan [T&D]: Manager").locator("div").click()
    # self.page.get_by_text("Yes").click()
    # self.page.get_by_label("Do you recommend any").click()
    # self.page.get_by_placeholder("The above will be used to").fill("/no")
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_text("Core Value Assessment * Pending").click()
    # self.page.get_by_role("button", name="KPI (1)").click()
    # self.page.get_by_role("button", name="Individual KPI 2024 * Pending").click()
    # self.page.get_by_label("KPI (1)").get_by_text("Individual KPI 2024 1.2").click()
    # self.page.locator("#mat-select-value-13").click()
    # self.page.get_by_text("5", exact=True).click()
    # self.page.get_by_placeholder("Did the employee take").click()
    # self.page.get_by_placeholder("Did the employee take").fill("Test Remark")
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_label("KPI (1)").get_by_text("Individual KPI 2024 1.4").click()
    # self.page.locator("#mat-select-value-13").click()
    # self.page.get_by_text("3", exact=True).click()
    # self.page.get_by_placeholder("Did the employee take").click()
    # self.page.get_by_placeholder("Did the employee take").fill("Test Remark")
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_label("KPI (1)").get_by_text("Individual KPI 2024 1.5").click()
    # self.page.locator("#mat-select-value-13").click()
    # self.page.get_by_text("2", exact=True).click()
    # self.page.locator("#mat-select-value-13").click()
    # self.page.get_by_text("5", exact=True).click()
    # self.page.get_by_placeholder("Did the employee take").click()
    # self.page.get_by_placeholder("Did the employee take").fill("Test remark")
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_label("KPI (1)").get_by_text("Individual KPI 2024 1.3").click()
    # self.page.locator("#mat-select-value-13").click()
    # self.page.get_by_text("5", exact=True).click()
    # self.page.get_by_placeholder("Did the employee take").click()
    # self.page.get_by_placeholder("Did the employee take").fill("Test remark")
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.get_by_role("button", name="Accept/Revert").click()
    # self.page.get_by_role("button", name="Accept", exact=True).click()
    # self.page.locator(".mat-slide-toggle-thumb").click()
    # self.page.locator(".mat-slide-toggle-thumb").click()
    # self.page.get_by_role("button", name="Save").click()
    # self.page.get_by_role("button", name="Ok").click()
    # self.page.locator(".cdk-overlay-backdrop").click()


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
        # for i in range(1, slots+1):
        #     self.page.get_by_role("button", name="Add").click()

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