"""
Utility for rapidly inputting Robo-Magellan course coordinates,
generating a CSV file, and and loading it onto an SD card to
slot into the robot.
"""

from pprint import pprint
import csv

COURSE_FN = "course.csv"

rows = []
while True:
    print("Enter the type of waypoint.")
    print("S\tStart point")
    print("E\tEnd point")
    print("1...9\tMandatory cone")
    print("O\tOptional bonus cone")
    print("B\tCourse boundary")
    print("Q\tQuit")
    user_input = input("> ").upper()
    if user_input in "SE123456789OB":
        print("Latitude pole (N or S)")
        latitude_pole = input("> ").upper()
        print("Latitude degrees (integer)")
        latitude_degrees = int(input("> "))
        print("Latitude minutes (decimal)")
        latitude_minutes = float(input("> "))

        print("Longitude pole (E or W)")
        longitude_pole = input("> ").upper()
        print("Longitude degrees (integer)")
        longitude_degrees = int(input("> "))
        print("Longitude minutes (decimal)")
        longitude_minutes = float(input("> "))

        print("Comment (optional)")
        comment = input("> ")
        row = [user_input, latitude_pole, latitude_degrees, latitude_minutes, longitude_pole, longitude_degrees, longitude_minutes, comment]
        rows.append(row)
    elif user_input == "Q":
        pprint(rows)
        with open(COURSE_FN, "w") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"Course data written to {COURSE_FN}.")
        break

print("Done!")
