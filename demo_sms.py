import time
from pygsm import GsmModem

gsm = GsmModem(port = "/dev/ttyUSB0", logger = GsmModem.debug_logger).boot()

print("Waiting for network...")
s = gsm.wait_for_network()

with open("messaggio.txt", "rt") as f:
    messaggio = f.read()

with open("lista.csv", "rt") as f:
    for i, l in enumerate(f):
        gsm.send_sms(l.strip(), messaggio)
        time.sleep(1)

gsm.disconnect()