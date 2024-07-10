from singleton.gof.singleton import Singleton


def test_gof_singleton():
    obj_1 = Singleton.get_instance()
    obj_2 = Singleton.get_instance()

    assert obj_1 is obj_2
