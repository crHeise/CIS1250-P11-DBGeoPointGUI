# Programmer: Chris Heise (crheise@icloud.com)
# School: Central New Mexico Community College
# Course: CIS 1250 Python Programming I
# Instructor: Rob Garner
# Date: 25 November 2020 

# Program: P11 Geopoint Distance Calculator
# Purpose: Use a GUI to calculate the distance between user geopoints
#          and geopoints stored in a database.
# File: GUI.py

from GeoPointLibrary import GeoPoint
from GeoPointLibrary import GeoPointsList
import wx


###---Event---###
def calculate(event):

    try:
    
        # get points from database
        geo_points_list = GeoPointsList()
        geo_points_list.SetPoints()

        # get user point
        userLat = float(user_lat_text.GetValue())
        userLon = float(user_lon_text.GetValue())
        userPoint = GeoPoint(userLat,userLon,'User Location')

        # calculate closest from list
        results_text.SetValue(geo_points_list.FindClosest(userPoint))

    except TypeError:
        results_text.SetValue('Wrong type of input!')
    except ValueError:
        results_text.SetValue('That wasn\'t a number!')
    except FileNotFoundError:
        results_text.SetValue('Couldn\'t find that file!')
    except Exception as e:
        results_text.SetValue('Something went wrong: ',e)
    

###---GUI---###
app = wx.App()

# Window
win = wx.Frame(None,title='Distance Calculator 3000',size=(420,395))

# User latitude text box
user_lat_label = wx.StaticText(win,pos=(5,5),size=(210,25),
                               label ='Your Latitude:')
user_lat_text = wx.TextCtrl(win,pos=(5,25),size=(110,25))

# User longitude text box
user_lon_label = wx.StaticText(win,pos=(140,5),size=(210,25),
                                label='Your Longitude:')
user_lon_text = wx.TextCtrl(win,pos=(140,25),size=(110,25))

# Button
calculate_button = wx.Button(win,label='Calculate!',
                             pos=(300,25),size=(90,25))
calculate_button.Bind(wx.EVT_BUTTON,calculate)

# Results text box
results_label = wx.StaticText(win,pos=(5,70),size=(210,25),label="Results:")
results_text = wx.TextCtrl(win,pos=(5,100),size=(390,200),
                           style=wx.TE_MULTILINE|wx.HSCROLL)


win.Show()
app.MainLoop()
