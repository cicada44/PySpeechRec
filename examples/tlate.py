# -----------------------------------------------------------------------------
#
# Trivial example for google translate in Python3
#
# -----------------------------------------------------------------------------

from googletrans import Translator


def translate_russian_to_english(sentence):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(sentence, src='ru', dest='en')
    return translation.text


# Example usage
russian_sentence = "Привет, как дела?"
english_translation = translate_russian_to_english(russian_sentence)

print(english_translation)
