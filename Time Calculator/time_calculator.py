def add_time(start, duration, day=""):
  days0 = 0
  start_time = start.split()
  iso_start = start_time[0].split(":")
  start_h, start_m = iso_start
  f_clock = start.split()[1]
  duration_h, duration_m = duration.split(":")
  week_days = [
      "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
      "Saturday"
  ]
  sum_hour = 0
  act_min = int(start_m) + int(duration_m)
  if act_min > 60:
    sum_hour += act_min // 60
    act_min = act_min % 60

  act_hour = int(start_h) + int(duration_h) + sum_hour
  if act_hour >= 12:
    if f_clock == "AM" and (act_hour // 12) % 2 == 1:
      f_clock = "PM"
    else:
      f_clock = "AM"

  if f_clock == "AM":
    if (act_hour // 12) == 2:
      days0 = (act_hour // 24)
    elif (act_hour // 12) == 1 or (act_hour // 12) > 2:
      days0 = (act_hour // 24) + 1

  act_hour = act_hour % 12
  if act_hour == 0:
    act_hour = 12

  if day:
    day_index = week_days.index(day.capitalize())
    day_index += days0 % 7
    act_day = week_days[day_index % 7]
  else:
    act_day = ""

  if len(str(act_min)) == 1:
    act_min = "0" + str(act_min)

  new_time = str(act_hour) + ":" + str(act_min) + " " + f_clock

  if act_day:
    new_time += ", " + act_day

  if days0 == 1:
    new_time += " (next day)"
  elif days0 > 1:
    new_time += f" ({days0} days later)"

  return new_time
