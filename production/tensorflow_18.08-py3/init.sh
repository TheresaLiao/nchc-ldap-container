#!/bin/bash

tmpHome=$HOME
export $(sudo cat /proc/1/environ | tr '\0' '\n' | sed 's/CC_OPT_FLAGS.*//')
export CC_OPT_FLAGS="-march=sandybridge -mtune=broadwell"
export HOME=$tmpHome
export BAZELRC=$HOME/.bazelrc
