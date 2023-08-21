def convert_12hr_to_24hr(hour, minute, period):
    if hour not in range (1, 13):
        raise ValueError ("not in range between 1 and 12")
    if minute not in range(60):
        raise ValueError ("minutes are not in range")

    if period == "pm" and hour!= 12:
        hour+= 12

    elif period =="am" and hour ==12 :
        hour = 0   


    return f"{hour:02d}{minute:02d}"