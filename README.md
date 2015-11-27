# Register, field and datatype register data

Register entries for the
[register register](http://register.openregister.org),
[field register](http://field.openregister.org) and
[datatype register](http://datatype.openregister.org)
are currently maintained as individual yaml files in the [data](data/) directory.

# Tests

The shape of the registers and links between the data can be tested by running `make`
— we recommend using a [Python virtual environment](http://virtualenvwrapper.readthedocs.org/en/latest/):

    $ mkvirtualenv -p python3 registers
    $ workon registers
    $ make init

    $ make

A dump of each register as `JSON-L` is generated in the [prod](prod) directory.
