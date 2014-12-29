Requirements:
-------------------------
Generic:
* Myriadcoin >=0.9.2.7
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local myriadcoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net {network_name} 

Replace {network_name} with the following depending on the algorithm:

<<<<<<< HEAD
* SHA256d - myriad_sha256d
* Scrypt - myriad_scrypt
* Scrypt - myriad_scrypt_lh (Low hash rate network)
* Skein - myriad_skein
* Myr-Groestl - myriad_groestl
* Qubit - myriad_qubit
=======
If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 9333 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk

Official wiki:
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web frontend:
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Notes for Litecoin:
=========================
Requirements:
-------------------------
In order to run P2Pool with the Litecoin network, you would need to build and install the
ltc_scrypt module that includes the scrypt proof of work code that Litecoin uses for hashes.

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
>>>>>>> upstream/master
	
To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!):

* SHA256d: Worker Port = 5578; Peer-2-Peer Port = 5577
* Scrypt: Worker Port = 5556; Peer-2-Peer Port = 5555
* Scrypt Low Hash: Worker Port = 5558; Peer-2-Peer Port = 5557
* Skein: Worker Port = 5589; Peer-2-Peer Port = 5588
* Myr-Groestl: Worker Port = 3333; Peer-2-Peer Port = 8889
* Qubit: Worker Port = 5567; Peer-2-Peer Port = 5566


Run for additional options:

    python run_p2pool.py --help

Official wiki :
-------------------------
<<<<<<< HEAD
https://en.bitcoin.it/wiki/P2Pool
=======

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
 
License:
-------------------------

[Available here](COPYING)

>>>>>>> upstream/master

