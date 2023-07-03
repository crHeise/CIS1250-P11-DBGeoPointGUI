# Programmer: Chris Heise (crheise@icloud.com)
# School: Central New Mexico Community College
# Course: CIS 1250 Python Programming I
# Instructor: Rob Garner
# Date: 25 November 2020 

# Program: P11 Geopoint Distance Calculator
# Purpose: Use a GUI to calculate the distance between user geopoints
#          and geopoints stored in a database.
# File: GeoPointLibrary.py

import sqlite3


class GeoPoint:
    # initialize class variables
    def __init__(self,lat=0,lon=0,desc='TBD'):
        self.lat = lat
        self.lon = lon
        self.desc = desc
        
    # Point methods & property
    def SetPoint(self,point):
        self.lat,self.lon = point
    def GetPoint(self):
        return (self.lat,self.lon)
    PointCoord = property(GetPoint,SetPoint)

    # Description methods & property
    def SetDescription(self,description):
        self.desc = description
    def GetDescription(self):
        return self.desc
    PointDesc = property(GetDescription,SetDescription)
    
    # Distance calculation method
    def GetDistance(self,userPoint):
        from math import sin,cos,sqrt,atan2,radians
        earthRadius = 6371
        # convert to radians
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(userPoint.lat)
        lon2 = radians(userPoint.lon)
        # calculate difference of lat&lon
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        # finish calculation
        varA = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        varC = 2 * atan2(sqrt(varA),sqrt(1-varA))
        distance = earthRadius * varC
        return distance

class GeoPointsList:
    def __init__(self):
        self.geo_points_list = []

    # Connect to db and read in points
    def SetPoints(self):
        conn = sqlite3.connect('GeoPointDB.db')
        curs = conn.cursor()
        sqlcmd = '''SELECT * FROM PointsTable;'''
        curs.execute(sqlcmd)
        points = curs.fetchall()
        # create class objects with table data
        for row in points:
            lat = row[0]
            lon = row[1]
            desc = row[2]
            geo_point_obj = GeoPoint(lat,lon,desc)
            self.geo_points_list.append(geo_point_obj)
        
        conn.commit()
        conn.close()        

    # Calculate distance/find and set values as closest
    def FindClosest(self,userPoint):
        closest_loc_dist = 10000
        for geo_point in self.geo_points_list:
            loc_dist = geo_point.GetDistance(userPoint)
            if loc_dist < closest_loc_dist:
                closest_loc_dist = loc_dist
                closest_loc_coord = geo_point.PointCoord
                closest_loc_desc = geo_point.PointDesc
        closest = 'You are closest to %s which is located at %s!'%(closest_loc_desc,
                                                                  closest_loc_coord)
        return closest
