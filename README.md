# pfSense Faux-API Scripts

This is a collection of Python scripts for interacting with [pfSense FauxAPI](https://github.com/ndejong/pfsense_fauxapi) to automate some common pfSense functions. It leverages FauxAPI's [python client](https://github.com/ndejong/pfsense_fauxapi_client_python).

The following packages need to be installed on the machine which is using FauxAPI's Python client:

```
pip3 install pfsense-fauxapi
pip3 install python-dotenv
```

To install Faux API on pfSense use the procedure given [here](https://github.com/ndejong/pfsense_fauxapi#installation).

Copy and rename the `.env.example` file to `.env` and set the values of the given environment variables in it.