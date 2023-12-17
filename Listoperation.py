""" Lists
Consider a list ( list = [] ). You can perform the following commands:
1. insert i e : Insert integer at position .
2. print : Print the list.
3. remove e : Delete the first occurrence of integer .
4. append e : Insert integer at the end of the list.
5. sort : Sort the list.
6. pop : Pop the last element from the list.
7. reverse : Reverse the list.
Initialize your list and read in the value of followed by lines of commands where each command will
be of the types listed above. Iterate through each command in order and perform the corresponding
operation on your list.
Example
: Append to the list, .
: Append to the list, .
: Insert at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format
The first line contains an integer, , denoting the number of commands.
Each line of the subsequent lines contains one of the commands described above.
Constraints
The elements added to the list must be integers.
Output Format
2/2
For each command of type print , print the list on a new line.
Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]  """


#Solution

if __name__ == "__main__":
    N = int(input())
    final = []
    for i in range(N):
        command = input().split(" ")
        if command[0] == "append":
          final.append(int(command[1]))
        elif command[0] == "insert":
          final.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
          final.remove(int(command[1]))
        elif command[0] == "sort":
          final.sort()
        elif command[0] == "reverse":
          final.reverse()
        elif command[0] == "pop":
          final.pop()
        elif command[0] == "print":
          print(final)



