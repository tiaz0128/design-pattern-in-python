from abc import ABC, abstractmethod


class Facade(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class SubsystemA:
    def operation_a(self) -> str:
        return "Subsystem A: Ready!"


class SubsystemB:
    def operation_b(self) -> str:
        return "Subsystem B: Ready!"


class SubsystemC:
    def operation_c(self) -> str:
        return "Subsystem C: Ready!"


class ConcreteFacade(Facade):
    def __init__(
        self, subsystem_a: SubsystemA, subsystem_b: SubsystemB, subsystem_c: SubsystemC
    ):
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b
        self._subsystem_c = subsystem_c

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_a.operation_a())
        results.append(self._subsystem_b.operation_b())
        results.append(self._subsystem_c.operation_c())
        return "\n".join(results)
