import logging
import threading
import time

from singleton.meta.singleton import Singleton as LazySingleton
from singleton.thread.singleton import Singleton as ThreadSafeSingleton


def test_thread_safe_singleton():
    result = race_condition(get_thread_singleton_instance)

    assert len(set(result)) == 1


def test_lazy_singleton():
    result = race_condition(get_lazy_singleton_instance)

    assert len(set(result)) == 1


def race_condition(func):
    threads = []
    results = [None] * 100  # 결과를 저장할 리스트를 생성합니다.
    barrier = threading.Barrier(100)

    def wrapper(index):
        barrier.wait()
        results[index] = func()

    for i in range(100):
        t = threading.Thread(target=wrapper, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return results  # 결과 리스트를 반환합니다.


def get_thread_singleton_instance():
    s = ThreadSafeSingleton()
    logging.info(s)

    return s


def get_lazy_singleton_instance():
    s = LazySingleton()
    logging.info(s)

    return s
