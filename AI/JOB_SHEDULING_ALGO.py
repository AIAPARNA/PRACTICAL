def schedule_jobs(jobs): 
    sorted_jobs = sorted(jobs, key = lambda x : x[2], reverse = True)
    
    if not sorted_jobs: 
        return [] , 0 
    
    max_deadline = 0 
    for job in sorted_jobs: 
        if job[1] > max_deadline: 
            max_deadline = job[1]
            
    slots = [-1] * max_deadline 
    
    total_profit = 0 
    scheduled_jobs_id = [] 
    for job in sorted_jobs: 
        job_id, deadline, profit = job 
        
        for i in range(deadline - 1, -1, -1): 
            if slots[i] == -1: 
                total_profit += profit 
                slots[i] = job_id 
                scheduled_jobs_id.append(job_id)
                break
    
    final_sequence = [job_id for job_id in slots if job_id != -1]
    
    return final_sequence, total_profit

jobs_list = [('J1', 4, 70),
             ('J2', 2, 60),
             ('J3', 1, 40),
             ('J4', 3, 100),
             ('J5', 4, 50)]

print("Original jobs (ID, Deadline, Profit):")
print(jobs_list)

sequence, profit = schedule_jobs(jobs_list)

print("\n--- Job Scheduling Result ---")
print(f"Optimal Job Sequence: {sequence}")
print(f"Maximum Total Profit: {profit}")