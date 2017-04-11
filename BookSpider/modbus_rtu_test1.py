#!/usr/bin/env python
# -*- coding: utf_8 -*-
""" 
 Modbus TestKit: Implementation of Modbus protocol in python 
 (C)2009 - Luc Jean - luc.jean@gmail.com 
 (C)2009 - Apidev - http://www.apidev.fr 
 This is distributed under GNU LGPL license, see license.txt 
"""

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# PORT = 1
#PORT = "/dev/ttyUSB0"
PORT = 'COM4'


def test_mbrtu_master():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=19200, bytesize=8, parity='E', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")

        '''
        # 1—从设备地址
        # cst.READ_HOLDING_REGISTERS—读保持寄存器，命令码03
        # 0—开始地址
        # 4—读4个字节
        '''
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4))

        # send some queries
        # logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        # logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        # logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))

        '''
        # cst.WRITE_SINGLE_REGISTER—向保持寄存器写入一个数据，　命令码06
        # 1—从设备地址
        # 4—开始地址
        # 54—写入值
        '''
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 4, output_value=54))
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))

        '''
        # cst.WRITE_SINGLE_REGISTER—向保持寄存器写入连续数据，　命令码16
        # 1—从设备地址
        # 4—开始地址
        # 54—写入值
        '''
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 5, output_value=xrange(4)))

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())


if __name__ == "__main__":
    test_mbrtu_master()
