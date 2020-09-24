import random
import nltk


BOT_CONFIG = {
    'intents': {
        
        'hello': {
            'examples': ['Привет', 'Здравствуй', 'Хай', 'Добрый день', 'Йоу', 'Хеллоу'],
            'responses': ['Привет!', 'Привет, рад, что ты тут', 'Здравствуй, дитя человеческое']
        },
        'bye': {
            'examples': ['Пока', 'Прощай', 'До свидания', 'До скорого'],
            'responses': ['Жду твоего возвращения', 'Надеюсь, ты скоро вернешься', 'Пока. Жду тебя']
        },
        'thanks': {
            'examples': ['Спасибо', 'Благодарю', 'Большое спасибо', 'Дякую'],
            'responses': ['Рад помочь', 'Всегда пожалуйста', 'Пожалуйста!', 'Обращайся', 'Не за что!']
        },
        'rest1': {
            'examples': ['Отпуск', 'Хочу отпуск', 'Я бы сейчас поехал в отпуск'],
            'responses': ['Я тоже хочу отдохнуть', 'Если поедешь отдыхать, возьми меня с собой', 'Отпуск - это запретный плод']
        },
        'rest2': {
            'examples': ['Куда поехать', 'Где можно отдохнуть', 'Какое место для отдыха посоветуешь?'],
            'responses': ['Всегда можно поехать в Одессу', 'Я бы рванул в Италию!', 'Уверен, на островах тебе понравится', 'В Норвегии есть много красивых мест!']
        },
        'rest3': {
            'examples': ['Хочу отдохнуть', 'Много работы', 'Нужен отдых', 'Я устал', 'Время отдохнуть', 'Я очень устал'], 
            'responses': ['Тебе стоит посмотреть фильм', 'Я слышал, что чай может помочь', 'Тебе действительно нужен перерыв, сходи в парк', 'Поесть и поспать - лучшее решение!']
        },
        'movie': {
            'examples': ['Какой фильм посмотреть', 'Какой фильм посоветуешь', 'Посоветуй фильм', 'Какое кино глянуть', 'Порекомендуй фильм', 'Фильм на вечер'], 
            'responses': ['Посмотри "Джентельмены"', 'Я не очень люблю фильмы, выбирай сам', '"Кролик ДжоДжо" - замечательный фильм', 'Смотри все фильмы Нолана', 'Новый фильм "Довод"']
        }
        
    },
    
    'failure_phrases': [
        'Не понимаю',
        'Пожалуйста, перефразируй',
        'Извини, я бот, я не понимаю'
    ]
    
}

def clear_text(text): # clears the text of characters that can interfere with understanding the request
    text = text.lower()
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789- '
    result = ''
    for char in text:
        if char in alphabet:
            result += char
    return result

def get_intent(text):
    text = clear_text(text)

    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            example = clear_text(example)
            if example:
                distance = nltk.edit_distance(text, example)
                if distance / len(example) < 0.4:
                    return intent
            

def get_response_by_intent(intent):
    phrases = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(phrases)

def get_response_generator(text):
    return

def get_failure_phrase():
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases)

def bot(request):
    # NLU 
    intent = get_intent(request)
    
    # Response generator
    if intent:
        return get_response_by_intent(intent)
    
    response = get_response_generator(request)
    if response:
        return response
    
    return get_failure_phrase()
