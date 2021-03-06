#!/usr/bin/env python

# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Need to figure out why this only fails on travis
# pylint: disable=bad-continuation

"""
Executes a command, and cleans up minikube state for profile $HOSTNAME
This should be run with the minikube-in-go job type
"""

import argparse
import os
import subprocess
import sys
import socket

def check(*cmd):
    """Log and run the command, raising on errors."""
    print >>sys.stderr, 'Run:', cmd
    exception = None
    try:
        subprocess.check_call(cmd)
    except:
        exception = sys.exc_info()[0]
        pass # handle errors in the called executable
    subprocess.call(["minikube", "delete", "--profile=%s" % socket.gethostname()])
    subprocess.call(["rm", "-Rf", "/var/lib/libvirt/caches/minikube/.minikube/machines/%s" % socket.gethostname()])
    if exception:
        raise exception

def main(envs, cmd):
    """Run script and verify it exits 0."""
    for env in envs:
        key, val = env.split('=', 1)
        print >>sys.stderr, '%s=%s' % (key, val)
        os.environ[key] = val
    if not cmd:
        raise ValueError(cmd)
    check(*cmd)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--env', default=[], action='append')
    PARSER.add_argument('cmd', nargs=1)
    PARSER.add_argument('args', nargs='*')
    ARGS = PARSER.parse_args()
    main(ARGS.env, ARGS.cmd + ARGS.args)
