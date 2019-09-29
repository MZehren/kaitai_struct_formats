# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class GuitarPro5(KaitaiStruct):
    """Guitar Pro is a very common software to transcribe music. TODO 
    blabla
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_version = self._io.read_bytes(30)
        _io__raw_version = KaitaiStream(BytesIO(self._raw_version))
        self.version = self._root.ByteStr(_io__raw_version, self, self._root)
        self.test = self._io.read_u4le()
        self.test2 = self._io.read_s1()

    class ByteStr(KaitaiStruct):
        """bla."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_s1()
            self.value = (self._io.read_bytes(self.len)).decode(u"UTF-8")


    class IntByteStr(KaitaiStruct):
        """blablabla."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_s4le()
            self._raw_value = self._io.read_bytes(self.len)
            _io__raw_value = KaitaiStream(BytesIO(self._raw_value))
            self.value = self._root.ByteStr(_io__raw_value, self, self._root)



