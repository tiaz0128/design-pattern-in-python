from abc import ABC, abstractmethod
from enum import Enum, auto
from random import choice


class ApprovalLevel(Enum):
    TEAM_LEAD = auto()
    SENIOR_MANAGER = auto()
    VICE_PRESIDENT = auto()
    PRESIDENT = auto()


class Report:
    def __init__(self, content, required_approval_level: ApprovalLevel):
        self.content = content
        self.required_approval_level = required_approval_level


class Approver(ABC):
    def __init__(self, level):
        self.level = level
        self.next_approver = None

    def set_next(self, approver):
        self.next_approver = approver
        return approver

    def process_report(self, report):
        is_approved = False
        if self.level.value <= report.required_approval_level.value:
            is_approved = self.approve(report)

        if self.next_approver and is_approved:
            return self.next_approver.process_report(report)
        return False

    @abstractmethod
    def approve(self, report):
        pass

    def get_title(self, is_approved, is_final_approval) -> tuple[str, str]:
        approve_msg = "승인" if is_approved else "반려"

        if is_final_approval:
            return "✅종결" if is_approved else "❌반려", approve_msg

        return "✨진행" if is_approved else "❌반려", approve_msg


class TeamLead(Approver):
    def __init__(self):
        super().__init__(ApprovalLevel.TEAM_LEAD)

    def approve(self, report):
        is_approved = choice([True, False])
        is_final_approval = report.required_approval_level == self.level

        title, approve_msg = self.get_title(is_approved, is_final_approval)
        print(f'{title} : 팀장이 ~{report.content}~ 보고서를 "{approve_msg}"했습니다')
        return is_approved


class VicePresident(Approver):
    def __init__(self):
        super().__init__(ApprovalLevel.VICE_PRESIDENT)

    def approve(self, report):
        is_approved = choice([True, False])
        is_final_approval = report.required_approval_level == self.level

        title, approve_msg = self.get_title(is_approved, is_final_approval)
        print(f'{title} : 부사장이 ~{report.content}~ 보고서를 "{approve_msg}"했습니다')
        return is_approved


class President(Approver):
    def __init__(self):
        super().__init__(ApprovalLevel.PRESIDENT)

    def approve(self, report):
        is_approved = choice([True, False])
        is_final_approval = report.required_approval_level == self.level

        title, approve_msg = self.get_title(is_approved, is_final_approval)
        print(f'{title} : 사장이 ~{report.content}~ 보고서를 "{approve_msg}"했습니다')

        return is_approved


def setup_approval_chain():
    team_lead = TeamLead()
    vice_president = VicePresident()
    president = President()

    team_lead.set_next(vice_president).set_next(president)

    return team_lead
