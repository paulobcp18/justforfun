import calendar

print('What year?')

yy = int(input()) # colocar o ano

print('And the month?')
mm = int(input()) # colocar o mês

print(calendar.month(yy, mm))