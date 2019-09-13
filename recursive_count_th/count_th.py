'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# set a substring to "th"
# set count = 0
# set an index = the substring using find
# if the index is >= 0
# the count is += 1
# set word = to the index + the len of substring
# increment count by calling count_th()


def count_th(word):

    substring = 'th'
    count = 0

    index = word.find(substring)
    if index >= 0:
        count += 1
        word = word[index + len(substring):]

        count += count_th(word)
    return count
