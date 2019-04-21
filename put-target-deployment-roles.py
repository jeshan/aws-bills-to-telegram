from glob import glob
from subprocess import check_output, CalledProcessError


def run(command):
    print('Running', command)
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output.decode('utf-8'))


def go():
    for path in glob('config/app/*/config.yaml'):
        env = path[:path.rindex('/')]
        env = env[env.rindex('/') + 1:]
        output = run(f'sceptre --no-colour launch -y app/{env}/base')
        print(output)


if __name__ == '__main__':
    go()
