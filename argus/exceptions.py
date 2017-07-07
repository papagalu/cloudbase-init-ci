# Copyright 2014 Cloudbase Solutions Srl
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
"""Various exceptions that can be raised by the CI project."""


class ArgusError(Exception):
    pass


class ArgusTimeoutError(ArgusError):
    pass


class ArgusCLIError(ArgusError):
    pass


class ArgusPermissionDenied(ArgusError):
    pass


class ArgusHeatTeardown(ArgusError):
    pass


class ArgusEnvironmentError(ArgusError):
    """Base class for errors related to the Argus environment."""
    pass


class ArgusInvalidDecoratorError(ArgusError):
    """Exception triggered when a decorator has been improperly used."""
    pass
