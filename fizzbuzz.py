def fizzbuzz(arg): 
    if(arg % 3 == 0 and arg % 5 == 0):
        print('fizbuzz',arg)
    elif(arg % 3 == 0):
        print('fizz',arg)
    elif(arg % 5 == 0):
        print('buzz',arg)
   


random_numbers = [8633,1285,1644,8713,1096,3542,3702,7326,5927,1500,4087,3349,5769,4522,6468]
for num in random_numbers:
    fizzbuzz(num)