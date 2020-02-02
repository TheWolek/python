def __init__():
    print(__name__,'init')

__name__ = '[mod2]'
def func(nums):
    output = []
    for num in nums:
        output.append(num**2)
    return output