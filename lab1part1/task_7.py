#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	k=0
	while not wall_is_beneath():
		move_down()
	while wall_is_beneath():
		k=k+1
		move_right()
	move_down()
	move_left(n=k)
	


if __name__ == '__main__':
    run_tasks()
