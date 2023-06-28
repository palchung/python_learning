time_swimming = int(
    input("What is the completing time of swimming ? (in minutes) "))
time_running = int(
    input("What is the completing time of running ? (in minutes) "))
time_cycing = int(
    input("What is the completing time of cycing ? (in minutes) "))

total_time = time_swimming + time_running + time_cycing
print("The total completing time of triathlon is : ", total_time)

award = "No award"
if total_time <= 100:
    award = "Provincial Colours"

if total_time <= 105 and total_time > 100:
    award = "Provincial Half Colours"

if total_time <= 110 and total_time > 105:
    award = "Provincial Scroll"

print("Award for this player is", award)
