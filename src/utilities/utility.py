class objectutils: 
  def __init__(self):
    pass

  def add(self,a=0,b=0):
    return a+b

  def sub(self,a=0,b=0):
    try:
      assert a > b
    except AssertionError as ae:
      print('Handling run-time error:', ae)
    else:
      c = a-b
      return c

