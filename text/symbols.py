""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;?। '
_eos = '~'
_special = '-'
_bengali_jaso_code = list(range(0x0980,0x09FF))
_bengali_jaso = list(chr(c) for c in _bengali_jaso_code)
_letters = _bengali_jaso

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
#symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
symbols = list(_punctuation) + list(_punctuation) + list(_letters)
