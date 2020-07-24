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

def info_code(code):
    info_ids = dict()
    info_ids[1] = 'Starting GPOA via command invocation'
    info_ids[2] = 'Starting GPOA via D-Bus'
    info_ids[3] = 'Group Policy target set for update'
    info_ids[4] = 'Initializing Samba backend for domain'
    info_ids[5] = 'Initializing local backend without domain'
    info_ids[6] = 'Cache directory determined'
    info_ids[7] = 'Initializing plugin manager'
    info_ids[8] = 'ADP plugin initialized'
    info_ids[9] = 'Running ADP plugin'

    return info_ids.get(code, 'Unknown info code')

def error_code(code):
    error_ids = dict()
    error_ids[1] = 'Insufficient permissions to run gpupdate'
    error_ids[2] = 'gpupdate will not be started'
    error_ids[3] = 'Backend execution error'
    error_ids[4] = 'Error occurred while running frontend manager'
    error_ids[5] = 'Error running GPOA for computer'
    error_ids[6] = 'Error running GPOA for user'
    error_ids[7] = 'Unable to initialize Samba backend'
    error_ids[8] = 'Unable to initialize no-domain backend'
    error_ids[9] = 'Error running ADP'

    return error_ids.get(code, 'Unknown error code')

def debug_code(code):
    debug_ids = dict()
    debug_ids[1] = 'The GPOA process was started for user'
    debug_ids[2] = ''

    return debug_ids.get(code, 'Unknown debug code')

def warning_code(code):
    warning_ids = dict()
    warning_ids[1] = (
        'Unable to perform gpupdate for non-existent user, '
        'will update machine settings'
    )
    warning_ids[2] = (
        'Current permissions does not allow to perform gpupdate for '
        'designted user. Will update current user settings'
    )
    warning_ids[3] = 'oddjobd is inaccessible'
    warning_ids[4] = 'No SYSVOL entry assigned to GPO'
    warning_ids[5] = 'ADP package is not installed - plugin will not be initialized'

    return warning_ids.get(code, 'Unknown warning code')

def get_message(code):
    retstr = 'Unknown message type, no message assigned'

    if code.startswith('E'):
        retstr = error_code(int(code[1:]))
    if code.startswith('I'):
        retstr = info_code(int(code[1:]))
    if code.startswith('D'):
        retstr = debug_code(int(code[1:]))
    if code.startswith('W'):
        retstr = warning_code(int(code[1:]))

    return retstr

def message_with_code(code):
    retstr = '[' + code[0:1] + code[1:].rjust(5, '0') + ']: ' + get_message(code)

    return retstr

