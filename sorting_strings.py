import re
import collections

p = re.compile(r'(?P<date>\d{4}[-/]\d{2}[-/]\d{2})|(?P<num>[0-9-\.]+)|(?P<word>[a-zA-Z]+)')


def get_type_and_value(s):
    tps, mapping_values = [], []
    for m in p.finditer(s):
        for k, v in m.groupdict().iteritems():
            if v:
                tps.append(k)
                mapping_values.append(get_mapping_value(k, v))
    return tuple(tps), tuple(mapping_values)


def get_mapping_value(tp, s):
    if tp == 'num':
        return float(s)
    elif tp == 'date':
        return ''.join(re.split('[-/]', s))
    else:
        return s


class StringType(object):
    def __init__(self, s):
        self.val = s
        # tuple of types in the compound string, type of mapping value (for sorting comparison)
        self.types, self.mappings = get_type_and_value(s)


def sortStrings(strings):
    s_types = collections.defaultdict(list)
    for s in strings:
        s_type = StringType(s)
        s_types[s_type.types].append(s_type)
    result = []
    for type_list in s_types.values():
        result += [item.val for item in sorted(type_list, key=lambda tp: tp.mappings)]
    return result


print sortStrings(["-2.4", "-1", "2", "10", ".2"])
print sortStrings(["2017-09-01", "2016/10/10", "2016-10-12", "2017-01-01"])
print sortStrings(["Apple", "Cat", "Bob123", "Banana2017-03-03", "banana"])

print sortStrings(['abc45', 'cdf123', 'bcd44', '123xyz2017-03-03', '234abc'])
print sortStrings(["a1", "a2016-01-01", "a3"])
