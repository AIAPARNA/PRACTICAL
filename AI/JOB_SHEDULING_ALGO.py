# --- THIS IS THE FUNCTION YOU PROVIDED (UNCHANGED) ---

def schedule_jobs(jobs): 
    """
    Schedules jobs to maximize profit based on deadlines.
    Jobs are given as a list of tuples: (Job_ID, Deadline, Profit)
    """
    
    # 1. Sort jobs in decreasing order of profit
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    if not sorted_jobs: 
        return [], 0 
    
    # 2. Find the maximum deadline to create the time slots array
    max_deadline = 0 
    for job in sorted_jobs: 
        if job[1] > max_deadline: 
            max_deadline = job[1]
            
    # 3. Initialize slots. -1 indicates a free slot.
    # We use max_deadline slots, indexed 0 to max_deadline-1
    slots = [-1] * max_deadline 
    
    total_profit = 0 
    
    # 4. Iterate through sorted jobs
    for job in sorted_jobs: 
        job_id, deadline, profit = job 
        
        # 5. Find a free slot for this job (from its deadline backwards)
        # We start from deadline-1 because slots are 0-indexed
        for i in range(deadline - 1, -1, -1): 
            if slots[i] == -1: 
                # Found a free slot
                slots[i] = job_id 
                total_profit += profit 
                break # Move to the next job
    
    # 6. Create the final sequence from the slots array
    # This filters out any -1 (empty) slots
    final_sequence = [job_id for job_id in slots if job_id != -1]
    
    return final_sequence, total_profit

# --- NEW MENU-DRIVEN PART ---

jobs_list = []  # Start with an empty list of jobs

while True:
    print("\n--- Job Scheduling Menu ---")
    print("  1. Add a Job")
    print("  2. View Current Jobs")
    print("  3. Run Job Scheduler")
    print("  4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Add a Job
        try:
            job_id = input("  Enter Job ID (e.g., 'J1', 'A', etc.): ")
            deadline = int(input("  Enter Job Deadline (a positive number): "))
            profit = int(input("  Enter Job Profit (a number): "))
            
            if deadline <= 0 or profit < 0:
                print("Error: Deadline must be positive and profit cannot be negative.")
            else:
                new_job = (job_id, deadline, profit)
                jobs_list.append(new_job)
                print(f"==> Job {new_job} added.")
                
        except ValueError:
            print("Error: Deadline and Profit must be valid numbers.")

    elif choice == '2':
        # View Current Jobs
        if not jobs_list:
            print("==> No jobs added yet.")
        else:
            print("\n--- Current Jobs (ID, Deadline, Profit) ---")
            for job in jobs_list:
                print(f"  {job}")

    elif choice == '3':
        # Run Job Scheduler
        if not jobs_list:
            print("Error: No jobs to schedule. Please add jobs first (Option 1).")
        else:
            # We pass a copy of the list so the original isn't modified
            sequence, profit = schedule_jobs(list(jobs_list))
            
            print("\n--- Job Scheduling Result ---")
            print(f"  Original Jobs: {jobs_list}")
            print(f"  Optimal Job Sequence: {sequence}")
            print(f"  Maximum Total Profit: {profit}")

    elif choice == '4':
        # Exit
        print("Goodbye!")
        break

    else:
        print("Error: Invalid choice. Please pick 1, 2, 3, or 4.")