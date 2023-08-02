import multiprocessing
import atexit

class Worker:
    """
        A class that represents a worker for executing a target function in a separate process.

        Attributes:
            target_func (function): The target function to be executed in the separate process.
            args (tuple): Positional arguments to be passed to the target function.
            kwargs (dict): Keyword arguments to be passed to the target function.
            process (multiprocessing.Process): The multiprocessing process instance.

        Methods:
            run(): Starts the worker process and registers an exit handler to join the process on shutdown.
            join(): Joins the worker process if it is still running.
            stop_process(): Terminates the worker process if it is still running.

        Example:
            def my_function(name, age):
                print(f"Hello, {name}. You are {age} years old.")

            worker = Worker(target_func=my_function, args=("John", 30))
            worker.run()
    """

    def __init__(self, target_func, *args, **kwargs):
        """
            Initialize a Worker instance.

            Parameters:
                target_func (function): The target function to be executed in the separate process.
                *args: Positional arguments to be passed to the target function.
                **kwargs: Keyword arguments to be passed to the target function.
        """
        self.target_func = target_func
        self.args        = args
        self.kwargs      = kwargs
        self.process     = None
        self.process     = multiprocessing.Process(
            target = self.target_func, 
            args   = self.args, 
            kwargs = self.kwargs
        )

    def run(self):
        """
            Start the worker process and register an exit handler to join the process on shutdown.
        """
        self.process.start()

        # Register an exit handler to join the process on shutdown
        atexit.register(self.join)

    def join(self):
        """
            Join the worker process if it is still running.
        """
        if self.process is not None and self.process.is_alive():
            self.process.join()

    def stop(self):
        """
            Terminate the worker process if it is still running.
        """
        if self.process is not None and self.process.is_alive():
            self.process.terminate()
