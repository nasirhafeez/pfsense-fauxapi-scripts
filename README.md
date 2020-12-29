# pfSense FauxAPI Scripts

This is a collection of Python scripts for interacting with [pfSense FauxAPI](https://github.com/ndejong/pfsense_fauxapi) to automate some common pfSense functions. It leverages FauxAPI's [python client](https://github.com/ndejong/pfsense_fauxapi_client_python). These scripts have been tested on pfSense v2.4.5-RELEASE-p1.

The following packages need to be installed on the machine which is using FauxAPI's Python client:

```
pip3 install pfsense-fauxapi
pip3 install python-dotenv
```

To install Faux API on pfSense use the procedure given [here](https://github.com/ndejong/pfsense_fauxapi#installation).

Copy and rename the `.env.example` file to `.env` and set the values of the given environment variables in it.

The `user_ovpn_setup.py` script relies on API Action `function_call`. It should be setup as follows:

```
cp /etc/fauxapi/pfsense_function_calls.sample.txt /etc/fauxapi/pfsense_function_calls.txt
```

Edit `/etc/fauxapi/pfsense_function_calls.txt` in a text editor and uncomment the line `openvpn.inc:function openvpn_resync_csc_all()`.
