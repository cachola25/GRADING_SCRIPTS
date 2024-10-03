import os
import subprocess
import json

# Python script to run tests on the students' program
# This would be modified from assignment to assignment 
# to accommodate different tests and different programming languages
if __name__ == '__main__':
    files = os.listdir(os.getcwd())
    
    with open("config.json", "r") as file:
        data = json.load(file)

    test_dir = data['test_dir']
    test_files = os.listdir(data['test_files'])
    
    if 'makefile' not in files:
        print('makefile not found')
        exit(1)
        
    result = subprocess.run(['make', 'all'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode != 0:
        print('make all failed')
        exit(1)
    print()
    for test in test_files:
        with open(f"{test_dir}/{test}", 'r') as file:
            if test == "test_valid.g":
                continue
            print(f"Running test {test}")
    
            result = subprocess.run(['./random_sentence'], stdin=file, capture_output=True)
            if result.stdout.decode('utf-8') == '' and result.stderr.decode('utf-8') == '':
                print("\033[91m" + "-" * 50 + "\033[0m")
                print("\033[91mError running test\033[0m")
            else:
                print("\033[92m" + "-" * 50 + "\033[0m")
                if result.stdout.decode('utf-8') != '':
                    print(result.stdout.decode('utf-8'))
                if result.stderr.decode('utf-8') != '':
                    print(result.stderr.decode('utf-8'))
            print("\n")
            
    if "test_valid.g" not in test_files:
        print("test_valid.g not found")
        exit(1)
    
    for i in range(3):
        with open(f"{test_dir}/test_valid.g", 'r') as file:
            print(f"Running test test_valid.g #{i+1}")
            result = subprocess.run(['./random_sentence'], stdin=file, capture_output=True)
            if result.stdout.decode('utf-8') == '' and result.stderr.decode('utf-8') == '':
                print("\033[91m" + "-" * 50 + "\033[0m")
                print("\033[91mError running test\033[0m")
            else:
                print("\033[92m" + "-" * 50 + "\033[0m")
                if result.stdout.decode('utf-8') != '':
                    print(result.stdout.decode('utf-8'))
                if result.stderr.decode('utf-8') != '':
                    print(result.stderr.decode('utf-8'))
            print("\n")
            subprocess.run(['make', 'clean'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            result = subprocess.run(['make', 'all'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
    subprocess.run(['make', 'clean'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)