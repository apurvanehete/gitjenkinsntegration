# the same is copied in dummy 2
# This code will randomly select no. of test cases to fail between tests_to_fail_start & tests_to_fail_end range
# python3 dummy_test_result_generation_script.py --total_test_count 5 --total_stage_count 6 --tests_to_fail_range 0,4
# Below code will additionally throw error msg if range given is greater than. no of test_cases

import argparse
import random

def generate_test_results(total_test_count, total_stage_count, tests_to_fail_start, tests_to_fail_end):
    # Check if the specified range is greater than the total number of tests
    if tests_to_fail_end - tests_to_fail_start + 1 > total_test_count:
        print("Error: The specified range is greater than the total number of tests.")
        return

    # Create test cases and stages
    test_cases = [f"Test{i}" for i in range(1, total_test_count + 1)]
    test_stages = [f"Stage{i}" for i in range(1, total_stage_count + 1)]

    # Randomly choose the number of tests to fail within the specified range
    num_tests_to_fail = random.randint(tests_to_fail_start, min(tests_to_fail_end, total_test_count))

    # Randomly select tests to fail
    tests_to_fail = random.sample(test_cases, num_tests_to_fail)

    # Initialize result dictionary
    results = {'Test Case': [], 'Stage': [], 'Result': []}

    # Generate and append test results
    for test_case in test_cases:
        if test_case in tests_to_fail:
            # If the test is selected to fail, choose a random stage to fail
            fail_stage = random.choice(test_stages)
            for stage in test_stages:
                if stage == fail_stage:
                    result = 'FAIL'
                elif stage > fail_stage:
                    result = 'NOT_RUN'
                else:
                    result = 'PASS'
                results['Test Case'].append(test_case)
                results['Stage'].append(stage)
                results['Result'].append(result)
        else:
            # If the test is not selected to fail, mark all stages as PASS
            for stage in test_stages:
                results['Test Case'].append(test_case)
                results['Stage'].append(stage)
                results['Result'].append('PASS')

    # Print detailed results
    print("Detailed Test Results:")
    print(f"{'Test Case':<15}{'Stage':<15}{'Result'}")
    print('-' * 45)
    for i in range(len(results['Test Case'])):
        print(f"{results['Test Case'][i]:<15}{results['Stage'][i]:<15}{results['Result'][i]}")

    # Print results for each test
    print("\nResults for each Test:")
    for test_case in test_cases:
        test_result = set(results['Result'][i] for i in range(len(results['Test Case'])) if results['Test Case'][i] == test_case)
        final_result = 'FAIL' if 'FAIL' in test_result else 'PASS'
        print(f"{test_case}: {final_result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate detailed dummy test results.')
    parser.add_argument('--total_test_count', type=int, help='Total number of test cases')
    parser.add_argument('--total_stage_count', type=int, help='Total number of stages in each test case')
    parser.add_argument('--tests_to_fail_range', type=str, help='Range of tests to mark as FAIL (e.g., 0,5)')

    args = parser.parse_args()

    total_test_count = args.total_test_count
    total_stage_count = args.total_stage_count

    tests_to_fail_range = list(map(int, args.tests_to_fail_range.split(',')))
    generate_test_results(total_test_count, total_stage_count, tests_to_fail_range[0], tests_to_fail_range[1])
