# -*- coding: utf-8 -*-
from MetroTransit.MetroTiming  import MetroTiming as data
import time,sys

main_data = data()

NORTH = 4
SOUTH = 1
EAST = 2
WEST = 3

input_route = sys.argv[1]
input_stop = sys.argv[2]
input_direction = sys.argv[3]

'''
#Tested with below inputs
input_route = 'METRO Blue Line'
input_stop = 'Target Field Station Platform 1'
input_direction = SOUTH
'''

def get_route_number():
    routes=main_data.routes_operation()
    for i in routes:
        if  input_route in i['Description']:
            return i['Route']

def get_stops(route_number, direction):
        Stops = main_data.stops_operation(route_number, SOUTH)
        for i in Stops:
            if input_stop in i['Text']:
                return i['Value']

def main():
    route_number=get_route_number()
    a=time.time()
    stopage = get_stops(route_number, input_direction)
    time_dept = main_data.timepoint_departures_operation(route_number, input_direction, stopage)
    next_dept = float(time_dept[0]['DepartureTime'][6:16])
    time_remaining = int(next_dept - a) // 60
    return time_remaining


if __name__ == '__main__':
    a=main()
    print(a,"Minutes")


