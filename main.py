# main.py
import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python main.py <exercise_folder>')
        print('Example: python main.py exercise_01')
        return 1

    exercise = sys.argv[1]
    exercise_dir = Path(__file__).parent / exercise

    if not exercise_dir.exists() or not exercise_dir.is_dir():
        print(f'Error: folder not found: {exercise}')
        return 1

    test_module = f'{exercise}.test_solution'
    cmd = [sys.executable, '-m', 'unittest', test_module, '-v']

    print(f'Running tests for: {exercise}')
    print(f"Command: {' '.join(cmd)}")
    print('-' * 40)

    completed = subprocess.run(cmd)
    return completed.returncode


if __name__ == '__main__':
    raise SystemExit(main())