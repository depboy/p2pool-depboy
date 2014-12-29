Requirements:
-------------------------
Generic:
* Myriadcoin >=0.9.2.10
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

* SHA256d - myriad_sha256d
* Scrypt - myriad_scrypt
* Scrypt - myriad_scrypt_lh (Low hash rate network)
* Skein - myriad_skein
* Myr-Groestl - myriad_groestl
* Qubit - myriad_qubit

To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!):

* SHA256d: Worker Port = 5578; Peer-2-Peer Port = 5577
* Scrypt: Worker Port = 5556; Peer-2-Peer Port = 5555
* Scrypt Low Hash: Worker Port = 5558; Peer-2-Peer Port = 5557
* Skein: Worker Port = 5589; Peer-2-Peer Port = 5588
* Myr-Groestl: Worker Port = 3333; Peer-2-Peer Port = 8889
* Qubit: Worker Port = 5567; Peer-2-Peer Port = 5566


Run for additional options:

    python run_p2pool.py --help

