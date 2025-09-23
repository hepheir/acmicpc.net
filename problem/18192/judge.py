import pathlib
import random
import subprocess


DIR = pathlib.Path(__file__).parent
INPUT_FILE = DIR / 'stdin'
OUTPUT_FILE = DIR / 'stdout'

if __name__ == '__main__':
    print()
    print(f'Start compiling...')
    subprocess.run(['make', 'main'], cwd=str(DIR))

    print()
    print(f'Start Judging...')
    for N in (10, 20, 50, 100, 200):
        print(f'Testing for {N=}')
        for _ in range(10):
            A = list(range(N))
            random.shuffle(A)
            INPUT_FILE.write_text(f'{N}\n'+' '.join(map(str, A)))
            OUTPUT_FILE.write_text('')

            subprocess.run(['./main'],
                        cwd=str(DIR),
                        stdin=INPUT_FILE.open('r'),
                        stdout=OUTPUT_FILE.open('w'))

            output = OUTPUT_FILE.read_text()
            accepted = output.split()[0] == 'Accepted'
            if not accepted:
                print(output)

    print()
    print('Accepted!')

    subprocess.run(['make', 'clean'],
                cwd=str(DIR),
                stdout=OUTPUT_FILE.open('w'))
    INPUT_FILE.unlink()
    OUTPUT_FILE.unlink()
