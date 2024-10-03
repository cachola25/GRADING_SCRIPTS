import os
import subprocess
import glob

# Copy any files needed to run the student's assignment into the directory
# with the students' code
if __name__ == '__main__':
    dir = os.getcwd()
    files_to_copy = glob.glob(f"{dir}/filesToCopy/*")
    for i in range(1,4):
        os.chdir(f"{dir}/grp{i}")
        original_dir = os.getcwd()
        files = os.listdir(original_dir)
        for file in files:
            if os.path.isdir(file):
                print(f"{dir}/grp{i}/{file}")
                os.chdir(f"{dir}/grp{i}/{file}")
                for src_file in files_to_copy:
                    subprocess.run(['cp', f"{src_file}", f"{os.getcwd()}/{os.path.basename(src_file)}"])
                os.chdir(original_dir)
                    
        