#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/13/2020 9:19 PM
# @Author  : Guofeng Mei
# @Email   : Guofeng.Mei@student.uts.edu.au
# @File    : net_function.py
# @Software: PyCharm
import multiprocessing as mp
import sys
import time

import numpy as np
from scipy.integrate import odeint


def lorenz(v0, t, sigma, rho, beta):
    x, y, z = v0
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]


def solve(v0):
    t = np.linspace(0, 200, 801)
    sigma = 10.0
    rho = 28.0
    beta = 8 / 3.0
    sol = odeint(lorenz, v0, t, args=(sigma, rho, beta), rtol=1e-10, atol=1e-12)
    print(sol)
    return sol


if __name__ == "__main__":
    ics = np.random.randn(2, 3)
    print("multiprocessing:", end='')
    tstart = time.time()
    num_processes = 5
    p = mp.Pool(num_processes)
    mp_solutions = p.map(solve, ics)
    tend = time.time()
    tmp = tend - tstart
    print(" %8.3f seconds" % tmp)

    print("serial:         ", end='')
    sys.stdout.flush()
    tstart = time.time()
    serial_solutions = [solve(ic) for ic in ics]
    tend = time.time()
    tserial = tend - tstart
    print(" %8.3f seconds" % tserial)

    print("num_processes = %i, speedup = %.2f" % (num_processes, tserial / tmp))

    check = [(sol1 == sol2).all()
             for sol1, sol2 in zip(serial_solutions, mp_solutions)]
    if not all(check):
        print("There was at least one discrepancy in the solutions.")
