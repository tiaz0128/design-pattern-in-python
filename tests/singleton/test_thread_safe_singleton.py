import logging
import threading

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
    results = [None] * 100  # 결과 저장 리스트
    barrier = threading.Barrier(100)  # 100개의 쓰레드가 동시에 실행되도록 설정

    def wrapper(index):
        barrier.wait()  # 모든 쓰레드가 이 지점에 도달할 때까지 대기
        results[index] = func()

    for i in range(100):
        t = threading.Thread(target=wrapper, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return results  # 결과 리스트를 반환


def get_thread_singleton_instance():
    s = ThreadSafeSingleton()
    logging.info(s)

    return s


def get_lazy_singleton_instance():
    s = LazySingleton()
    logging.info(s)

    return s
