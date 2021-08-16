""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;?। '
_eos = '~'
_special = '-'
_english_jaso_code = list(range(0x0040,0x007A))
_bengali_jaso_code = list(range(0x0980,0x09FF))
_jaso_code = _english_jaso_code + _bengali_jaso_code + _english_jaso_code
_jaso = list(chr(c) for c in _jaso_code)
_letters = _jaso

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
#symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
symbols = [_pad] + list(_punctuation) + list(_punctuation) + list(_letters)
