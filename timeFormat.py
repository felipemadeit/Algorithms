def timeConversion (normal_hour: str):
    
    
    #12:00 pm
    
    hour = normal_hour[:2]
    minutes = normal_hour[3:5]
    seconds = normal_hour[6:8]
    zone = normal_hour[8:]
    
    new_hour = 0
    
    if zone == 'PM':
        if int(hour) == 12:
            print(f"{hour}:{minutes}:{seconds}")
        elif int(hour[1:])< 10:
            new_hour += 12 + int(hour)
            print(f"{new_hour}:{minutes}:{seconds}")
        elif int(hour) >= 10:
            new_hour += 12 + int(hour)
            print(f"{new_hour}:{minutes}:{seconds}")
    else:
        if int(hour) == 12:
            new_hour = 0
            print(f"0{new_hour}:{minutes}:{seconds}")
        else:
            print(f"0{hour}:{minutes}:{seconds}")
    

    
            
    
    
timeConversion(input())