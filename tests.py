import unittest
from coop_mult_example.eventloop import EventLoop

class TestEventLoop(unittest.TestCase):

    def test_task_registration(self):
        eventLoop = EventLoop()
        def task1():
            i = 5
            yield
        
        eventLoop.registerTask(task1)
        self.assertEqual(len(eventLoop._task_queue),  1)

    def test_TypeError_when_task_aint_generator(self):
        eventLoop = EventLoop()
        def task1():
            i = 5

        with self.assertRaises(TypeError): 
            eventLoop.registerTask(task1)

    def test_task_loop_works_as_expected(self):
        eventLoop = EventLoop()
        def task1():
            i = 5
            yield
            i = 6
            yield
            i = 7
            yield
        
        def task2():
            h = 1
            yield
            h = 5

        eventLoop.registerTask(task1)
        eventLoop.registerTask(task2)

        eventLoop.startLoop()

        self.assertEqual(len(eventLoop._task_queue), 0)

if __name__ == '__main__':
    unittest.main()