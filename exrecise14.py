"""
Strive is a new developer-centric service that is focused on presenting software developers with jobs that excite us. Strive discovers these jobs for developers based on a number of factors.

One of the simplest, yet most important factors is compensation. As developers we know how much money we need to support our lifestyle, so we generally have a rough idea of the minimum salary we would be satisfied with.

Let's give this a try. We'll create a function match which takes a candidate and a job, which will either return a boolean indicating whether the job is a valid match for the candidate.
"""
def match(candidate, job):
    if candidate == {} or job == {}:
        raise "error"
    else:
        if candidate['min_salary'] <= (job['max_salary'] + candidate['min_salary'] * 0.10):
            return True
        else:
            return False






candidate1 = {'min_salary': 120000}
candidate2 = {'min_salary': 190000}
job1 = {'max_salary': 130000}
job2 = {'max_salary': 80000}
job3 = {'max_salary': 171000}

print(match(candidate2, job3))
