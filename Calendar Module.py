(lambda a,calendar:print([*calendar.day_name][calendar.weekday(a[-1],a[0],a[1])].upper()))([*map(int,input().split())],__import__("calendar"))