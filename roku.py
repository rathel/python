#!/usr/bin/env python3

from roku import Roku
import ssdp

a = Roku.diacovery(timeout=10)

print(a)
