from django.shortcuts import render
from googletrans.constants import LANGCODES
#from translate import Translator
from . import translate
# Create your views here.

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'be': 'belarusian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'zh-CN': 'chinese_simplified',
    'zh-TW': 'chinese_traditional',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'de': 'german',
    'el': 'greek',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'ko': 'korean',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'mt': 'maltese',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'yi': 'yiddish',
}


def Homepage(request):
    return render(request, "homepage.html")


def TranslatorPage(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        from_lang = request.POST['from_lang']
        to_lang = request.POST['to_lang']
        print(from_lang, to_lang)
        output_text = translate.translate(original_text, from_lang, to_lang)
        #translation = Translator(to_lang="Kannada")

        #output_text = translation.translate(original_text)
        return render(request, 'homepage.html', {'output_text': output_text, 'original_text': original_text, "LANGUAGES": LANGUAGES.items()})
    else:
        return render(request, "homepage.html", {"LANGUAGES": LANGUAGES.items()})