You are given matchsticks of different size in a row, find out a way you can make one square by using up all those matchsticks. 
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Your output will either be true or false, to represent whether you could make one square using all the matchsticks in the row.

Input description:
First line contains, N the size of the row.
Second line contains, N elements of matchsticks length.

Output Description:
Print True or False.

Sample Input:
5
1 1 2 2 2

Sample Output:
True

Explanations:
1+1=2, which is one side and 2,2,2 are rest three sides. so the output is True.

Sample Input:
4
3 3 3 3

Sample Output:
True

Sample Input:
6
2 4 3 1 6 5

Sample Output:
False

Sample Input:
3
2 2 1

Sample Output:
False

Sample Input:
4
7 7 7 8

Sample Output:
False

Sample Input:
8
1 6 2 3 3 3 6

Sample Output:
True
