def add_time(start, duration, day=''):
    finalMinutes = 0
    finalHours = 0
    dayCounter = 0
    day = day.lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
  #SPLIT START INPUT
    splitTime = start.split()
    splitHoursMinutes = splitTime[0].split(':')
    startHours = int(splitHoursMinutes[0])
    startMinutes = int(splitHoursMinutes[1])
    label = splitTime[1]

  #SPLIT DURATION INPUT
    durationHours = int(duration.split(':')[0])
    durationMinutes = int(duration.split(':')[1])

    if startMinutes + durationMinutes >= 60:
      finalMinutes = (startMinutes + durationMinutes) % 60
      startHours = startHours + 1
    else:
      finalMinutes = (startMinutes + durationMinutes)

    finalHours = startHours + durationHours

    if finalHours >= 12:
      if label == 'PM':
        dayCounter += 1
      numberOfHalfDays = (startHours + durationHours) // 12
      if numberOfHalfDays % 2 != 0:
        if label == 'PM':
          label = 'AM'
        else:
          label = 'PM'
      finalHours = (startHours + durationHours) % 12
      dayCounter = dayCounter + (startHours + durationHours) // 24
      
    if finalHours == 0:
      finalHours = 12
      
    if len(str(finalMinutes)) == 1:
      finalMinutes =  "0" + str(finalMinutes)
      
    if day != "":
      day = days.index(day)
      day = (day + dayCounter) % 7

    # CREATE STRING TO BE RETURNED
    new_time = f'{finalHours}:{finalMinutes} {label}'
    if day != '':
      new_time += f', {days[day].capitalize()}'
    if dayCounter == 0:
      dayCounter =''
    elif dayCounter == 1:
      new_time +=f' (next day)'
    else:
      new_time +=f' ({dayCounter} days later)'
    

    return new_time


