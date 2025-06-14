def get_word_number (content):
    count = 0
    for name in content:
        count += 1
    return count

def get_char_number (content_list):
    character_nums = {}
    for content in content_list:
        if content in character_nums:
             character_nums[content] += 1
        elif content not in character_nums:
            character_nums[content] = 1
    return character_nums
