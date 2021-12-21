#!/usr/bin/python3
# coding=utf-8

#   Copyright 2021 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" Module """
from pylon.core.tools import log, web  # pylint: disable=E0611,E0401
from pylon.core.tools import module  # pylint: disable=E0611,E0401

from .components import render_security_test_create


class Module(module.ModuleModel):
    """ Task module """

    def __init__(self, context, descriptor):
        self.context = context
        self.descriptor = descriptor

    def init(self):
        """ Init module """
        log.info(f"Initializing module {self.descriptor.name}")

        self.descriptor.init_blueprint()
        # link: https://webdesign.tutsplus.com/tutorials/auto-formatting-input-value--cms-26745

        self.context.slot_manager.register_callback('security_scheduling_test_create', render_security_test_create)


    def deinit(self):  # pylint: disable=R0201
        """ De-init module """
        log.info(f"De-initializing {self.descriptor.name}")

    @web.route('/scheduling')
    def tst(self):
        # return render_security_test_create(self.context, None, {})
        return self.descriptor.render_template(
            'tst_security_test_create.html',
        )
