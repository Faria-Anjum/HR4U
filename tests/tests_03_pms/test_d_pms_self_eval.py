from tests.tests_01_landing.test_b_handset_claim import test_loginAsEmployee as employeelogin
from tests.tests_02_leave.test_a_leave import test_loginAsManager as managerlogin, test_logout as logout
from models.pms import PMSSelfEvaluation, IndividualPMS, PMSEvaluationApproval

def test_loginAsEmployee(page):
    employeelogin(page)

def test_navigateToPmsEvaluation(page):
    eval = PMSSelfEvaluation(page)
    page.pause()
    eval.navigateToPmsSelfEvaluation()
    pms = IndividualPMS(page)
    pms.navigateToKPI()
    eval.fillupKpiEvals()
    eval.submitToSupervisor()

def test_employeeLogout(page):
    logout(page)

def test_loginAsManager(page):
    managerlogin(page)

def test_navigateToPmsEvaluationApproval(page):
    # page.pause()
    approve = PMSEvaluationApproval(page)
    approve.navigateToPmsEvaluationApproval()
    pms = IndividualPMS(page)
    pms.navigateToKPI()

    page.clock.fast_forward("01:00")
    
def test_completePmsEvaluation(page):
    approve = PMSEvaluationApproval(page)
    approve.evaluateEvaluation()
    approve.fillupCoreValueAssessment()
    approve.fillupIndividualDevelopmentPlan()
    approve.submitEvaluation()