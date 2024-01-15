
import os
from hello_world import generate_test_results  # Importing the generate_test_results function

def create_artifacts_directory(test_case):
    # Create directory if it doesn't exist
    directory_path = f"out/tests/{test_case}"
    os.makedirs(directory_path, exist_ok=True)
    return directory_path

def create_status_text(status, stage):
    return f"({status}) : {stage}\nStage {stage} has {'Passed Successfully' if status == 'PASS' else 'FAILED..!!'}"

def process_test_results(total_test_count, total_stage_count):
    for test_case in range(1, total_test_count + 1):
        # Run the test generation function from python1.py
        generate_test_results(total_test_count, total_stage_count, test_case - 1, test_case - 1)

        # Create artifacts directory for the current test case
        test_case_directory = create_artifacts_directory(f"Test{test_case}")

        # Get the final result for the current test case
        final_result = 'PASS' if 'PASS.txt' in os.listdir(test_case_directory) else 'FAIL.txt'

        # Write status text to the result file
        with open(os.path.join(test_case_directory, final_result), 'w') as result_file:
            for stage in range(1, total_stage_count + 1):
                status = 'PASS' if stage <= test_case else 'FAIL' if final_result == 'FAIL.txt' else 'NOT_RUN'
                status_text = create_status_text(status, f"Stage{stage}")
                result_file.write(status_text + '\n')

if __name__ == "__main__":
    # Provide total_test_count and total_stage_count
    total_test_count = 5
    total_stage_count = 6

    # Run the process_test_results function
    process_test_results(total_test_count, total_stage_count)
