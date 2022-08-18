from django.test import TestCase

"""My custom weird  test for numpy, openssl  and bitcoinlib. Long story short, sometimes numpy doesn't work after installation  and requores a reinstall and openssl requires adding a few lines of code to it' s ' openssl cnf config file ' """



# -*- coding: utf-8 -*-
#
#    BitcoinLib - Python Cryptocurrency Library
#
#    EXAMPLES - Wallets and Transactions
#
#    © 2018 February - 1200 Web Development <http://1200wd.com/>
#

import os
from pprint import pprint
from bitcoinlib.wallets import Wallet, BCL_DATABASE_DIR


#
# Create Wallets
#

# First recreate database to avoid already exist errors
test_databasefile = os.path.join(BCL_DATABASE_DIR, 'bitcoinlib.test.sqlite')
test_database = 'sqlite:///' + test_databasefile
if os.path.isfile(test_databasefile):
    os.remove(test_databasefile)

print("\n=== Create a wallet and a simple transaction ===")
wlt = Wallet.create('wlttest1', network='bitcoinlib_test', db_uri=test_database)
wlt.get_key()
wlt.utxos_update()  # Create some test UTXOs
wlt.info()
to_key = wlt.get_key()
print("\n- Create transaction (send to own wallet)")
t = wlt.send_to(to_key.address, 50000000)
t.info()

print("\n- Successfully send, updated wallet info:")
wlt.info()
