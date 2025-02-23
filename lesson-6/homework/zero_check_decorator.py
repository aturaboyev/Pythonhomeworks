def check(func):
  def wrapper(*args, **wargs):
    a, b = args
    try:
      return a / b
    except ZeroDivisionError:
      return "Cant divide to zero"
  return wrapper      

# @check
def div(a, b):
  return a / b

div = check(div)

print(div(6, 2))

