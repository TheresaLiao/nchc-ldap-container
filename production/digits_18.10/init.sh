#!/bin/bash

tmpHome=$HOME
export $(sudo cat /proc/1/environ | tr '\0' '\n')
export HOME=$tmpHome
export BAZELRC=$HOME/.bazelrc
