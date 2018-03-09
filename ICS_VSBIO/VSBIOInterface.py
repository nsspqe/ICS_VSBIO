# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_VSBIOInterface')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_VSBIOInterface')
    _VSBIOInterface = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_VSBIOInterface', [dirname(__file__)])
        except ImportError:
            import _VSBIOInterface
            return _VSBIOInterface
        try:
            _mod = imp.load_module('_VSBIOInterface', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _VSBIOInterface = swig_import_helper()
    del swig_import_helper
else:
    import _VSBIOInterface
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def ReadVSBW(filename: 'wchar_t const *') -> "ReadHandle":
    return _VSBIOInterface.ReadVSBW(filename)
ReadVSBW = _VSBIOInterface.ReadVSBW

def ReadVSB(filename: 'char const *') -> "ReadHandle":
    return _VSBIOInterface.ReadVSB(filename)
ReadVSB = _VSBIOInterface.ReadVSB

def ReadNextMessage(handle: 'ReadHandle', message: 'icsSpyMessageVSB', size: 'unsigned int') -> "unsigned int *":
    return _VSBIOInterface.ReadNextMessage(handle, message, size)
ReadNextMessage = _VSBIOInterface.ReadNextMessage

def ReadClose(handle: 'ReadHandle') -> "void":
    return _VSBIOInterface.ReadClose(handle)
ReadClose = _VSBIOInterface.ReadClose

def GetProgress(handle: 'ReadHandle') -> "int":
    return _VSBIOInterface.GetProgress(handle)
GetProgress = _VSBIOInterface.GetProgress

def GetProgressString(handle: 'ReadHandle') -> "char const *":
    return _VSBIOInterface.GetProgressString(handle)
GetProgressString = _VSBIOInterface.GetProgressString

def GetDisplayMessage(handle: 'ReadHandle') -> "char const *":
    return _VSBIOInterface.GetDisplayMessage(handle)
GetDisplayMessage = _VSBIOInterface.GetDisplayMessage

def GetErrorMessage(handle: 'ReadHandle') -> "char const *":
    return _VSBIOInterface.GetErrorMessage(handle)
GetErrorMessage = _VSBIOInterface.GetErrorMessage

def WriteVSBW(filename: 'wchar_t const *') -> "WriteHandle":
    return _VSBIOInterface.WriteVSBW(filename)
WriteVSBW = _VSBIOInterface.WriteVSBW

def WriteVSB(filename: 'char const *') -> "WriteHandle":
    return _VSBIOInterface.WriteVSB(filename)
WriteVSB = _VSBIOInterface.WriteVSB

def WriteMessage(handle: 'WriteHandle', message: 'icsSpyMessageVSB', size: 'unsigned int') -> "int":
    return _VSBIOInterface.WriteMessage(handle, message, size)
WriteMessage = _VSBIOInterface.WriteMessage

def WriteClose(handle: 'WriteHandle') -> "void":
    return _VSBIOInterface.WriteClose(handle)
WriteClose = _VSBIOInterface.WriteClose

def VSBIOFree(message: 'icsSpyMessageVSB') -> "void":
    return _VSBIOInterface.VSBIOFree(message)
VSBIOFree = _VSBIOInterface.VSBIOFree

def VSBIOMalloc(nBytes: 'int') -> "icsSpyMessageVSB *":
    return _VSBIOInterface.VSBIOMalloc(nBytes)
VSBIOMalloc = _VSBIOInterface.VSBIOMalloc
class icsSpyMessageVSB(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, icsSpyMessageVSB, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, icsSpyMessageVSB, name)
    __repr__ = _swig_repr
    __swig_setmethods__["StatusBitField"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField_set
    __swig_getmethods__["StatusBitField"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField_get
    if _newclass:
        StatusBitField = _swig_property(_VSBIOInterface.icsSpyMessageVSB_StatusBitField_get, _VSBIOInterface.icsSpyMessageVSB_StatusBitField_set)
    __swig_setmethods__["StatusBitField2"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField2_set
    __swig_getmethods__["StatusBitField2"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField2_get
    if _newclass:
        StatusBitField2 = _swig_property(_VSBIOInterface.icsSpyMessageVSB_StatusBitField2_get, _VSBIOInterface.icsSpyMessageVSB_StatusBitField2_set)
    __swig_setmethods__["TimeHardware"] = _VSBIOInterface.icsSpyMessageVSB_TimeHardware_set
    __swig_getmethods__["TimeHardware"] = _VSBIOInterface.icsSpyMessageVSB_TimeHardware_get
    if _newclass:
        TimeHardware = _swig_property(_VSBIOInterface.icsSpyMessageVSB_TimeHardware_get, _VSBIOInterface.icsSpyMessageVSB_TimeHardware_set)
    __swig_setmethods__["TimeHardware2"] = _VSBIOInterface.icsSpyMessageVSB_TimeHardware2_set
    __swig_getmethods__["TimeHardware2"] = _VSBIOInterface.icsSpyMessageVSB_TimeHardware2_get
    if _newclass:
        TimeHardware2 = _swig_property(_VSBIOInterface.icsSpyMessageVSB_TimeHardware2_get, _VSBIOInterface.icsSpyMessageVSB_TimeHardware2_set)
    __swig_setmethods__["TimeSystem"] = _VSBIOInterface.icsSpyMessageVSB_TimeSystem_set
    __swig_getmethods__["TimeSystem"] = _VSBIOInterface.icsSpyMessageVSB_TimeSystem_get
    if _newclass:
        TimeSystem = _swig_property(_VSBIOInterface.icsSpyMessageVSB_TimeSystem_get, _VSBIOInterface.icsSpyMessageVSB_TimeSystem_set)
    __swig_setmethods__["TimeSystem2"] = _VSBIOInterface.icsSpyMessageVSB_TimeSystem2_set
    __swig_getmethods__["TimeSystem2"] = _VSBIOInterface.icsSpyMessageVSB_TimeSystem2_get
    if _newclass:
        TimeSystem2 = _swig_property(_VSBIOInterface.icsSpyMessageVSB_TimeSystem2_get, _VSBIOInterface.icsSpyMessageVSB_TimeSystem2_set)
    __swig_setmethods__["TimeStampHardwareID"] = _VSBIOInterface.icsSpyMessageVSB_TimeStampHardwareID_set
    __swig_getmethods__["TimeStampHardwareID"] = _VSBIOInterface.icsSpyMessageVSB_TimeStampHardwareID_get
    if _newclass:
        TimeStampHardwareID = _swig_property(_VSBIOInterface.icsSpyMessageVSB_TimeStampHardwareID_get, _VSBIOInterface.icsSpyMessageVSB_TimeStampHardwareID_set)
    __swig_setmethods__["TimeStampSystemID"] = _VSBIOInterface.icsSpyMessageVSB_TimeStampSystemID_set
    __swig_getmethods__["TimeStampSystemID"] = _VSBIOInterface.icsSpyMessageVSB_TimeStampSystemID_get
    if _newclass:
        TimeStampSystemID = _swig_property(_VSBIOInterface.icsSpyMessageVSB_TimeStampSystemID_get, _VSBIOInterface.icsSpyMessageVSB_TimeStampSystemID_set)
    __swig_setmethods__["NetworkID"] = _VSBIOInterface.icsSpyMessageVSB_NetworkID_set
    __swig_getmethods__["NetworkID"] = _VSBIOInterface.icsSpyMessageVSB_NetworkID_get
    if _newclass:
        NetworkID = _swig_property(_VSBIOInterface.icsSpyMessageVSB_NetworkID_get, _VSBIOInterface.icsSpyMessageVSB_NetworkID_set)
    __swig_setmethods__["NodeID"] = _VSBIOInterface.icsSpyMessageVSB_NodeID_set
    __swig_getmethods__["NodeID"] = _VSBIOInterface.icsSpyMessageVSB_NodeID_get
    if _newclass:
        NodeID = _swig_property(_VSBIOInterface.icsSpyMessageVSB_NodeID_get, _VSBIOInterface.icsSpyMessageVSB_NodeID_set)
    __swig_setmethods__["Protocol"] = _VSBIOInterface.icsSpyMessageVSB_Protocol_set
    __swig_getmethods__["Protocol"] = _VSBIOInterface.icsSpyMessageVSB_Protocol_get
    if _newclass:
        Protocol = _swig_property(_VSBIOInterface.icsSpyMessageVSB_Protocol_get, _VSBIOInterface.icsSpyMessageVSB_Protocol_set)
    __swig_setmethods__["MessagePieceID"] = _VSBIOInterface.icsSpyMessageVSB_MessagePieceID_set
    __swig_getmethods__["MessagePieceID"] = _VSBIOInterface.icsSpyMessageVSB_MessagePieceID_get
    if _newclass:
        MessagePieceID = _swig_property(_VSBIOInterface.icsSpyMessageVSB_MessagePieceID_get, _VSBIOInterface.icsSpyMessageVSB_MessagePieceID_set)
    __swig_setmethods__["ExtraDataPtrEnabled"] = _VSBIOInterface.icsSpyMessageVSB_ExtraDataPtrEnabled_set
    __swig_getmethods__["ExtraDataPtrEnabled"] = _VSBIOInterface.icsSpyMessageVSB_ExtraDataPtrEnabled_get
    if _newclass:
        ExtraDataPtrEnabled = _swig_property(_VSBIOInterface.icsSpyMessageVSB_ExtraDataPtrEnabled_get, _VSBIOInterface.icsSpyMessageVSB_ExtraDataPtrEnabled_set)
    __swig_setmethods__["NumberBytesHeader"] = _VSBIOInterface.icsSpyMessageVSB_NumberBytesHeader_set
    __swig_getmethods__["NumberBytesHeader"] = _VSBIOInterface.icsSpyMessageVSB_NumberBytesHeader_get
    if _newclass:
        NumberBytesHeader = _swig_property(_VSBIOInterface.icsSpyMessageVSB_NumberBytesHeader_get, _VSBIOInterface.icsSpyMessageVSB_NumberBytesHeader_set)
    __swig_setmethods__["NumberBytesData"] = _VSBIOInterface.icsSpyMessageVSB_NumberBytesData_set
    __swig_getmethods__["NumberBytesData"] = _VSBIOInterface.icsSpyMessageVSB_NumberBytesData_get
    if _newclass:
        NumberBytesData = _swig_property(_VSBIOInterface.icsSpyMessageVSB_NumberBytesData_get, _VSBIOInterface.icsSpyMessageVSB_NumberBytesData_set)
    __swig_setmethods__["NetworkID2"] = _VSBIOInterface.icsSpyMessageVSB_NetworkID2_set
    __swig_getmethods__["NetworkID2"] = _VSBIOInterface.icsSpyMessageVSB_NetworkID2_get
    if _newclass:
        NetworkID2 = _swig_property(_VSBIOInterface.icsSpyMessageVSB_NetworkID2_get, _VSBIOInterface.icsSpyMessageVSB_NetworkID2_set)
    __swig_setmethods__["DescriptionID"] = _VSBIOInterface.icsSpyMessageVSB_DescriptionID_set
    __swig_getmethods__["DescriptionID"] = _VSBIOInterface.icsSpyMessageVSB_DescriptionID_get
    if _newclass:
        DescriptionID = _swig_property(_VSBIOInterface.icsSpyMessageVSB_DescriptionID_get, _VSBIOInterface.icsSpyMessageVSB_DescriptionID_set)
    __swig_setmethods__["ArbIDOrHeader"] = _VSBIOInterface.icsSpyMessageVSB_ArbIDOrHeader_set
    __swig_getmethods__["ArbIDOrHeader"] = _VSBIOInterface.icsSpyMessageVSB_ArbIDOrHeader_get
    if _newclass:
        ArbIDOrHeader = _swig_property(_VSBIOInterface.icsSpyMessageVSB_ArbIDOrHeader_get, _VSBIOInterface.icsSpyMessageVSB_ArbIDOrHeader_set)
    __swig_setmethods__["Data"] = _VSBIOInterface.icsSpyMessageVSB_Data_set
    __swig_getmethods__["Data"] = _VSBIOInterface.icsSpyMessageVSB_Data_get
    if _newclass:
        Data = _swig_property(_VSBIOInterface.icsSpyMessageVSB_Data_get, _VSBIOInterface.icsSpyMessageVSB_Data_set)
    __swig_setmethods__["StatusBitField3"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField3_set
    __swig_getmethods__["StatusBitField3"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField3_get
    if _newclass:
        StatusBitField3 = _swig_property(_VSBIOInterface.icsSpyMessageVSB_StatusBitField3_get, _VSBIOInterface.icsSpyMessageVSB_StatusBitField3_set)
    __swig_setmethods__["StatusBitField4"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField4_set
    __swig_getmethods__["StatusBitField4"] = _VSBIOInterface.icsSpyMessageVSB_StatusBitField4_get
    if _newclass:
        StatusBitField4 = _swig_property(_VSBIOInterface.icsSpyMessageVSB_StatusBitField4_get, _VSBIOInterface.icsSpyMessageVSB_StatusBitField4_set)
    __swig_setmethods__["AckBytes"] = _VSBIOInterface.icsSpyMessageVSB_AckBytes_set
    __swig_getmethods__["AckBytes"] = _VSBIOInterface.icsSpyMessageVSB_AckBytes_get
    if _newclass:
        AckBytes = _swig_property(_VSBIOInterface.icsSpyMessageVSB_AckBytes_get, _VSBIOInterface.icsSpyMessageVSB_AckBytes_set)
    __swig_setmethods__["ExtraDataPtr"] = _VSBIOInterface.icsSpyMessageVSB_ExtraDataPtr_set
    __swig_getmethods__["ExtraDataPtr"] = _VSBIOInterface.icsSpyMessageVSB_ExtraDataPtr_get
    if _newclass:
        ExtraDataPtr = _swig_property(_VSBIOInterface.icsSpyMessageVSB_ExtraDataPtr_get, _VSBIOInterface.icsSpyMessageVSB_ExtraDataPtr_set)
    __swig_setmethods__["MiscData"] = _VSBIOInterface.icsSpyMessageVSB_MiscData_set
    __swig_getmethods__["MiscData"] = _VSBIOInterface.icsSpyMessageVSB_MiscData_get
    if _newclass:
        MiscData = _swig_property(_VSBIOInterface.icsSpyMessageVSB_MiscData_get, _VSBIOInterface.icsSpyMessageVSB_MiscData_set)
    __swig_setmethods__["Reserved"] = _VSBIOInterface.icsSpyMessageVSB_Reserved_set
    __swig_getmethods__["Reserved"] = _VSBIOInterface.icsSpyMessageVSB_Reserved_get
    if _newclass:
        Reserved = _swig_property(_VSBIOInterface.icsSpyMessageVSB_Reserved_get, _VSBIOInterface.icsSpyMessageVSB_Reserved_set)

    def __init__(self):
        this = _VSBIOInterface.new_icsSpyMessageVSB()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _VSBIOInterface.delete_icsSpyMessageVSB
    __del__ = lambda self: None
icsSpyMessageVSB_swigregister = _VSBIOInterface.icsSpyMessageVSB_swigregister
icsSpyMessageVSB_swigregister(icsSpyMessageVSB)

icsSpyMessageVSB_SIZE = _VSBIOInterface.icsSpyMessageVSB_SIZE
eSuccess = _VSBIOInterface.eSuccess
eEndOfFile = _VSBIOInterface.eEndOfFile
eError = _VSBIOInterface.eError
eBufferToSmall = _VSBIOInterface.eBufferToSmall

def GetEDP(message: 'icsSpyMessageVSB') -> "char *":
    return _VSBIOInterface.GetEDP(message)
GetEDP = _VSBIOInterface.GetEDP
# This file is compatible with both classic and new-style classes.


