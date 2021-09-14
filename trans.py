from googletrans import Translator
import eel

def select_language(before_translate,after_translate):
    language_dict = {
        "japanese":"ja",
        "english":"en",
        "korean":"ko",
        "chinese":"zh-cn",
        "german":"de",
        "french":"fr"
    }
    return language_dict[before_translate] , language_dict[after_translate]

def context_translate(context,before_translate,after_translate):
    translator = Translator()
    src_lang, dest_lang = select_language(before_translate,after_translate)
    trans_result = translator.translate(context,src=src_lang,dest=dest_lang)
    eel.view_result(trans_result.text)
