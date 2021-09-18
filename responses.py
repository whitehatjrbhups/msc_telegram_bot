def sample_responses(input_text):
    user_message = str(input_text).lower()

    if '#' in user_message:
        k = user_message + ' '
        hash = k[k.find('#') + 1:k.find(' ', k.find('#'))]
        if hash.lower() == 'help':
            m=""
        else:
            m = '''Looks like you tried a wrong command!
click /help to get started.'''
            return m

    # return input_text
    return ""
