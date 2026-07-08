'''Russian Peasent Multiplication Algorithm  

Ethiopean Peasent multiplication Algorithm  


 num1        num2      product                         num1       num2       product
 173          77         0                              365       250         0 
  86         154        77                              182       500        250
  43         308        77                              91        1000       250
  21         616        385                             45        2000       1250
  10         1232       1001                            22        4000       3250
  5          2464       1001                            11        8000       3250
  2          4928       3465                            5         16000      11250
  1          9856       3465                            2         32000      27250
  0          ???/       13321                           1         64000      27250
                                                        0                    91250
''' 

def compute(n1,n2):   #n1 = 77    n2 = 35 
    product = 0               # product = 0 
    while n1 > 0:                # while 77 > 0 ?        while 38 > 0?        while 19>0?          while 9>0?
        if n1%2  != 0:              # if 77%2 != 0:          if 38%2 != 0?      if 19%2 != 0?        if 9%2 != 0?
            product = product + n2      # product = 0 + 35 (35)                   product=35+140( 175)  product=175+280(455)
        n1 = n1 // 2                # n1 = 77/2 (38)        n1 = 38//2 (19)     n1 = 19//2 (9)       n1=9//2 (4)
        n2 = n2 * 2                 # n2 = 35*2 (70)        n2 = 70*2 ( 140)    n2 = 140*2 (280)     n2 = 280*2 (560)
    return product 
                                    # while 4 > 0?            while 2 > 0?      while 1>0?                while 0 > 0?
                                       # if 4%2 != 0?           if 2%2 != 0       if 1%2 != 0?
                                                                                   # product = 455+2240(2695)
                                     # n1 = 4//2 (2)           n1 = 2/2 (1)       n1 = 1//2 (0)
                                     # n2 = 560*2 (1120)       n2 = 1120*2 (2240) n2 = 2240*2 (4480)

while True:
    num1, num2 = input("\n\tEnter any Two Integer Numbers e.g. 365  250  ").split()
    num1 = int(num1)
    num2 = int(num2)
    print("\n\tUsing Russian Peasent Multiplication ",num1, " * ", num2, " = ", compute(num1,num2))
    
