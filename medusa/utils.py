# -*- coding: utf-8 -*-
# Copyright 2019 Spotify AB. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import sys
import traceback

import medusa.monitoring

def evaluate_boolean(value):
    # same behaviour as python's configparser
    if str(value).lower() in ('0', 'false', 'no', 'off'):
        return False
    elif str(value).lower() in ('1', 'true', 'yes', 'on'):
        return True
    else:
        raise TypeError('{} not a boolean'.format(value))


def handle_exception(exception, msg, tags, config):
    medusa.monitoring.send(tags, 1)
    if medusa.utils.evaluate_boolean(config.grpc.enabled):
        # Propagate the exception when running gRPC server so that exception/error
        # details can be sent back to client.
        raise exception
    else:
        logging.error(msg)
        traceback.print_exc()
        sys.exit(1)

