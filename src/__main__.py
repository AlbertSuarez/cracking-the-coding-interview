import argparse
import glob
import subprocess
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--questions_folder', type=str, default='src/questions')
    parser.add_argument('--rtd', type=int, default=3)
    return parser.parse_args()


def run_all():
    python_file_list = [i for i in glob.glob(f'{args.questions_folder}/**/**/*.py')]
    python_file_list = [i for i in python_file_list if not i.endswith('__init__.py')]
    python_file_list = [i.replace('.py', '') for i in python_file_list]
    python_file_list = [i.replace('/', '.') for i in python_file_list]
    for idx, python_path in enumerate(python_file_list):
        print(f'({idx + 1}/{len(python_file_list)}) Running [{python_path}]...')
        subprocess.call(f'python3 -m {python_path}', shell=True)
        time.sleep(args.rtd)


if __name__ == '__main__':
    args = parse_args()
    run_all()
