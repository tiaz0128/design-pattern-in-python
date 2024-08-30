from chain_of_responsibility.coin import calculate_change
from chain_of_responsibility.logger import LogLevel, setup_chain
from chain_of_responsibility.report import ApprovalLevel, Report, setup_approval_chain


def test_coin():
    calculate_change(1680)


def test_logger():
    logger_chain = setup_chain()

    logger_chain.log(LogLevel.INFO, "This is an information.")
    logger_chain.log(LogLevel.DEBUG, "This is a debug information.")
    logger_chain.log(LogLevel.ERROR, "This is an error!")


def test_report():
    approval_chain = setup_approval_chain()

    report1 = Report("일일 업무 보고", ApprovalLevel.TEAM_LEAD)
    report2 = Report("분기별 실적 보고", ApprovalLevel.VICE_PRESIDENT)
    report3 = Report("연간 전략 계획", ApprovalLevel.PRESIDENT)

    print("\n")
    approval_chain.process_report(report1)
    print("\n")
    approval_chain.process_report(report2)
    print("\n")
    approval_chain.process_report(report3)
