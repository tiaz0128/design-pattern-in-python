from singleton.meta.singleton import Singleton


def test_meta_singleton():
    obj_1 = Singleton()
    obj_2 = Singleton()

    assert obj_1 is obj_2
