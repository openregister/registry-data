# Register register data

The data for the
[register register](http://register.openregister.org),
[field register](http://field.openregister.org),
[datatype register](http://datatype.openregister.org),
and
[registry register](http://registry.openregister.org)
is currently maintained as individual yaml files in the [data](data/) directory.

# Testing

[![Build Status](https://travis-ci.org/openregister/registers.svg?branch=master)](https://travis-ci.org/openregister/registers)

The shape of the registers and links between the data can be tested by running `make`
— we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 registers
    $ workon registers
    $ make init

    $ make

A dump of each register as `JSON-L` is generated in the [prod](prod) directory.
