
# The simplest port 9100 printer honeypot

A simple multi-threaded TCP server listener that saves the raw socket input to files.

    [robbe@teslacoil PrinterHoneypot]$ ./raw_tcp9100.py
    [+] Writing to file 2018-12-03_20-52-02_127.0.0.1_53366.raw
    [+] Initializing thread for 127.0.0.1:53366
    [+] Running thread for 127.0.0.1:53366
    [ ] No more data from 127.0.0.1:53366
    ^C
    [*] Keyboard interrupt exiting ...
    Nr of threads joined: 1
    Nr of threads started: 1
