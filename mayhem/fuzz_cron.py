#!/usr/bin/env python3

import atheris
import sys

import fuzz_helpers

with atheris.instrument_imports():
    from cron_descriptor import ExpressionDescriptor, get_description


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        get_description(fdp.ConsumeRandomString())
        ExpressionDescriptor(fdp.ConsumeRandomString())
    except Exception:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
