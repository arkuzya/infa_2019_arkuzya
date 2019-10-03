#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
	for i in range(2):
		move_down()
		move_right()
	fill_cell()
	move_down()
	move_right(n=2)	

    
    



if __name__ == '__main__':
    run_tasks()
