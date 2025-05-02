#!/usr/bin/python3
'''Method for calculating minumumof operation
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    cpy_buffer = 0
    done = 1
    while done < n:
        if cpy_buffer == 0:
           # first copy all and paste
            cpy_buffer = done
            done += cpy_buffer
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            cpy_buffer = done
            done += cpy_buffer
            ops_count += 2
        elif cpy_buffer > 0:
            # paste
            done += cpy_buffer
            ops_count += 1
    return ops_count
