# alpha-registers-data

## This repo contains data for Register register, Field register and Datatype register



### Working with the register register

####  Install requirements

`make init`

#### Import data into a register

To import data, first adjust the Makefile REGISTER_URL variable with
* On production: http://register.openregister.org
* On local environment: http://register.openregister.dev:9000

And then:<br>
`make`

## Create a new register

To create a new register:

1. add a yaml file for the register to the data/register directory in
   this repository.
2. ensure you have a `~/.boto` file with credentials for setting a CNAME in route 53.
3. ensure you have the [field.register][] repository checked out in
   the same directory as this repo.
4. run the command: `bin/add_register.py data/register/<new-register>.yaml <herokuapp-to-host-register> --record_description="<description of a record for the field register>"`

[field.register]: https://github.com/openregister/field.register


### Working with the field register

#### Add a new field

Add a line to data/Field/fields.tsv

#### Import data into the field register

Visit:

* On production: http://register.openregister.org/load
* On local environment: http://register.openregister.dev:9000/load

and follow instructions.


