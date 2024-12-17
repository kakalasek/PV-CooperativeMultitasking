from coop_mult_example.eventloop import EventLoop

def test_func():
    print("uno")
    yield
    print("dos")
    yield
    print("tres")


if __name__ == '__main__':
    task1 = test_func
    task2 = test_func
    task3 = test_func

    loop = EventLoop()
    loop.registerTask(task1)
    loop.registerTask(task2)
    loop.registerTask(task3)

    loop.startLoop()