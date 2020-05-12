listA = [24, 56, 89, 0, 15, -4, 25, -8, 125, -98]

def small_num(numbers):

  smallest_num = numbers[0]

  for num in numbers:
    if num < smallest_num:
      smallest_num = num

  return(smallest_num)

print(small_num(listA))


