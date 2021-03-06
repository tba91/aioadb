class BaseException(Exception):
    '''Base exception class'''
    pass


class OpenFileError(Exception):
    '''Raised when couldn't open a file'''


class AdbResponseError(Exception):
    '''Raised when adb response doesn't match'''


class AdbConnectionClosedError(Exception):
    '''Raised when adb connection closes'''
   

class AdbShellReadError(Exception):
    '''Raised when couldn't read all response data from adb'''


class SyncError(BaseException):
    '''Base sync exception class'''
    pass


class StartSyncError(SyncError):
    '''Raised when couldn't start sync'''
    pass


class PushSyncError(SyncError):
    '''Raised when couldn't complete push sync'''
    pass