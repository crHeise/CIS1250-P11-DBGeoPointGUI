# Programmer: Chris Heise (crheise@icloud.com)
# School: Central New Mexico Community College
# Course: CIS 1250 Python Programming I
# Instructor: Rob Garner
# Date: 25 November 2020 

# Program: P11 Geopoint Distance Calculator
# Purpose: Use a GUI to calculate the distance between user geopoints
#          and geopoints stored in a database.
# File: DBInit.py
# *Run this once to initialize a database to use.

import sqlite3


# open/create database
conn = sqlite3.connect('GeoPointDB.db')

curs = conn.cursor()

# create table in database if it doesn't already exist
try:
    sqlcmd = '''
        CREATE TABLE PointsTable(
            Latitude FLOAT,
            Longitude FLOAT,
            Description TEXT
            )'''
    curs.execute(sqlcmd)

    # add data to the table
    points = [(40.7128, 70.0060, 'New York City, NY'),
              (37.7749, 122.4194, 'San Francisco, CA'),
              (21.3069, 157.8583, 'Honolulu, HI'),
              (58.3019, 134.4197, 'Juneau, AK'),
              (24.5551, 81.7800, 'Key West, FL')]
    for row in points:
        sqlcmd = '''
                    INSERT INTO PointsTable
                    VALUES (?, ?, ?);'''
        curs.execute(sqlcmd,row)
    # commit changes
    conn.commit()

except sqlite3.OperationalError as e:
    print('Database message: ',e)
finally:
    conn.close()
