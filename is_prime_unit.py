
import cProfile
import pstats
import timeit

# The Decorator Function, activated by placing @function_name over another function.
def profile_this_function(func):
    def wrapper(*arguments, **keyworded_arguments):
        option = 1
        if option == 0:
            profiler = cProfile.Profile(timeunit=0.000001)  # Time units default to 1.0 seconds.
            profiler.enable()

            result = func(*arguments, **keyworded_arguments)

            profiler.disable()

            stats_o_profiler = pstats.Stats(profiler).strip_dirs().sort_stats(
                'cumulative')  # See other sort-bys available https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats
            stats_o_profiler.print_stats()
            return result

        elif option == 1:
            num_runs = 50
            results_list = []*num_runs
            exec_time_list = []*num_runs
            for i in range(num_runs):
                start_time = timeit.default_timer()

                result = func(*arguments, **keyworded_arguments)

                time_difference = timeit.default_timer() - start_time
                exec_time_list.append(time_difference)
                results_list.append(result)
            average_time = sum(exec_time_list)/len(exec_time_list)
            print(f"Function took {average_time:.15f} seconds.")

            for i in range(num_runs-1):
                if results_list[i+1] != results_list[i]:
                    print(f"Uneven results {results_list}")

            return results_list[0]
        elif option == 2:
            execution_time = timeit.timeit(lambda: func(*arguments, **keyworded_arguments), number=1000)
            print(f"Function took {execution_time:.15f} seconds.")
    return wrapper



def new_limit(use, primes):
    j=0
    squared=use**(1./2)
    while primes[j]<squared:
        j +=1
    j +=1
    return j

@profile_this_function
def is_it_prime(use, primes, limit):
    i=0
    Boo=True
    while (Boo==True) and (i<limit):
        if use%primes[i]!=0:
            i +=1
        else:
            Boo=False
    return Boo

def is_prime(curr_num, primes, limit): # ideally collapse the limit call to be insight too
    for i in range(0, limit, 1):
        if curr_num%primes[i]==0:
            return False
    return True

def test_prime_funcs(primes):
    """This is silly. Just plant the code into Annnotated.py and verify its correctness that way.

    Also this code is unclean
    """
    num_runs = primes[-1] + 1
    results_list = []*num_runs
    new_prime_list = []
    for i in range(num_runs+1):
        results_list[i] = is_it_prime(i, new_prime_list, new_limit(i, new_prime_list))
        if results_list[i]:
            new_prime_list.append(i)

    new_prime_list2 = []
    results_list2 = [] * num_runs
    for i in range(num_runs + 1):
        results_list2[i] = is_prime(i, new_prime_list, new_limit(i, new_prime_list))
        if results_list2[i]:
            new_prime_list2.append(i)

    for i in range(len(new_prime_list)):
        print(f"Matches? {results_list[i] == results_list2[i]}")

    if len(new_prime_list) != len(new_prime_list2):
        print("Prime results don't match.")

    for i in range(len(new_prime_list)):
        print(f"Primes match? {new_prime_list[i] == new_prime_list2[i]}   {new_prime_list[i] == primes[i]}")

if __name__ == '__main__':
    primes_test_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    curr_num = 59
    # print(is_it_prime(curr_num, primes_test_list, new_limit(curr_num, primes_test_list)))
    test_prime_funcs(primes_test_list)