print("Hello world")

import argparse
import os
import random

def generate_test_results(total_test_count, total_stage_count, tests_to_fail_count, jenkins_url):
    # Check if the specified number of tests to fail is greater than the total number of tests
    if tests_to_fail_count > total_test_count:
        print("Error: The number of tests to fail cannot be greater than the total number of tests.")
        return

    # Create test cases and stages
    test_cases = [f"Test{i}" for i in range(1, total_test_count + 1)]
    test_stages = [f"Stage{i}" for i in range(1, total_stage_count + 1)]

    # Randomly select tests to fail
    tests_to_fail = random.sample(test_cases, tests_to_fail_count)

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

    # Create out/tests directory
    tests_dir = os.path.join('out', 'tests')
    os.makedirs(tests_dir, exist_ok=True)

    # Generate PASS.txt or FAIL.txt for each test case
    for test_case in test_cases:
        result_file_path = os.path.join(tests_dir, f"{test_case}.txt")
        with open(result_file_path, 'w') as result_file:
            result_file.write(f"Test Case: {test_case}\n\n")
            for stage, result in zip(results['Stage'], results['Result']):
                result_file.write(f"({result}) : {stage}\n")
                if result == 'PASS':
                    result_file.write(f"Stage{stage} has Passed Successfully..!!\n")
                elif result == 'FAIL':
                    result_file.write(f"Stage{stage} has FAILED..!!\n")
                    break

    # Print Jenkins artifact details
    print("\nJenkins Artifacts:")
    for test_case in test_cases:
        print(f"{jenkins_url}/job/jenkinsgitintegration/ws/out/tests/{test_case}.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate detailed dummy test results.')
    parser.add_argument('--total_test_count', type=int, help='Total number of test cases')
    parser.add_argument('--total_stage_count', type=int, help='Total number of stages in each test case')
    parser.add_argument('--tests_to_fail_count', type=int, help='Number of tests to mark as FAIL')
    parser.add_argument('--jenkins_url', type=str, help='Jenkins server URL')

    args = parser.parse_args()

    total_test_count = args.total_test_count
    total_stage_count = args.total_stage_count

    generate_test_results(total_test_count, total_stage_count, args.tests_to_fail_count, args.jenkins_url)
