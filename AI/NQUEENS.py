def check(board, column, row, n):
    r = row - 1
    c = column - 1
    # Check upper-left diagonal
    while(r >= 0 and c >= 0):
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    r = row + 1
    c = column - 1
    # Check lower-left diagonal
    while(r < n and c >= 0):
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1

    c = column - 1
    r = row
    # Check the row to the left
    while(c >= 0):
        if board[r][c] == 'Q':
            return False
        c -= 1
    
    return True
    
def solve(board, column, n, ans):
    if column == n:
        # Found a valid solution, save a copy
        ans.append(["".join(row) for row in board])
        return
    
    for row in range(n):
        board[row][column] = 'Q'
        if check(board, column, row, n):
            solve(board, column + 1, n, ans)
        # Backtrack
        board[row][column] = '.'
            
def main():
    """
    Main function with a minimal menu.
    """
    while True:
        print("\n1. Solve N-Queens\n2. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            try:
                n = int(input("Enter N: "))
                if n <= 0:
                    print("Invalid N.")
                    continue

                board = [['.' for i in range(n)] for _ in range(n)]
                ans = []
                
                solve(board, 0, n, ans)
                
                print(f"Found {len(ans)} solutions:")
                print(ans) # Prints the raw list of solutions
                        
            except ValueError:
                print("Invalid input.")
                
        elif choice == '2':
            print("Exiting.")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()