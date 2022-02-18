#miles_distance = 7425
#miles_per_hour = 55

miles_distance = input("How much distance to reach your destination: ")
miles_per_hour = input("How much miles per hour can the plan achieve?: ")
x = int(miles_distance) / int(miles_per_hour)

print("the total flight time is: " + str(x) + " hours!")
