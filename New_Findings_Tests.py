import New_Findings
import New_Findings_Annotated

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
            start_time = timeit.default_timer()

            result = func(*arguments, **keyworded_arguments)

            time_difference = timeit.default_timer() - start_time

            print(f"Function took {time_difference} seconds.")

            return result

    return wrapper

@profile_this_function
def test_massprimeduction():
    """
    Decorator must precede a newly created function.
    """
    New_Findings_Annotated.massprimeduction(200)

if __name__ == "__main__":
    test_massprimeduction()