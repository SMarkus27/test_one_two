""" 
Write a function that takes as arguments: an array of distinct integers and an integer (target value). 
You need to check if any two numbers of the array sum up to the target value. 
If that's the case, your function should return those two numbers in array fashion. Otherwise, just return an empty array.
"""


def two_sum(array, target):
    # Write your code here

    """
    This code was made in two parts.
    The first part we used the quicksort algorithm to sort the array,avoiding the n*n complexity.
    The second part we begin sum the extreme elements,and following to the middle. 
    """
    # Part one
    def quicksort(array):
        if len(array) <= 1:
            return array
        less_than_pivot = []
        greater_than_pivot = []
        pivot = array[0]
        for value in array[1:]:
            if value <= pivot:
                less_than_pivot.append(value)
            else:
                greater_than_pivot.append(value)
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
    # Part two
    new_array = quicksort(array)

    initial = 0
    final = len(new_array)-1
    while initial < final:
        result_sum = new_array[initial]+new_array[final]
        if result_sum == target:
            return [new_array[initial],new_array[final]]
        elif result_sum < target:
            initial +=1
        else:
            final-=1
    return[]



if __name__=="__main__":
        array_one = [3, 5, 4, 8, 11, 1, -1, 6]
        target = 10

        print(two_sum(array_one,target))