import sys
import os
import time
from datetime import timedelta
from pyats.easypy import Task
import argparse


def run_task(testscript, taskid, runtime, **kwargs):

    task = Task(testscript=testscript, taskid=taskid, runtime=runtime, **kwargs)
    task.start()
    return task

# Main block
def main(runtime):

    parser = argparse.ArgumentParser(description="Custom argument parser for pyATS job.")
    parser.add_argument('--num1', type=int, required=True, help='First number for the test scripts.')
    parser.add_argument('--num2', type=int, required=True, help='Second number for the test scripts.')
    parser.add_argument('--runtime', type=int, default=300, help='Runtime for each task in seconds.')


    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])


    prefix = os.path.dirname(os.path.abspath(__file__))
    print("Directory of the job file:", prefix)

    task_id_subtraction = 'subtraction_task'
    task_id_addition = 'addition_task'
    task_id_multiplication = 'multiplication_task'
    task_id_division = 'division_task'
    max_runtime = args.runtime


    division_task = run_task(
        testscript=os.path.join(prefix, 'division_script.py'),
        taskid=task_id_division,
        runtime=runtime,
        num1=args.num1,
        num2=args.num2
    )

    addition_task = run_task(
        testscript=os.path.join(prefix, 'addition_script.py'),
        taskid=task_id_addition,
        runtime=runtime,
        num1=args.num1,
        num2=args.num2
    )

    subtraction_task = run_task(
        testscript=os.path.join(prefix, 'subtraction_script.py'),
        taskid=task_id_subtraction,
        runtime=runtime,
        num1=args.num1,
        num2=args.num2
    )

    multiplication_task = run_task(
        testscript=os.path.join(prefix, 'multiplication_script.py'),
        taskid=task_id_multiplication,
        runtime=runtime,
        num1=args.num1,
        num2=args.num2
    )


    counter = timedelta(minutes=5)
    while counter:
        if (division_task.is_alive() or
                addition_task.is_alive() or
                subtraction_task.is_alive() or
                multiplication_task.is_alive()):

            time.sleep(1)
            counter -= timedelta(seconds=1)
        else:

            print("All tasks completed within the allowed time.")
            break
    else:

        print("Exceeded maximum allowed runtime. Terminating tasks...")
        division_task.terminate()
        addition_task.terminate()
        subtraction_task.terminate()
        multiplication_task.terminate()


        division_task.join()
        addition_task.join()
        subtraction_task.join()
        multiplication_task.join()


        raise TimeoutError('Not all tasks finished within the 5-minute limit!')


    print("Subtraction task result:", subtraction_task.result)
    print("Multiplication task result:", multiplication_task.result)
    print("Addition task result:", addition_task.result)
    print("Division task result:", division_task.result)


if __name__ == "__main__":
    main(runtime=None)
