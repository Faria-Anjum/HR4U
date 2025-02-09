from models.landing import Dashboard
from files.readFromJson import readCurrentKpiName, readKpiYear, readKpiCount as count, readEmployeeName
from files.writeToJson import increaseTestCounter as updateTestNo
from playwright.sync_api import expect
import re, time, random

#core and sub kpi configuration hardcoded, dynamic needs work

class IndividualPMS(Dashboard):
    def __init__(self, page):
        self.page = page
        self.kpiname = readCurrentKpiName()
        self.kpiYear = readKpiYear()

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

    def configureKPISlots(self):
        self.page.get_by_label("config slot").click()

        for i in range(1, 6):
            kpi = self.page.get_by_label(f"{self.kpiname} {self.kpiYear} 1.{i} Weightage *")
            if kpi.is_visible():
                kpi = kpi
            else:
                kpi = self.page.get_by_label(f"{self.kpiname} 1.{i} Weightage *")

            kpi.click()
            kpi.fill('20')

        self.page.get_by_role("button", name="Save").click()
        self.confirmSuccessPopup()

    def navigateToKPI(self):
        kpiButton = self.page.get_by_role("button").filter(has_text=re.compile(fr"{self.kpiname} {self.kpiYear}"))
        if kpiButton.is_visible():
            kpiButton = kpiButton
        else:
            kpiButton = self.page.get_by_role("button").filter(has_text=re.compile(fr"{self.kpiname}"))
        kpiButton.click()

    def fillupSubKPIs(self, start, stop):
        #print(count, start, stop)
        # self.page.get_by_text("Close").click()

        for kpi in range(start, stop+1):
            #print(kpi, stop)
            subkpi = self.page.get_by_text(f"{self.kpiname} {self.kpiYear} 1.{kpi}")
            if subkpi.is_visible():
                subkpi = subkpi
            else:
                subkpi = self.page.get_by_text(f"{self.kpiname} 1.{kpi}")

            subkpi.click()
            self.page.get_by_role("button", name="Create KPI").click()
            self.page.get_by_label("KPI Name *").fill(f"Sub {self.kpiname} {count()}_{kpi} (Automated)")
            self.page.get_by_label("KPI Definition *").click()
            self.page.get_by_placeholder("Write Your Kpi Definition").fill(f"Sub {self.kpiname} {kpi}")

            var = random.randint(50,80)
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
    def __init__(self, page):
        self.page = page
        self.kpiname = readCurrentKpiName()
        self.kpiYear = readKpiYear()

    def navigateToManagerDashboard(self):
        self.page.get_by_text("Manager", exact=True).click()
        self.page.get_by_text("Manager Dashboard", exact=True).click()

    def navigateToPmsApproval(self):
        self.page.get_by_text("Manage PMS").click()
        self.page.get_by_role("link", name="PMS Planning Approval").click()
        self.page.get_by_label("2025").locator("div").first.click()
        self.page.get_by_text(f"{self.kpiYear}").click()
        self.page.get_by_role("cell").filter(has_text=re.compile(fr"{readEmployeeName()}")).click()
    
    def revertKPI(self, action="Revert"):
        self.page.get_by_role("button", name="Accept/Revert").click()

        kpi = self.page.locator("label").filter(has_text=f"{self.kpiname} {self.kpiYear}")
        if kpi.is_visible():
            kpi = kpi
        else:
            kpi = self.page.locator("label").filter(has_text=f"{self.kpiname}")
        kpi.click()
        # self.page.get_by_role("checkbox", name=f"{self.kpiName} {self.kpiYear}").click()
        self.page.get_by_role("button", name=action, exact=True).click()
        
    def enterRevertReason(self):
        self.page.get_by_label("Provide clear and").click()
        self.page.get_by_placeholder("Max 1000 characters").fill(f"Reverting for test")
        self.page.get_by_role("button", name="Save").click()

        self.confirmSuccessPopup()
        self.page.goto("https://test-pub-hris.robi.com.bd/")

    def acceptKpi(self):
        self.page.get_by_role("button", name="Accept/Revert").click()
        self.page.locator("label").filter(has_text="Select All").click()
        # self.page.get_by_role("checkbox", name=f"{self.kpiName} {self.kpiYear}").click()
        self.page.get_by_role("button", name="Accept", exact=True).click()
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
        kpi = self.page.get_by_text("Individual KPI 2024 1.1")
        if kpi.is_visible():
            kpi = kpi
        else:
            kpi = self.page.get_by_text("Individual KPI 1.1")
        kpi.click()
        self.page.locator(".seconddiv > div > button").first.click()
        self.page.get_by_label("L2 *").click()
        L2 = self.page.get_by_label("L2 *").input_value()
        self.page.get_by_label("L2 *").fill(str(int(L2)+3))
        self.page.get_by_label("L4 *").click()
        L4 = self.page.get_by_label("L4 *").input_value()
        self.page.get_by_label("L4 *").fill(str(int(L4)+3))
        self.page.get_by_text("Cancel Save").click()
        self.page.get_by_role("button", name="Save").click()
        self.page.get_by_role("button", name="Ok").click()

