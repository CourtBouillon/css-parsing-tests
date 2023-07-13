import colorsys  # It turns out Python already does HSL -> RGB!


def trim(s):
    return s if not s.endswith('.0') else s[:-2]


print('[')
print(',\n'.join(
    '"hsl%s(%s, %s%%, %s%%%s)", [%s, %s, %s, %s]' % (
        ('a' if alpha is not None else '',
         hue, trim(str(saturation/10.)),
         trim(str(lightness/10.)),
         ', %s' % alpha if alpha is not None else '')
        + tuple(
            trim(str(round(val, 10))) for val in
            colorsys.hls_to_rgb(hue/360., lightness/1000., saturation/1000.))
        + (alpha if alpha is not None else 1,)
    )
    for alpha in [None, 1, .2, 0]
    for lightness in range(0, 1001, 125)
    for saturation in range(0, 1001, 125)
    for hue in range(0, 360, 30)
))
print(']')
