import pendulum

TIME_ZONE: str = "Asia/Tokyo"
DATE_CHANGE_HOUR: int = 3


def use_pendulum() -> None:
    """pendulumを使った日付操作

    Returns:
        None

    """

    print("オブジェクト生成-------------------------------------")
    now = pendulum.now(TIME_ZONE)
    time = pendulum.datetime(2020, 1, 1, 12, 00, 00, tz=TIME_ZONE)
    print(time)
    print(time.date())
    print(time.time())
    print(time.year)
    print(time.month)
    print(time.hour)
    print(time.minute)
    print(time.second)
    print(time.microsecond)
    print(time.timezone)

    print("オブジェクト〜文字列の変換-------------------------------------")
    from_format = pendulum.parse("1975-05-21T22:00:00+09:00")  # 文字列からオブジェクト
    to_format = now.isoformat()  # オブジェクトから文字列
    print(from_format)
    print(to_format)

    from_format = pendulum.from_format(
        "1975/05/21 22:10:30", "YYYY/MM/DD HH:mm:SS", tz=TIME_ZONE
    )
    to_format = now.format("YYYYMMDDHHmmSS")
    print(from_format)
    print(to_format)

    print("加減算-------------------------------------")
    added_time = time.add(years=1, months=1, days=1, hours=1, minutes=1, seconds=1)
    subtracted_time = time.subtract(1, 1, 1, 1, 1, 1, 1)
    print(time)
    print(added_time)
    print(subtracted_time)

    print("Duration 期間-------------------------------------")
    dur = pendulum.duration(days=15)
    print(dur)
    print(dur.weeks)
    print(dur.days)
    print(dur.hours)
    print(dur.in_hours())

    print("Period 指定範囲期間-------------------------------------")
    start = pendulum.now(TIME_ZONE)
    end = start.add(weeks=2)
    period = end - start
    print(period)
    print(now.add(days=-1), now.add(days=-1) in period)
    print(now.add(days=2), now.add(days=2) in period)


def convert_date(datetime, change_date_hour):
    return (
        datetime.date()
        if datetime.hour >= change_date_hour
        else datetime.add(days=-1).date()
    )


use_pendulum()
