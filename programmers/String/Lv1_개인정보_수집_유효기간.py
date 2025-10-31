def format_date(date, m):
    year, month, day = map(int, date.split('.')) # 년, 월, 일
    total = year * 12 * 28 + (month - 1) * 28 + day + m * 28
    new_year = total // (12 * 28)
    total %= (12 * 28)
    new_month = total // 28 + 1
    new_day = total % 28
    if new_day == 0:
        new_day = 28
        new_month -= 1
        if new_month == 0:
            new_month = 12
            new_year -= 1
    return f"{new_year:04d}.{new_month:02d}.{new_day:02d}"

# 오늘 날짜와 비교하여 유효기간이 지났는지 확인
def is_stale(today, date):
    date = list(map(int, date.split('.')))
    today = list(map(int, today.split('.')))
    num_date = date[0] * 12 * 28 + date[1] * 28 + date[2]
    num_today = today[0] * 12 * 28 + today[1] * 28 + today[2]
    return num_date <= num_today


def solution(today, terms, privacies):
    answer = []
    arr = {}

    for term in terms:
        char, t = term.split()
        arr[char] = int(t)

    for idx, privacy in enumerate(privacies):
        date, char = privacy.split()
        new_date = format_date(date, arr[char])

        if is_stale(today, new_date):
            answer.append(idx + 1)

    return answer
