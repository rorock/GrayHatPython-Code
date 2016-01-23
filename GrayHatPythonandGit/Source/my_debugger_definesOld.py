from ctypes import *
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE= c_void_p


DEBUG_PROCESS=0x00000001
CREATE_NEW_COSOLE=0x00000010

class STARTUPINFO(Structure):
    _fields_ = [
                ("cb",  DWORD),
                ("lpReserved",LPTSTR),
                ("lpDesktop",LPTSTR),
                ("lpTitle",LPTSTR),
                ("dwX",DWORD),
                ("dwY",DWORD),
                ("dwXSize",DWORD),
                ("dwYSize",DWORD),
                ("dwXCountChars",DWORD),
                ("dwFillAttribute",DWORD),
                ("wShowWindow",DWORD),
                ("cbReserved2",WORD),
                ("lpReserved2",LPBYTE),
                ("hStdInput",HANDLE),
                ("hStdOutput",HANDLE),
                ("hStdError",HANDLE),
                ]
class PROCESS_INFORMATION(Structure):
        _fields_ = [ 
                    ("hProcess", HANDLE),
                    ("hThread", HANDLE),
                    ("dwProcessId", DWORD),
                    ("dwThreadID", DWORD),
                    ]
        
        print ("IN DEFINES")