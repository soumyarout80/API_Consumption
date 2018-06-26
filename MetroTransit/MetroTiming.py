# -*- coding: utf-8 -*-
'''
Created by Soumya Ranjan Rout on 25/6/2018
'''
import requests

class MetroTiming(object):
    """
    This class is for extract data from url [http://svc.metrotransit.org] with diffrent
    value . There are 7 methords for diffrent data endpoint and all functions will pass though one common function
    "get_data" to convert data in to json format.
    """

    def routes_operation(self):
        """
        This operation returns a list of Transit routes that are in service on the current day.
        :return:
        """
        url = 'http://svc.metrotransit.org/NexTrip/Routes?format=json'
        return self.get_json_data(url)


    def stops_operation(self, route, direction):
        """
        This methord returns a list of Timepoint stops for the given Route/Direction.
        The result includes text/value pairs with the stop description and a 4 character stop (or node) identifier.
        :param route:
        :param direction:
        :return:
        """
        url = "http://svc.metrotransit.org/NexTrip/Stops/{0}/{1}?format=json".format(route, direction)
        return self.get_json_data(url)


    def timepoint_departures_operation(self, route, direction, stop):
        """
        This methord returns the scheduled departures for a selected route, direction and timepoint stop.
        :param route:5
        :param direction:SOUTH
        :param stop:
        :return:
        """
        url_template = 'http://svc.metrotransit.org/NexTrip/{0}/{1}/{2}?format=json'.format(route, direction, stop)
        return self.get_json_data(url_template)

    def get_json_data(self,url):
        """"
        This methord will take the api url and return the data in json format
        :return: [{'Description': 'METRO Blue Line', 'ProviderID': '8', 'Route': '901'}, {'Description': 'METRO Green Line', 'ProviderID': '8', 'Route': '902'},........
        """
        response = requests.get(url)
        return response.json()

