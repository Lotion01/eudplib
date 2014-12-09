#!/usr/bin/python
# -*- coding: utf-8 -*-

from .. import core as c
import struct


class EUDGrp(c.EUDObject):
    def __init__(self, content):
        super().__init__()
        if type(content) is str:
            content = open(content, 'rb').read()
        self._content = content

    def Evaluate(self):
        return c.GetObjectAddr(self) + 2

    def GetDataSize(self):
        return len(self._content) + 2

    def WritePayload(self, buf):
        buf.WriteBytes(b'\0\0')  # 2byte padding to align dwords at (*)

        # fill in grp header
        b = self._content
        fn, w, h = struct.unpack('<HHH', b[0:6])
        buf.WriteWord(fn)
        buf.WriteWord(w)
        buf.WriteWord(h)

        # fill in grp frame headers table
        selfaddr = self.Evaluate()

        for i in range(fn):
            fhoffset = 6 + 8 * i
            xoff, yoff, w, h, lto = struct.unpack(
                '<BBBBI', b[fhoffset: fhoffset + 8])
            buf.WriteByte(xoff)
            buf.WriteByte(yoff)
            buf.WriteByte(w)
            buf.WriteByte(h)
            buf.WriteDword(lto + selfaddr)  # (*)

        buf.WriteBytes(b[6 + 8 * fn:])