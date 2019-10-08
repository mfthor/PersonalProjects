import random

box_num = random.randint(1,12)

class Box:

  def __init__(self, num):
        self.num = num
  
  marb_count = 0
  flag = False


def make_box(num):

  box = Box(num)

  return box

def trial(i):
  box_list = []
  flag = True
  count = 0
  for x in range(1,i+1):
    box = make_box(x)
    box_list.append(box)

  while flag == True:

    print('Turn {0}'.format(count))

    assign = random.randint(1,12)

    for x in box_list:

      if x.num == assign:
        x.marb_count += 1

        if x.marb_count > 1:
          x.flag == True
          print('Box Filled: {0} | Marble Count: {1}'. format(x.num,x.marb_count))

    left = [x for x in box_list if x.marb_count < 2]
    print('Boxes Left: {0}'.format(len(left)))

    if not left:
      flag = False
      print("Trial Completed")
    
    count += 1
  
  return count
  

def multi_trial(i):

 sum = 0
 for x in range(1,i):
  print('Trial {0}'.format(x))
  result = trial(12)
  sum += result


 average = sum / i

 print('Average Turns Required: {0}'. format(average))

multi_trial(10000)