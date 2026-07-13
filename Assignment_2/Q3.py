
# Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet:"))
inches = int(input("Enter inches:"))
total_inches = (feet * 12) + inches
total_meters = total_inches * 0.0254
meters = int(total_meters)
centimeters = (total_meters - meters) * 100
print("Distance in meters:",meters)
print("Distance in centimeters:",centimeters)

                