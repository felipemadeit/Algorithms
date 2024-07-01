def timeConversion (normal_hour: str):
    
    
    #12:00 pm
    
    hour = normal_hour[:2]
    minutes = normal_hour[3:5]
    seconds = normal_hour[6:8]
    zone = normal_hour[8:]
    
    new_hour = 0
    
    
    if zone == 'AM':
           if int(hour) == 12:
               print(f"00:{minutes}:{seconds}")
           else:
               print(f"{hour}:{minutes}:{seconds}")
    else:
        if hour != '12':
            if hour[0] == '0':
                print(f"{12+int(hour[1])}:{minutes}:{seconds}")
            else:
                print(f"{12+int(hour)}:{minutes}:{seconds}")
        else:
            print(f"{hour}:{minutes}:{seconds}")

    
            
    
    
timeConversion(input())