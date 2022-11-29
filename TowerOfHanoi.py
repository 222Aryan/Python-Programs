#Recursive Python Function to solve the Tower of Hanaoi


def tower_of_hanoi(n , source, destination, auxillary):
    if n == 1:
        print("Move disk 1 from source", source,"to destination",destination)

        return
    tower_of_hanoi(n-1, source, auxillary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    
    tower_of_hanoi(n-1, auxillary, destination, source)

#Driver code
n = 3
tower_of_hanoi(n,'A','B','C') 
# A, B, C are the name of rods

