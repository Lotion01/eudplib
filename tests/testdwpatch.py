import sys
import os

sys.path.insert(0, os.path.abspath('..\\'))


from eudplib import *

LoadMap('outputmap/basemap/basemap.scx')


@EUDFunc
def main():
    DoActions([
        SetMemory(0x58A364, SetTo, 1234),
        SetMemory(0x58A368, SetTo, 5678),
    ])

    f_simpleprint(
        "1 : ",
        f_dwread_epd(EPD(0x58A364)),
        f_dwread_epd(EPD(0x58A368))
    )

    f_dwpatch_epd(EPD(0x58A364), 123)
    f_dwpatch_epd(EPD(0x58A368), 456)

    f_simpleprint(
        "2 : ",
        f_dwread_epd(EPD(0x58A364)),
        f_dwread_epd(EPD(0x58A368))
    )

    data = Db(b'\x01\x02\x03\x04\x05\x06\x07\x08')
    f_blockpatch_epd(
        EPD(0x58A364),
        EPD(data),
        2
    )

    f_simpleprint(
        "3 : (Should be %d, %d)" % (0x04030201, 0x08070605),
        f_dwread_epd(EPD(0x58A364)),
        f_dwread_epd(EPD(0x58A368))
    )

    f_unpatchall()

    f_simpleprint(
        "4 : ",
        f_dwread_epd(EPD(0x58A364)),
        f_dwread_epd(EPD(0x58A368))
    )


SaveMap('outputmap/testdwpatch.scx', main)
