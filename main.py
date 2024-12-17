from coop_mult_example.eventloop import EventLoop

def first_task():
    print("1: The first task has started")
    yield
    print("1: First task is doing some work")
    yield
    print("1: First task is doing some more work")
    yield
    print("1: First task has ended")

def second_task():
    print("2: Second task has started")
    yield
    print("2: Second task has ended")

def third_task():
    print("3: Third task has started")
    yield
    print("3: Third task is doing some work")
    yield
    print("3: Third task is doing some more work")
    yield
    print("3: Third task is doing some more work")
    yield
    print("3: Third task is doing some more work")
    yield
    print("3: Third task is doing some more work")
    yield
    print("3: Third task has ended")

def fourth_task():
    print("4: Fourth task has started")
    yield
    print("4: Fourth task has ended")

if __name__ == '__main__':
    try:
        task1, task2, task3, task4 = first_task, second_task, third_task, fourth_task

        loop = EventLoop()
        loop.registerTask(task1)
        loop.registerTask(task2)
        loop.registerTask(task4)
        loop.registerTask(task3)

        loop.startLoop()
    except TypeError as e:
        print(e)