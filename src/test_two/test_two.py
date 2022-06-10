"""
Write a function that takes as arguments two arrays of integers. 
Your function needs to determine whether the second array is contained in the first one, returning true or false;
"""

def contains_second_array(array_one, array_two):
        # Write your code here

    """
    This code was made in three parts.
    The firs part we check if the size of array_one is smaller than array_two or the array_two is bigger than array_one,
    if it is smaller or bigger return False.
    The second part we used the quicksort algorithm to sort the arrays,avoiding the n*m complexity.
    The third part we started to compare the initial elements, which would give us in the worst case an n+m complexity. 
    """

    # Part one
    if len(array_one) < len(array_two) or len(array_two) > len(array_one):
        return False
    
    # Part two     
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

    new_array_one = quicksort(array_one)
    new_array_two = quicksort(array_two)


    # Part three
    i , j = 0,0

    while i < len(new_array_two) and j < len(new_array_one):
        if new_array_one[j] < new_array_two[i]:
            j += 1
        elif new_array_one[j] == new_array_two[i]:
            j += 1
            i += 1
        else:
            return False


    return False if i < len(array_two) else True


if __name__=="__main__":

        array_one = [5, 1, 22, 25, 6, -1, 8, 10]
        array_two = [1, 6, 0, 10]

        print(contains_second_array(array_one, array_two))