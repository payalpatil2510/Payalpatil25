
#Convert the time entered in hh,min and sec into seconds.

hh = int(input("Enter hours:"))
min = int(input("Enter minutes:"))
sec = int(input("Enter seconds:"))
total_seconds = (hh * 3600) + (min * 60) + sec
print("Total time in seconds:", total_seconds)