class PMSSelfEvaluation(Dashboard):
    def __init__(self, page):
        self.page = page
        self.kpiname = readCurrentKpiName()
        self.kpiYear = readKpiYear()

    def navigateToPmsSelfEvaluation(self):
        expect(self.page.get_by_text("PMS (B21-F14)")).to_be_visible()
        self.page.get_by_text("PMS (B21-F14)").click()
        expect(self.page.get_by_role("link", name="PMS Evaluation")).to_be_visible()
        self.page.get_by_role("link", name="PMS Evaluation").click()

    def enterIndividualAchievement(self):
        expect(self.page.get_by_label("Individual Achievement *")).to_be_visible()
        val = "div.p-1.pr-2.ng-star-inserted > app-pms-dtog-slot-view > div:nth-child(9) > div:nth-child(1)"
        expect(self.page.locator(val)).to_be_visible()
        self.page.get_by_label("Individual Achievement *").click()
        self.page.get_by_label("Individual Achievement *").fill(self.page.locator(val).inner_text()[-3:])
        self.page.get_by_text("Save").click()
        self.page.get_by_text("Ok").click()

    def fillupKpiEvals(self):
        for kpi in range(1, 6):

            subkpi = self.page.get_by_text(f"{self.kpiname} {self.kpiYear} 1.{kpi}")
            if subkpi.is_visible():
                subkpi = subkpi
            else:
                subkpi = self.page.get_by_text(f"{self.kpiname} 1.{kpi}")

            subkpi.click()
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
        self.kpiname = readCurrentKpiName()
        self.kpiYear = readKpiYear()

    def navigateToPmsEvaluationApproval(self):
        self.page.get_by_text("Manage PMS").click()
        self.page.get_by_role("link", name="PMS Evaluation Approval").click()
        self.page.get_by_role("cell").filter(has_text=re.compile(fr"{readEmployeeName()}")).click()

    def evaluateEvaluation(self):
        for kpi in range(1, 6):
            subkpi = self.page.get_by_text(f"{self.kpiname} {self.kpiYear} 1.{kpi}")
            self.page.clock.fast_forward("00:15")

            
            if subkpi.is_visible():
                subkpi = subkpi
            else:
                subkpi = self.page.get_by_text(f"{self.kpiname} 1.{kpi}")

            subkpi.click()

            self.selectTheHow(random.randint(3,5))
            self.page.get_by_placeholder("Did the employee take").click()
            self.page.get_by_placeholder("Did the employee take").fill("Test Remark")

            self.page.get_by_role("button", name="Save").click()
            self.confirmSuccessPopup()

    def selectTheHow(self, val):
        expect(self.page.locator("span").filter(has_text="LM Evaluation: The 'How' *")).to_be_visible()
        self.page.locator("span").filter(has_text="LM Evaluation: The 'How' *").click()
        score = str(val)
        self.page.get_by_role("option", name=score).click()

    def fillupCoreValueAssessment(self):
        self.page.get_by_role("button").filter(has_text=re.compile(r"Form")).click()
        self.page.get_by_text(re.compile(r"Core Value Assessment")).click()
        self.page.get_by_role("button", name="OK").click()

        self.page.locator("label").filter(has_text="Living the Values").click()
        self.page.get_by_role("button", name="Save").click()
        self.confirmSuccessPopup()

    def fillupIndividualDevelopmentPlan(self):
        self.page.get_by_text("Individual Development Plan").click()
        time.sleep(0.5)
        self.page.get_by_role("tab", name="Development Plan [T&D]: Manager").click()
        time.sleep(0.5)
        # div = self.page.get_by_role("tab", name="Development Plan [T&D]: Manager").locator("div")
        yesButton = self.page.locator("mat-radio-button").filter(has_text="Yes")
        time.sleep(0.5)
        yesButton.click()

        self.page.get_by_label("Do you recommend any").click()
        self.page.get_by_placeholder("The above will be used to").fill("No")
        self.page.get_by_role("button", name="Save").click()
        self.confirmSuccessPopup()

    def submitEvaluation(self):
        self.page.get_by_role("button", name="Accept/Revert").click()
        self.page.locator("label").filter(has_text="Select All").click()
        self.page.get_by_role("button", name="Accept", exact=True).click()
        self.page.get_by_role("button", name="Save").click()
        self.confirmSuccessPopup()

    # def loginAsSecondLM(self, secondLMLogin):
    #     email, pw = secondLMLogin
