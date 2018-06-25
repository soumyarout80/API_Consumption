# Case Study
## MetroTransit
Api Consumption module to tell you how long it is until the next bus on “BUS ROUTE” leaving from “BUS STOP NAME” going “DIRECTION” using the api defined at http://svc.metrotransit.org/ .
### MetroTiming.py
```
This is a python class which get the exact url and format it in json format and store as object.
```
### nextbus.py
```
This is a python script  which will call the class after accept arguments from user.
```
### input of nextbus.py
input_route = 'METRO Blue Line'
input_stop = 'Target Field Station Platform 1'
input_direction = SOUTH
### output of nextbus.py
5 Minutes

## Systems Programming
```
getdiskusage.py a program which will take a mount point as an argument and return a list of all the files on the mountpoint and their disk usage in bytes in json format.
```
### output of getdiskusage.py without argument
soumya@Ubuntu-18:~$ python3 test-disk.py
```
Sequence index out of range.
Oops!No argument||Please pass a directory name.
Local name referenced but not bound to a value.
Oops!Wrong path||Please enter a valid path.
```
### output of getdiskusage.py with argument
```
soumya@Ubuntu-18:~$ python3 test-disk.py /tmp
{"files": [["/tmp/terraform-log393656872", 2075], ["/tmp/winstone637069100051927219.jar", 2146767], ["/tmp/terraform-log499818461", 1504823]]}
```

## Author

* **Soumya Ranjan Rout** - *DevOps Engineer* - [Gitrepo](https://github.com/soumyarout80)

