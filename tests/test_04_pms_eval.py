from tests.test_01_leave import test_loginAsManager as loginAsManager
from tests.test_03_pms import test_employeeLogin as loginAsEmployee
from models.pms import PMSSelfEvaluation, IndividualPMS, PMSEvaluationApproval

def test_loginAsEmployee(page, employeeLogin):
    loginAsEmployee(page, employeeLogin)

def test_navigateToPmsEvaluation(page, readCurrentKpiNameJson, kpiYear):
    eval = PMSSelfEvaluation(page, readCurrentKpiNameJson, kpiYear)
    eval.navigateToPmsSelfEvaluation()
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    # pms.chooseYear('2025')
    pms.navigateToKPI()
    eval.fillupKpiEvals()
    eval.submitToSupervisor()

def test_loginAsManager(page, managerLogin):
    loginAsManager(page, managerLogin)

def test_navigateToPmsEvaluationApproval(page, readEmployeeName, readCurrentKpiNameJson, kpiYear):
    approve = PMSEvaluationApproval(page)
    approve.navigateToPmsEvaluationApproval(readEmployeeName)
    pms = IndividualPMS(page, readCurrentKpiNameJson, kpiYear)
    pms.navigateToKPI()
    approve.evaluateEvaluation()
    approve.fillupManagerForms()
    




