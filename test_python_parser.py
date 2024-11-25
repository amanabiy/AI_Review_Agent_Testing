def x(_): 
    __ = lambda _: x(chr(ord(_) + 1)) if _ != '' else 1
    _ = list(__.__code__.co_consts)[-1]; _2 = len(_); 
    ___ = lambda _, __: _.__class__.__name__[:2] == __[:2]; __ = ___
    ___ = ''.join
    _____ = [[c + d for c in __] for d in __ for __ in _]
    _______ = [__ for _ in _____ for __ in _]
    _8 = lambda __: x(_______[int(__.__class__.__name__[-1])])
    _8(__)
    return list(______)[_2]

print(x(''))
