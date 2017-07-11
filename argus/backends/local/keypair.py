# Copyright 2017 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six
import paramiko
import os
import getpass


class LocalKeyPair(object):

    def __init__(self):
        self._name = '%s@%s' % (getpass.getuser(), os.uname()[1])
        self._private_key, self._public_key = self.generate_key_pair()

    def generate_key_pair(self, bits=2048):
        key = paramiko.RSAKey.generate(bits)
        keyout = six.StringIO()
        key.write_private_key(keyout)
        private_key = keyout.getvalue()
        public_key = '%s %s %s' % (key.get_name(),
                                   key.get_base64(), self._name)
        return (private_key, public_key)

    @property
    def public_key(self):
        return self._public_key

    @property
    def private_key(self):
        return self._private_key
