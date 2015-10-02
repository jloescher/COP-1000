#### slicing1.py

def main():

    nums = [12,10,8,15,3,11]    ### a list of integers

    print(nums)         ### not a slice, entire list

    print(nums[2])      ### not a slice, 1 element
    
    print(nums[0:2])

    print(nums[2:5])

    print(nums[2:])

    print(nums[:-3])

    print(nums[2:-2])

    print('Loop 1 -------------------------------')
    for n in range(6):
        print(nums[n:])

    print('Loop 2 -------------------------------')
    for n in range(6):
        print(nums[:n])

    print('Loop 3 -------------------------------')
    for n in range(6):
        print(nums[-n:])

    print('Loop 4 -------------------------------')
    for n in range(6):
        print(nums[:-n])        

main()
