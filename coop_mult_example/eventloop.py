class EventLoop():

    def __init__(self):
        self._task_queue = []

    def registerTask(self, function):
        task = function() 
        self._task_queue.append(task)

    def startLoop(self):
        while len(self._task_queue) > 0:
            for task_id in range(0, len(self._task_queue)):
                try:
                    print(len(self._task_queue))
                    print(task_id)
                    next(self._task_queue[task_id])
                except StopIteration:
                    self._task_queue.pop(task_id)
                except IndexError:
                    break
