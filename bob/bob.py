def hey(phrase):
    if isSilence(phrase):
        return "Fine. Be that way!"
    elif isShouted(phrase) and isQuestion(phrase):
        return "Calm down, I know what I'm doing!"
    elif isShouted(phrase):
        return "Whoa, chill out!"
    elif isQuestion(phrase):
        return "Sure."
    else:
        return "Whatever."


def isSilence(phrase):
    return phrase == "" or phrase.isspace()


def isShouted(phrase):
    return phrase.strip().isupper()


def isQuestion(phrase):
    return phrase.strip().endswith("?")
