#!/usr/bin/env python3
import sys
import time
import re
import logging
from subprocess import Popen, PIPE, DEVNULL

logging.basicConfig(format='SGE job check: %(asctime)s - %(message)s',
                    level=logging.DEBUG)

#-- functions --#
def log_output(ret):
    for line in ret.decode().split('\n'):
        if line.rstrip() != '':
            logging.warning(line)

#def qstat_check(jobid, regex):
#    """
#    Using qstat to identify running files
#    """
#    p = Popen(['qstat'], stdout=PIPE, stderr=PIPE)
#    output, err = p.communicate()
#    if p.returncode != 0:
#        log_output(output)
#        log_output(err)        
#        return 0
#    for x in output.decode().split('\n'):
#        y = re.split(regex, x)
#        if y[0] == jobid:
#            if y[4] in ['r', 'qw', 't']:
#                print('running')
#            elif y[4] in ['Eqw', 'd', 'dr']:
#                print('failed')
#            else:
#                msg = 'Job status not recognized: "{}"'
#                logging.warning(msg.format(y[4]))
#                print('running')
#            p.stdout.close()
#            exit(0)

def qstat_check(jobid, regex):
    """
    Using qstat to identify running files
    """
    p = Popen(['qstat', '-j', str(jobid)], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    if p.returncode != 0:
#        logging.warning('-- qstat check --')
#        log_output(output)
#        log_output(err)        
        return 0
    else:
        print('running')
        exit(0)
            
def acct_check(jobid, max_lines):
    """
    Directly looking for the jobid in the SGE accounting file
    """
    acct_file = '/var/lib/gridengine/default/common/accounting'
    cmd = 'tail -n {max_lines} {acct_file} | tac | awk -F: -v id={jobid}'
    cmd = cmd.format(max_lines=max_lines, acct_file=acct_file, jobid=jobid)
    cmd += " '{if ($6 == id) {print $0; exit 0}}'"
    p = Popen([cmd], stdout=PIPE, shell=True)
    output, err = p.communicate()
    if p.returncode != 0:
        return 0
    for i,x in enumerate(output.decode().split('\n')):
        if i > max_lines:
            p.stdout.close()
            break
        y = x.split(':')
        if len(y) < 12:
            continue
        else:
            if y[12] == '0':
                print('success')
            else:
                print('failed')
            p.stdout.close()
            exit(0)
                
def qacct_check(jobid, regex):
    """
    Falling back to using qacct to find finished jobs based on jobid
    """
    cmd = ['qacct', '-j', str(jobid)]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    if p.returncode != 0:
#        logging.warning('-- qacct check --')
#        log_output(output)
#        log_output(err)
        time.sleep(3)
        return 0
    for x in output.decode().split('\n'):
        x = regex.split(x)
        if x[0] == 'exit_status':
            if x[1] == '0':
                print('success')
            else:
                print('failed')            
            exit(0)
            
#-- main --#
jobid = sys.argv[1]
regex = re.compile(r' +')
try:
    for i in range(15):
        # checking qstat
        qstat_check(jobid, regex)
        # if not listed via qstat, parsing sge accounting info
#        acct_check(jobid, 1000)
        # if not listed at the end of the acct file, trying qacct
        qacct_check(jobid, regex)
        # waiting
        time.sleep(5 + i)
    logging.warning(f'WARNING: jobid-{jobid} produced time-out failure')
    print('failed')
    exit(0)
except KeyboardInterrupt:
    print('failed')    
    exit(0)
except (OSError, ValueError, AssertionError, IndexError) as e:
    pass
# last resort
print('running')
