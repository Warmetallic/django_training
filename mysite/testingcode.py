
def test(text):
    result = text.split("ness")[0]

    if(result.endswith("i")):
        return result[:-1] + 'y'
    else:
        return result


print(test("heaviness"))