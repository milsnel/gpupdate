#
# GPOA - GPO Applier for Linux
#
# Copyright (C) 2019-2020 BaseALT Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from abc import ABC


def check_experimental_enabled(storage):
    experimental_enable_flag = 'Software\\BaseALT\\Policies\\gpupdate\\global_experimental_enable'
    flag = storage.get_hklm_entry(experimental_enable_flag)

    if '1' == flag:
        return True

    return False

def check_module_enabled(storage, module_name, default):
    gpupdate_module_enable_branch = 'Software\\BaseALT\\Policies\\gpupdate'
    gpupdate_module_flag = '{}\\{}_enable'.format(gpupdate_module_enable_branch, module_name)
    flag = storage.get_hklm_entry(gpupdate_module_flag)

    if '1' == flag:
        return True
    if '0' == flag:
        return True

    return default

class applier_frontend(ABC):
    @classmethod
    def __init__(self, regobj):
        pass

    @classmethod
    def apply(self):
        pass

