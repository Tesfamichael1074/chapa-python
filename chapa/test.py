#!/usr/bin/env python3

from api import Chapa

ch_test = Chapa('<sample_key>', response_format='json')

ch_test.send_request('', '' , {}, "", '')



