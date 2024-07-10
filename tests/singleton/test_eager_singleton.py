from singleton.eager.singleton import Singleton


def test_eager_singleton():
    obj_1 = Singleton()
    obj_2 = Singleton()

    assert obj_1 is obj_2
