#!/usr/bin/python
# IBM_PROLOG_BEGIN_TAG
# This is an automatically generated prolog.
#
# $Source: op-test-framework/ci/source/test_op_bmc_web_update.py $
#
# OpenPOWER Automated Test Project
#
# Contributors Listed Below - COPYRIGHT 2015
# [+] International Business Machines Corp.
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.
#
# IBM_PROLOG_END_TAG

import os
import sys
#from op_ci_bmc import bmc_reboot
#full_path = os.path.abspath(os.path.dirname(sys.argv[0])).split('ci')[0]
#sys.path.append(full_path)
#import op_ci_bmc
# Fixture
import op_bmc_web_update

def test_config_check():
    assert op_bmc_web_update.test_init() == 0

def test_bmc_web_pnor_update_hpm():
    assert op_bmc_web_update.bmc_web_pnor_update_hpm() == 0

def test_bmc_web_bmc_update_hpm():
    assert op_bmc_web_update.bmc_web_bmc_update_hpm() == 0

def test_bmc_web_bmcandpnor_update_hpm():
    assert op_bmc_web_update.bmc_web_bmcandpnor_update_hpm() == 0
