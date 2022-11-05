data_tri = [] # Declare a list to store the data
left = 0    # Buffer variables to evaluate left and right nodes
right = 0

input_file = input('Please input the name/directory of the data file (the file must be space delimited): ')
with open(input_file, 'r') as data_file:    # Read data and store in data_tri as 2-d list
    for line in data_file:                  
        data_tri.append(line.removesuffix('\n').split(' '))
    
    tri_len = len(data_tri)
    data_file.close()       # Close file

    for x, row in enumerate(data_tri):  
        for y, node in enumerate(row):      # Change all values of list into integer
            data_tri[x][y] = int(node)

    for index, row in enumerate(data_tri[len(data_tri)-2::-1]): # Iterate through list from the second to last row back up to the root
        for i, node in enumerate(row):                          # Iterate through every node
            left = node + data_tri[tri_len-(index+1)][i]             # Compute the hypothetical sum if left (right) path is taken
            right = node + data_tri[tri_len-(index+1)][i+1]          # Compute the hypothetical sum if right (left) path is taken
            data_tri[tri_len-(index+2)][i] = max([left, right])  # The current node is replacee by the maximum value out of the two values computed above

print(data_tri[0][0])       # Print the root, which now has the maximum possible sum