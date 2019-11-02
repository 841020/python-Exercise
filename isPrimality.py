def isPrimality(args, root):
  for i in range(2, a+1):
    if not num%i:
      return 'this num is not primality'
  print('this is primality')

num = input()
root = int(num**(0.5))
isPrimality(num, root)

# fermat's little theorem
def fermat(args):
  for i in args:
    if (i**args)%args != i:
      return 'this num is not primality'
    print('this is primality')
num = input()
fermat(nums)

from random import sample
# fermat's little theorem
def fermat(args):
    for i in sample(range(2, args),3):
        if (i**args)%args != i:
            print('this is not Primality')
isPrimal(int(input('input')))
