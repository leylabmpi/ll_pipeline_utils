#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import re
import argparse
import logging
import subprocess

desc = 'Getting the size/inode usage of a directory'
epi = """DESCRIPTION:
Getting the size and inode usage & limits for a specific directory.
"""
parser = argparse.ArgumentParser(description=desc,
                                 epilog=epi,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--directory', type=str, default='.',
                    help='Target directory (default: %(default)s)')
parser.add_argument('--version', action='version', version='0.0.1')

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


def run_cmd(cmd):
    """ returns % used
    """
    try:
        with open(os.devnull, 'w') as DNULL:
            res = subprocess.run(cmd, check=True, shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=DNULL)
    except subprocess.CalledProcessError as e:
        return None
    res = res.stdout.decode()
    for i,line in enumerate(res.split('\n')):
        if i == 1:
            line = re.split(r' +', line)
            total = float(line[1])
            used = float(line[2])
            used = -used if used < 0 else used
            perc_used = used / total * 100
            if perc_used > 100:
                perc_used = used / float(line[3]) * 100
            return perc_used
    return 0

def get_inodes(path):
    """ returns % used
    """
    # determine the basal directory
    parent_dir = [x for x in re.split(r'/', path) if x != '']
    try:
        parent_dir = os.path.join('/' + parent_dir[0], parent_dir[1])
    except IndexError:
        parent_dir = os.path.join('/' + parent_dir[0])
    st_p = os.statvfs(parent_dir)    
    st_c = os.statvfs(path)
    print([st_p.f_ffree,st_c.f_ffree])
    used_inode = st_p.f_ffree - st_c.f_ffree
    total_inode = st_c.f_files
    inode_perc = used_inode / total_inode * 100
    return inode_perc
        
def main(args):
    args.directory = os.path.abspath(args.directory)
    size = run_cmd('df {}'.format(args.directory))
    inodes = get_inodes(args.directory)
    print('% used size: {}'.format(round(size,1)))
    print('% used inodes: {}'.format(round(inodes,1)))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
