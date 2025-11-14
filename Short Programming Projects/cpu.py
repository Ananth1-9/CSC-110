def get_result(gigahertz, core_count):
    gh = float(gigahertz)
    cc = int(core_count)
    if cc >= 20:
        return 'That is a high-performance CPU.'
    elif gh >= 3.2 and cc >= 8:
        return 'That is a high-performance CPU.'
    elif gh >= 2.5 and cc >= 6:
        return 'That is a medium-performance CPU.'
    elif gh >= 2.0 and cc >= 2:
        return 'That is a low-performance CPU.'
    else:
        return 'That CPU could use an upgrade.'
    