import os
from glob import glob
from subprocess import check_output, CalledProcessError

import yaml

ACCOUNT_ID = os.environ['ACCOUNT_ID']


def run(command):
    print('Running', command)
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.output.decode('utf-8'))


def _configure_profile(profile_name, profile_role):
    print('Got', profile_role, 'for', profile_name)
    if profile_name != 'default':
        profile_name = f'profile.{profile_name}'
    run(f'aws configure set {profile_name}.region us-east-1')
    run(f'aws configure set {profile_name}.credential_source EcsContainer')
    if profile_role:
        run(f'aws configure set {profile_name}.role_arn {profile_role}')


def go():
    for path in glob('config/app/*/config.yaml'):
        parsed = yaml.load(open(path))
        profile_name = parsed['profile']
        account_id = parsed.get('account_id', ACCOUNT_ID)
        _configure_profile(profile_name, f'arn:aws:iam::{account_id}:role/${PROJECT_NAME}-target')
    _configure_profile('default', None)


if __name__ == '__main__':
    go()
