from tests.tests_02_leave.test_a_leave import test_loginAsManager as loginAsManager, test_logout as logout
from tests.tests_03_pms.test_a_request_kpi import test_employeeLogin as loginAsEmployee
from models.pms import PMSSelfEvaluation, IndividualPMS, PMSEvaluationApproval

def test_loginAsEmployee(page, employeeLogin):
    loginAsEmployee(page, employeeLogin)

def test_navigateToPmsEvaluation(page, readCurrentKpiNameJson, kpiYear):
    eval = PMSSelfEvaluation(page, readCurrentKpiNameJson, kpiYear)
    # page.pause()
    eval.navigateToPmsSelfEvaluation()
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    # pms.chooseYear('2025')
    pms.navigateToKPI()
    eval.fillupKpiEvals()
    eval.submitToSupervisor()

def test_employeeLogout(page, employeeLogin):
    logout(page, employeeLogin)

def test_loginAsManager(page, managerLogin):
    loginAsManager(page, managerLogin)

def test_navigateToPmsEvaluationApproval(page, readEmployeeName, readCurrentKpiNameJson, kpiYear):
    # page.pause()
    approve = PMSEvaluationApproval(page, readCurrentKpiNameJson, kpiYear)
    approve.navigateToPmsEvaluationApproval(readEmployeeName)
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    pms.navigateToKPI()
    
def test_completePmsEvaluation(page, readCurrentKpiNameJson, kpiYear):
    approve = PMSEvaluationApproval(page, readCurrentKpiNameJson, kpiYear)
    approve.evaluateEvaluation()
    approve.fillupCoreValueAssessment()
    approve.fillupIndividualDevelopmentPlan()
    approve.submitEvaluation()

