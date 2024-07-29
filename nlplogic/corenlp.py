from textblob import TextBlob
import wikipedia


def search_wikipediia(name):
    """Search wikipedia"""
    # print(f'Searching for {name} on Wikipedia')
    return wikipedia.summary(name)


def summarize_wikipedia(name, length=1):
    """Summarize Wikipedia"""
    # print(f'Finding Wikipedia summary for {name}')
    return wikipedia.summary(name, length)


def get_textblob(text):
    """Get textblob from text"""
    # print(f'Getting textblob for {text}')
    return TextBlob(text)


def get_phrases(text):
    """Get phrases from text"""
    # print(f'Getting phrases for {text}')
    return get_textblob(text).noun_phrases
