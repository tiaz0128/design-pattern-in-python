from facade.main import ConcreteFacade, SubsystemA, SubsystemB, SubsystemC


def test_facade():
    a = SubsystemA()
    b = SubsystemB()
    c = SubsystemC()

    facade = ConcreteFacade(a, b, c)

    assert isinstance(facade, ConcreteFacade)

    assert isinstance(facade._subsystem_a, SubsystemA)
    assert isinstance(facade._subsystem_b, SubsystemB)
    assert isinstance(facade._subsystem_c, SubsystemC)

    assert (
        facade.operation()
        == "Facade initializes subsystems:\nSubsystem A: Ready!\nSubsystem B: Ready!\nSubsystem C: Ready!"
    )
