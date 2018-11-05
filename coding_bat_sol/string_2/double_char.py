# def double_char(mot):
#     duplicate = ""
#     for i in mot:
#         duplicate += i * 2
#     return duplicate


def double_char(mot):
    duplicate = ""
    for i in range(len(mot)):
        duplicate += mot[i] + mot[i]
    return duplicate