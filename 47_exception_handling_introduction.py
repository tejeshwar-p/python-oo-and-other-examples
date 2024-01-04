# Python does not have any checked exceptions concept.
# All the exceptions are treated the same way

# ZeroDivisionError: division by zero
# 1/0
# i = 0
# j = 10/i

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 2 + '2'
# values = [1, '2']
# sum(values)

# NameError: name 'value' is not defined. Did you mean: 'False'?
# value

# AttributeError: 'list' object has no attribute 'non_existing'
# values = [1, '2']
# print(values.non_existing)
# print(values.non_existing())

import builtins
help(builtins)

# CLASSES
#     object
#         BaseException
#             BaseExceptionGroup
#                 ExceptionGroup(BaseExceptionGroup, Exception)
#             Exception
#                 ArithmeticError
#                     FloatingPointError
#                     OverflowError
#                     ZeroDivisionError
#                 AssertionError
#                 AttributeError
#                 BufferError
#                 EOFError
#                 ImportError
#                     ModuleNotFoundError
#                 LookupError
#                     IndexError
#                     KeyError
#                 MemoryError
#                 NameError
#                     UnboundLocalError
#                 OSError
#                     BlockingIOError
#                     ChildProcessError
#                     ConnectionError
#                         BrokenPipeError
#                         ConnectionAbortedError
#                         ConnectionRefusedError
#                         ConnectionResetError
#                     FileExistsError
#                     FileNotFoundError
#                     InterruptedError
#                     IsADirectoryError
#                     NotADirectoryError
#                     PermissionError
#                     ProcessLookupError
#                     TimeoutError
#                 ReferenceError
#                 RuntimeError
#                     NotImplementedError
#                     RecursionError
#                 StopAsyncIteration
#                 StopIteration
#                 SyntaxError
#                     IndentationError
#                         TabError
#                 SystemError
#                 TypeError
#                 ValueError
#                     UnicodeError
#                         UnicodeDecodeError
#                         UnicodeEncodeError
#                         UnicodeTranslateError
#                 Warning
#                     BytesWarning
#                     DeprecationWarning
#                     EncodingWarning
#                     FutureWarning
#                     ImportWarning
#                     PendingDeprecationWarning
#                     ResourceWarning
#                     RuntimeWarning
#                     SyntaxWarning
#                     UnicodeWarning
#                     UserWarning
#             GeneratorExit
#             KeyboardInterrupt
#             SystemExit
#         bytearray
#         bytes
#         classmethod
#         complex
#         dict
#         enumerate
#         filter
#         float
#         frozenset
#         int
#             bool
#         list
#         map
#         memoryview
#         property
#         range
#         reversed
#         set
#         slice
#         staticmethod
#         str
#         super
#         tuple
#         type
#         zip
