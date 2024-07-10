from singleton.thread.singleton import Singleton


def test_thread_safe_singleton():
    obj_1 = Singleton()
    obj_2 = Singleton()

    assert obj_1 is obj_2
