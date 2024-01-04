import random

def evaluate_max_load(assignment, M):
    max_load = 0
    reviewer_load = [0] * M
    for paper in assignment:
        for reviewer in paper:
            reviewer_load[reviewer - 1] += 1
            if reviewer_load[reviewer - 1] > max_load:
                max_load = reviewer_load[reviewer - 1]
    return max_load

def initial_solution(N, M, b, papers):
    assignment = []
    for i in range(N):
        reviewers = random.sample(papers[i], b)
        assignment.append(reviewers)
    return assignment

def local_search(N, M, b, papers):
    current_assignment = initial_solution(N, M, b, papers)
    current_max_load = evaluate_max_load(current_assignment, M)
    
    iterations_without_improvement = 0
    max_iterations_without_improvement = 1000
    
    while iterations_without_improvement < max_iterations_without_improvement:

        paper1 = random.randint(0, N - 1)
        paper2 = random.randint(0, N - 1)
        reviewer1 = random.choice(current_assignment[paper1])
        reviewer2 = random.choice(current_assignment[paper2])
        
        current_assignment[paper1].remove(reviewer1)
        current_assignment[paper1].append(reviewer2)
        
        current_assignment[paper2].remove(reviewer2)
        current_assignment[paper2].append(reviewer1)
        
        new_max_load = evaluate_max_load(current_assignment, M)
        
        if new_max_load < current_max_load:
            current_max_load = new_max_load
            iterations_without_improvement = 0
        else:
            # Revert the change if it doesn't improve the solution
            current_assignment[paper1].remove(reviewer2)
            current_assignment[paper1].append(reviewer1)
            current_assignment[paper2].remove(reviewer1)
            current_assignment[paper2].append(reviewer2)
            iterations_without_improvement += 1
            
    return current_assignment

# main
N, M, b = map(int, input().split())
papers = []
for _ in range(N):
    k, *reviewers = map(int, input().split())
    papers.append(reviewers)

assignment = local_search(N, M, b, papers)

print(N)
for paper in assignment:
    print(b, *paper)
