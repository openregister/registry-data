---
date: 2019-03-26
status: accepted
code: 0001
---

# RSF as source of truth

## Context

This repository has been used to keep track of the metadata used in all
registers in different stages.

As part of the stream of work of creating a
[registers CLI](https://github.com/openregister/registers-cli) capable of processing
updates based on RSF as the source of truth this repository needs to adapt.


## Decision

This repository changes its purpose to become the master copy of all
registers managed by GDS.

Data will be stored as RSF (Register Serialisation Format) and will rely on
the registers CLI extract and manipulate the content.


## Consequences

This repository will keep a copy of the latest RSF for each register managed
by GDS.

Also, the old yaml files will be removed.
