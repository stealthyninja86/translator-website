from googletrans import Translator
#from translate import Translator


def translate(text, fro, to):
    translator = Translator()
    translation = translator.translate(text, dest=to, src=fro)
    return translation.text

# def trans(text):
#    translation = Translator(to_lang="Kannada")
#    return translation.text