#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def th(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    th(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    th(n-1, auxiliary, source, destination)
n = 3  
th(n, 'A', 'B', 'C')
