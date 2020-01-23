import logging

def meetsCriteria(password:str, part2 = False):
    logging.debug('-------------------------------------------')
    logging.debug('Started criteria checking...')
    if sorted(list(password)) != list(password):
        logging.debug(f'Password does NOT meet criteria of only increasing digits: {password}')
        return False

    foundTwoAdjacentDigits = False
    foundTwoDigits = False
    for i in range(len(password)-1):
        if password.count(password[i]) == 2:
            foundTwoDigits = True

        if password[i] != password[i+1]:
            continue
        else:
            foundTwoAdjacentDigits = True
    
    if part2 and not foundTwoDigits:
        return False

    if not foundTwoAdjacentDigits:
        logging.debug(f'Password does NOT meet criteria of two adjacent digits: {password}')
        return False
    
    return True
    
def test():
    logging.basicConfig(level=logging.DEBUG)
    assert meetsCriteria('111111') == True
    assert meetsCriteria('223450') == False
    assert meetsCriteria('123789') == False
    assert meetsCriteria('112233', part2=True) == True
    assert meetsCriteria('123444', part2=True) == False
    assert meetsCriteria('111122', part2=True) == True

# test()
RANGE_MIN = 357253
RANGE_MAX = 892942

part1 = 0
part2 = 0
for i in range(RANGE_MIN, RANGE_MAX):
    if meetsCriteria(str(i)):
        part1 += 1

    if meetsCriteria(str(i), part2=True):
        part2 += 1
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
