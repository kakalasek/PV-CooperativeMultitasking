from types import GeneratorType

class EventLoop():

    def __init__(self):
        self._task_queue = []

    def registerTask(self, function):
        task = function() 
        if not isinstance(task, GeneratorType):
            raise TypeError("Provided function must be a generator")
        self._task_queue.append(task)

    def startLoop(self):
        while len(self._task_queue) > 0:
            task_id = 0
            while task_id < len(self._task_queue):
                try:
                    next(self._task_queue[task_id])
                    task_id += 1
                except StopIteration:
                    self._task_queue.pop(task_id)