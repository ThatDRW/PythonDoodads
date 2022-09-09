def fizzbuzz(amount:int=0):
    if amount <= 0: print('Very funny! Please enter a positive integer.')

    for i in range(1,amount+1):
        if i % 15 == 0: print('FizzBuzz')
        elif i % 5 == 0: print('Buzz')
        elif i % 3 == 0: print('Fizz')
        else: print(i)

if __name__ == '__main__':
    amount = input('How many Fizzes do we Buzz? : ')
    fizzbuzz(int(amount))