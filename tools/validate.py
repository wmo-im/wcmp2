###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################

import json
import logging
import os
import sys

from jsonschema import RefResolver, validate
import yaml

LOGGER = logging.getLogger(__name__)


def validate_json(instance: dict, schema: dict, schema_dir: str) -> bool:

    resolver = RefResolver(base_uri=f'file://{schema_dir}/', referrer=schema)

    validate(instance, schema, resolver=resolver)

    return True


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <instance> <schema>')
        sys.exit(1)

    schema_dir = os.path.dirname(os.path.abspath(sys.argv[2]))

    with open(sys.argv[1]) as fh1, open(sys.argv[2]) as fh2:
        instance = json.load(fh1)
        schema = yaml.load(fh2, Loader=yaml.SafeLoader)

        try:
            validate_json(instance, schema, schema_dir)
        except Exception as err:
            msg = f'ERROR: {err}'
            print(msg)
