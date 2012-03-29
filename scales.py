#!/usr/bin/env python

FLAT = '\342\231\255'
SHARP = '\342\231\257'

def get_key_name(scale, key):
    if 'Minor' in scale:
        # transpose key to its relative minor
        key = minorkeys[keys.index(key)]

    return key.replace('es', FLAT).replace('is', SHARP).upper()

keys = [ 'c', 'g', 'd', 'a', 'e', 'f', 'bes', 'ees', 'aes' ]
minorkeys = [ 'a', 'e', 'b', 'fis', 'cis', 'd', 'g', 'c', 'f' ]
scales = [
    'Major',
    'NatMinor',
    'HarMinor',
    'Dorian',
    'Lydian',
    'Mixolydian',
    'Blues',
    'Pentatonic'
]

time = {
    'Pentatonic': r'\time 6/4'
}

scalenames = {
    'NatMinor': 'nat. minor',
    'HarMinor': 'har. minor',
    'Pentatonic' : 'Pent.',
}

for scale in scales:
    print '{'
    print "\override Score.RehearsalMark #'self-alignment-X = #LEFT"
    print time.get(scale, r'\time 8/4')
    for key in keys:
        print r'\mark \markup { %s %s }' % (
            get_key_name(scale, key), scalenames.get(scale, scale))
        print r'\key %s \major \transpose c %s \%s' % (key, key, scale)
    print '}'
