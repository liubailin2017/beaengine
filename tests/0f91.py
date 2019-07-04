#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):


        # 0F 91
        # REX + 0F 91
        # SETNO r/m8

        Buffer = '0f9100'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f91)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'setno ')
        assert_equal(myDisasm.instr.repr, 'setno byte ptr [rax]')

        Buffer = '0f91c0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f91)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'setno ')
        assert_equal(myDisasm.instr.repr, 'setno al')

        # VEX.L0.0F.W0 91 /r
        # KMOVW m16, k1

        myVEX = VEX('VEX.L0.0F.W0')
        myVEX.R = 1
        Buffer = '{}9120'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x91')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovw ')
        assert_equal(myDisasm.instr.repr, 'kmovw word ptr [r8], k4')

        # VEX.L0.66.0F.W0 91 /r
        # KMOVB m8, k1

        myVEX = VEX('VEX.L0.66.0F.W0')
        myVEX.R = 1
        Buffer = '{}9120'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x91')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovb ')
        assert_equal(myDisasm.instr.repr, 'kmovb byte ptr [r8], k4')

        # VEX.L0.0F.W1 91 /r
        # KMOVQ m64, k1

        myVEX = VEX('VEX.L0.0F.W1')
        myVEX.R = 1
        Buffer = '{}9120'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x91')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovq ')
        assert_equal(myDisasm.instr.repr, 'kmovq qword ptr [r8], k4')

        # VEX.L0.66.0F.W1 91 /r
        # KMOVD m32, k1

        myVEX = VEX('VEX.L0.66.0F.W1')
        myVEX.R = 1
        Buffer = '{}9120'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x91')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovd ')
        assert_equal(myDisasm.instr.repr, 'kmovd dword ptr [r8], k4')
