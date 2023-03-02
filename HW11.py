# def cache_decorator(func):
#     d = {}
#
#     def qwerty(*args):
#         def qwerty(*args, **kwargs):
#             try:
#                 return d[args]
#             except KeyError:
#                 qwe = func(*args)
#                 qwe = func(*args, **kwargs)
#                 d[args] = qwe
#                 return qwe