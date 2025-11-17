import random
def standard_chaining(N:int, T:int, n:int) -> list[list[int]]:
    """Randomly inserts n keys from the universe {0, N-1} into a hashmap of size T and returns the largest chain""" 
    M = [[] for _ in range(T)]
    K = random.sample(range(N), n)
    for k in K:
        spot = k % T
        M[spot].append(k)
    return M

def two_choices_chaining(N:int, T:int, n:int, p:int=2027) ->int:
    """Randomly inserts n keys from the universe {0, N-1} into a hashmap of size T and returns the largest chain,
    using 2 different hash functions and inserting into the short chain"""
    M = [[] for _ in range(T)]
    K = random.sample(range(N), n)
    for k in K:
        spot1 = k % T
        spot2 = (p*k) % T
        M[min(len(M[spot1]), len(M[spot2]))].append(k)
    return M

def get_max_length_chain(M:list[list[int]]):
    m = 0
    for i in range(len(M)):
        m = max(m, len(M[i]))
    return m

def run_evaluation(fun, N:int, T:int, n:int, experiments:int=100) -> list[int]:
    res = []
    for _ in range(experiments):
        M = fun(N=N, T=T, n=n)
        max_length = get_max_length_chain(M=M)
        res.append(max_length)

    return res

def run_evaluation_suite() -> tuple[list[list[int]]]:
    standard_res = []
    two_choice_res = []

    N = 10_000
    T = 1_000
    standard_res.append(run_evaluation(fun=standard_chaining, N=N, T=T, n=100))
    two_choice_res.append(run_evaluation(fun=two_choices_chaining, N=N, T=T, n=100))

    standard_res.append(run_evaluation(fun=standard_chaining, N=N, T=T, n=500))
    two_choice_res.append(run_evaluation(fun=two_choices_chaining, N=N, T=T, n=500))

    standard_res.append(run_evaluation(fun=standard_chaining, N=N, T=T, n=1000))
    two_choice_res.append(run_evaluation(fun=two_choices_chaining, N=N, T=T, n=1000))

    return (standard_res, two_choice_res)

def print_res(l:list)->None:
    for li in l:
        print(li)
        print()
    print("--------")

if __name__ == "__main__":
    standard_res, two_choice_res = run_evaluation_suite()

    print_res(standard_res)
    print_res(two_choice_res)
    
    