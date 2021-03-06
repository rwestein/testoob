# Testoob, Python Testing Out Of (The) Box
# Copyright (C) 2005-2006 The Testoob Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"getting information about errors"

def create_err_info(test, err):
    """
    Factory method for creating ErrInfo instances.
    """
    if isinstance(err, ErrInfo):
        return err

    return ErrInfo(test, err)

def _should_skip(exception_type):
    import testoob
    try:
        return issubclass(exception_type, testoob.SkipTestException)
    except TypeError:
        # subclass check failed, assume not a subclass of SkipTestException
        return False

class ErrInfo:
    """
    An interface for getting information about test errors.
    Reporters receive instances of this class.
    """
    def __init__(self, test, exc_info):
        self.test = test
        self.exc_info = exc_info

    def __str__(self):
        from common import exc_info_to_string
        from test_info import TestInfo
        return exc_info_to_string(self.exc_info, TestInfo(self.test))

    def is_skip(self):
        """
        Does the error signify a skip?

        Normally done by checking that exception_type derives from
        SkipTestException, but that can't be done after fields pickling.
        """
        return _should_skip(self.exc_info[0])

    def exception_type(self):
        t = self.exc_info[0]
        try:
            return t.__module__ + "." + t.__name__
        except AttributeError:
            return str(t)

    def exception_value(self):
        return str(self.exc_info[1])

    def traceback(self):
        return self.exc_info[2]

from testoob.utils import add_fields_pickling
add_fields_pickling(ErrInfo)
