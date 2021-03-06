# -*- coding: utf-8 -*-
#  Copyright 2011 Takeshi KOMIYA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys

from blockdiag.utils.bootstrap import Application

import seqdiag
import seqdiag.builder
import seqdiag.drawer
import seqdiag.parser


class SeqdiagApp(Application):
    module = seqdiag


def main(args=sys.argv[1:]):
    return SeqdiagApp().run(args)
