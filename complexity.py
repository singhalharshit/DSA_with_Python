"""
Time Complexity - It tells us how the number of operations (or steps) in a program increases as the input size grows.

It does not measure the actual time taken in seconds, because that depends on your computer's speed.
Instead, it looks at how much more work the code has to do when you give it more data.

It is usually described using Big-O notation -> O() 
"""


"""
    Rules of TIME COMPLEXITY - 
    1 - Always calculate the time complexity in terms of worst case (There are 3 cases in total Best Case, Average Case, Worst Case)
    2 - Avoid Constant Values
    3 - Avoid Lower Bound
"""

# Examples

for i in range(5):
    print("Harshit")


"""
    Now we see that loop runs for 5 times and prints a string as soon as it breaches the loop limit the loop breaks. 

    So into this loop 3 operations are being performed which are checking the index, checking the value of i and then printing of the string and into this case since  our input size is 5 (loop runs for 5 times which is our input size) so total operations become 3*5 = 15 so our time complexity becomes O(3n) and now as per rule we dont want constant so our time complexity is O(n)
"""


# Space Complexity

"""
    Space Complexity - Auxiliary space + input space -> 
    Auxiliary space -> The extra space used to solve the problem
    Input Space -> TThe space used to store the input

    Example -> Tell the sum of x=5,y=10,z=15
    total = x+y+z
    print(total)
    so here x,y,z are the input space and total is the aux space

    ** Do not change the input unless asked
"""