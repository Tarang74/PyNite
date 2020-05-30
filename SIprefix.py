from sympy.functions import floor, ceiling, log
from re import compile

SI_PREFIX_UNITS = "yzafpnµm kMGTPEZY"

CRE_SI_NUMBER = compile(r'\s*(?P<sign>[\+\-])?'
                           r'(?P<integer>\d+)'
                           r'(?P<fraction>.\d+)?\s*'
                           u'(?P<si_unit>[%s])?\s*' % SI_PREFIX_UNITS)
                           
def si_format(value, precision=0, format_str=u'{value} {prefix}',
              exp_format_str=u'{value}e{ex10}', p=1):
    if p < 1:
        raise ValueError("Exponent out range for unit.")

    sValue, ex10 = split(value, precision, p=p)
    value_format = u'%%.%df' % precision
    value_str = value_format % sValue
    try:
        return format_str.format(value=value_str,
                                 prefix=prefix(ex10).strip())
    except ValueError:
        sign = ''
        if ex10 > 0:
            sign = "+"
        return exp_format_str.format(value=value_str,
                                     ex10=''.join([sign, str(ex10)]))

def split(value, precision=1, p=1):
    negative = False
    g = 3*p
    ex = 0

    if value < 0.:
        value = -value
        negative = True
    elif value == 0.:
        return 0., 0

    if negative == False: 
        ex10 = floor(float(log(value, 10)))
    else: 
        ex10 = ceiling(float(log(value, 10)))
    
    if ex10 > 0:
        mod = floor(ex10 / g)
        if floor(ex10 / g) > 1:
            mod = ceiling(ex10 / g)
        value /= (10 ** (g*mod))

        ex = floor(ex10 / g) * 3
        if floor(ex10 / g) > 1:
            ex = ceiling(ex10 / g) * 3
    elif ex10 < 0:
        mod = ceiling(-ex10 / g)
        value *= (10 ** (g*mod))
        
        ex = ceiling(-ex10 / g) * -3

    if negative:
        value *= -1
    
    return value, int(ex)

def prefix(ex10):
    prefix_levels = (len(SI_PREFIX_UNITS) - 1) // 2
    si_level = int(ceiling(ex10 / 3))
    if abs(si_level) > prefix_levels:
        raise ValueError("Exponent out range of available prefixes.")
    return SI_PREFIX_UNITS[si_level + prefix_levels]

def si_parse(value):
    CRE_10E_NUMBER = compile(r'^\s*(?P<integer>[\+\-]?\d+)?'
                                r'(?P<fraction>.\d+)?\s*([eE]\s*'
                                r'(?P<ex10>[\+\-]?\d+))?$')
    CRE_SI_NUMBER = compile(r'^\s*(?P<number>(?P<integer>[\+\-]?\d+)?'
                               r'(?P<fraction>.\d+)?)\s*'
                               u'(?P<si_unit>[%s])?\s*$' % SI_PREFIX_UNITS)
    match = CRE_10E_NUMBER.match(value)
    if match:
        # Can be parse using `float`.
        assert(match.group('integer') is not None or
               match.group('fraction') is not None)
        return float(value)
    match = CRE_SI_NUMBER.match(value)
    assert(match.group('integer') is not None or
           match.group('fraction') is not None)
    d = match.groupdict()
    si_unit = d['si_unit'] if d['si_unit'] else ' '
    prefix_levels = (len(SI_PREFIX_UNITS) - 1) // 2
    scale = 10 ** (3 * (SI_PREFIX_UNITS.index(si_unit) - prefix_levels))
    return float(d['number']) * scale

def si_prefix_scale(si_unit):
    return 10 ** si_prefix_ex10(si_unit)

def si_prefix_ex10(si_unit):
    prefix_levels = (len(SI_PREFIX_UNITS) - 1) // 2
    return (3 * (SI_PREFIX_UNITS.index(si_unit) - prefix_levels))
