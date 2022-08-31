#!/usr/bin/env python3
#import subprocess as sp
#import shlex
import sys
import logging
from subprocess import Popen, PIPE, DEVNULL, CalledProcessError

logging.basicConfig(format='SGE job cancel: %(asctime)s - %(message)s',
                    level=logging.DEBUG)

def log_output(ret):
    for line in ret.decode().split('\n'):
        if line.rstrip() != '':
            logging.warning(line)

def qdel(jobid):
    cmd = ['qdel', str(jobid)]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    if rc != 0:
        msg = '--- WARNING: non-zero exit for: {} ---'
        logging.warning(msg.format(' '.join(cmd)))         
        log_output(output)
        log_output(err)
    
for jobid in sys.argv[1:]:
    qdel(jobid)
