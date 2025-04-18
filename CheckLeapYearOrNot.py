year = int(input("Enter a year: "))

DaysInYear = 365

ExtraHoursPerYear = 24
ExtraMinutesPerYear = 48
ExtraSecondsPerYear = 47.5

TotalExtraHours = ExtraHoursPerYear * 4
TotalExtraMinutes = ExtraMinutesPerYear * 4
TotalExtraSeconds = ExtraSecondsPerYear * 4

ExtraHoursToDays = TotalExtraHours // 24
ExtraMinutesToDays = TotalExtraMinutes // (24*60)
ExtraSecondsToDays = TotalExtraSeconds // (24*60*60)

TotalExtraDays = ExtraHoursToDays + ExtraMinutesToDays + ExtraSecondsToDays


if year > 0:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print("Invalid year")