from dag import DAG

class Pipeline:
    
    def __init__(self):
        self.tasks = DAG()
        

    def task(self, depends_on=None):
        def inner(func):
            if depends_on:
                self.tasks.add(depends_on, func)
            else:
                self.tasks.add(func)
            return func
        return inner
    

    def run(self):
        sorted_tasks = self.tasks.sort()
        completed = {}
        
        for task in sorted_tasks:
            for depend_on, nodes in self.tasks.graph.items():
                if task in nodes:
                    completed[task] = task(completed[depend_on])
            if task not in completed:
                completed[task] = task()
        
        return completed