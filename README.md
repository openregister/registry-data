## Registers

## Register register, Field register and Datatype register data

### Prerequisites

```
mkvirtualenv -p /path/to/python3 somename
pip3 install -r requirements.txt
```

### Register register

####  Install requirements

`make init`


#### Import data into the Register register

To import data, first adjust the Makefile REGISTER_URL variable with
* On production: http://register.openregister.org
* On local environment: http://register.openregister.dev:9000

And then:<br>
`make register`

## Create a new register

To create a new register:

1. add a yaml file for the register to the data/register directory in
   this repository.
2. ensure you have a `~/.boto` [file with credentials](http://boto.readthedocs.org/en/latest/boto_config_tut.html) for setting a CNAME in route 53.
3. ensure you have the [field.register][] repository checked out in
   the same directory as this repo.
4. run the command: `bin/add_register.py data/register/<new-register>.yaml <herokuapp-to-host-register> --record_description="<description of a record for the field register>"`

[field.register]: https://github.com/openregister/field.register


### Datatype register

#### Import data into the datatype register

To import data, first adjust the Makefile DATATYPE_URL variable with
* On production: http://datatype.openregister.org
* On local environment: http://datatype.openregister.dev:9000

And then:<br>
`make datatype`

#### Add a new datatype

1. add a yaml file for the register to the data/Datatype directory in
   this repository and run the make task above again.


### Field register

#### Import data into the field register

Visit:

* On production: http://register.openregister.org/load
* On local environment: http://register.openregister.dev:9000/load

and follow instructions.

#### Add a new field to field register

Add a line to data/Field/fields.tsv. Then load as above.


