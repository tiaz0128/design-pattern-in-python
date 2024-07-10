from unittest.mock import patch

from singleton.meta.singleton import Singleton


def test_meta_singleton():
    obj_1 = Singleton(1)
    obj_2 = Singleton(2)

    assert obj_1 is obj_2
