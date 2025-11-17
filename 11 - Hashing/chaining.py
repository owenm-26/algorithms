import random
import matplotlib.pyplot as plt

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
        if len(M[spot1]) < len(M[spot2]):
            M[spot1].append(k)
        else:
            M[spot2].append(k)
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

def plot_max_distribution(vals:list, title:str):
    # Determine the range of integers for bins
    min_val, max_val = min(vals), max(vals)
    bins = range(min_val, max_val + 2)  # +2 to include max value
    
    plt.hist(vals, bins=bins, alpha=0.7, edgecolor='black')
    plt.xticks(range(min_val, max_val + 1))  # Show integer ticks
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    # Save before showing
    plt.savefig(f"{title}.png")
    plt.show()

import numpy as np

def plot_all_distributions(results, vals, method_name):
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))  # 2 rows, 3 columns
    
    for i, ax in enumerate(axes.flatten()):
        if i < len(vals):
            v = results[i]
            min_val, max_val = min(v), max(v)
            bins = range(min_val, max_val + 2)  # +2 to include max value
            
            # Histogram
            ax.hist(v, bins=bins, alpha=0.7, edgecolor='black')
            ax.set_xticks(range(min_val, max_val + 1))  # Show integer ticks
            ax.set_title(f"{method_name} n={vals[i]}")
            ax.set_xlabel('Value')
            ax.set_ylabel('Frequency')

            # Compute stats
            mean = np.mean(v)
            std_dev = np.std(v)

            # Add stats text
            ax.text(
                0.95, 0.95,
                f"Mean = {mean:.2f}\nStd Dev = {std_dev:.2f}",
                transform=ax.transAxes,
                fontsize=10,
                verticalalignment='top',
                horizontalalignment='right',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
            )

        else:
            ax.axis('off')  # Hide any empty subplot

    plt.tight_layout()
    plt.savefig(f"{method_name}_all_distributions.png")
    plt.show()

def compare_distributions(list1: list, list2: list, val:int, label1="Standard Chaining", label2="Two Choice Chaining"):
    # Compute statistics
    mean1, std1 = np.mean(list1), np.std(list1)
    mean2, std2 = np.mean(list2), np.std(list2)

    print(f"------- Val = {val} -------")
    print(f"{label1}: Mean = {mean1:.2f}, Std Dev = {std1:.2f}")
    print(f"{label2}: Mean = {mean2:.2f}, Std Dev = {std2:.2f}")

    # Plot combined histogram
    bins = range(min(min(list1), min(list2)), max(max(list1), max(list2)) + 2)

    plt.hist(list1, bins=bins, alpha=0.6, edgecolor='black', label=label1)
    plt.hist(list2, bins=bins, alpha=0.6, edgecolor='black', label=label2)

    plt.title(f"Distribution of Maximum Chain Lengths for n={val}")
    plt.xlabel("Max Chain Length")
    plt.ylabel("Frequency")
    plt.legend()

    # Save and show
    plt.tight_layout()
    plt.savefig(f"comparison_histogram_{val}.png")
    plt.show()

# Example usage inside main block
if __name__ == "__main__":
    standard_res, two_choice_res = run_evaluation_suite()
    
    # Assuming you want the results for n=100 across approaches
    
    
    vals = [100, 500, 1000]
    for i in range(len(vals)):
        standard_100 = standard_res[i]
        two_choice_100 = two_choice_res[i]
        compare_distributions(standard_100, two_choice_100, val=vals[i])

# # Example usage inside main block
# if __name__ == "__main__":
#     standard_res, two_choice_res = run_evaluation_suite()

#     vals = [100, 500, 1000]

#     plot_all_distributions(standard_res, vals, "Standard Chaining")
#     plot_all_distributions(two_choice_res, vals, "Two Choice Chaining")
    