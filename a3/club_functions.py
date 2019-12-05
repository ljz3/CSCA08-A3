"""Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file.

    NOTE: Functions (including helper functions) that have a parameter
          of type TextIO do not need docstring examples.

    """
    contents = profiles_file.readlines()
    person_to_friends = {}
    person_to_clubs = {}
    
    current_profile = ""

    for i in range(len(contents)):
        if i == 0 or contents[i - 1] == "\n":
            current_profile = contents[i][:contents[i].index(",")]\
                + contents[i][contents[i].index(",") + 1:-1]
            continue
        elif contents[i] == "\n":
            continue
        if "," in contents[i]:
            if current_profile not in person_to_friends:
                person_to_friends[current_profile] = []
            person_to_friends[current_profile].append(contents[i][:contents[i]\
                .index(",")] + contents[i][contents[i].index(",") + 1:-1])
        else:
            if current_profile not in person_to_clubs:
                person_to_clubs[current_profile] = []
            person_to_clubs[current_profile].append(contents[i][:-1])
        
    return (person_to_friends, person_to_clubs)


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6

    """
    total_clubs = 0

    for person in person_to_clubs:
        total_clubs += len(person_to_clubs[person])

    if not len(person_to_clubs) == 0:
        return total_clubs / len(person_to_clubs)
    else:
        return 0


def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people
    from the "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True

    """
    first_to_last = {}
    
    for person in person_to_friends:
        for friend in person_to_friends[person]:
            first = friend[:friend.rfind(" ")]
            last = friend[friend.rfind(" ") + 1:]
            if last not in first_to_last:
                first_to_last[last] = []
            if first not in first_to_last[last]:
                first_to_last[last].append(first)
        first = person[:person.rfind(" ")]
        last = person[person.rfind(" ") + 1:]
        if last not in first_to_last:
            first_to_last[last] = []
        if first not in first_to_last[last]:
            first_to_last[last].append(first)

    for last in first_to_last:
        first_to_last[last].sort()

    return first_to_last



def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    """
    inverted = {}
    for key in key_to_value:
        if type(key_to_value[key]) is list:
            for value in key_to_value[key]:
                if value not in inverted:
                    inverted[value] = []
                inverted[value].append(key)
            for inv_key in inverted:
                inverted[inv_key].sort()
        else:
            if key_to_value[key] not in inverted:
                inverted[key_to_value[key]] = []
            inverted[key_to_value[key]].append(key)

    return inverted


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']

    """
    clubs = []
    already_in = []
    if person in person_to_clubs:
        for club in person_to_clubs[person]:
            already_in.append(club)

    for friend in person_to_friends[person]:
        if friend in person_to_clubs:
            for club in person_to_clubs[friend]:
                if club not in already_in:
                    clubs.append(club)

    clubs.sort()
    return clubs


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]

    """
    clubs = {}
    for club in get_clubs_of_friends(
            person_to_friends, person_to_clubs, person):
        
        if club not in clubs:
            clubs[club] = [0]
        clubs[club][0] += 1

    if person in person_to_clubs:
        for club in person_to_clubs[person]:
            for member in invert_and_sort(person_to_clubs)[club]:
                clubs = add_clubs_not_repeating(
                    person_to_clubs, clubs, member, person)
    
    return convert_dict_to_tup_list(clubs)


def convert_dict_to_tup_list(
        clubs: Dict[str, List[int]]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples using the contents from clubs.
    
    >>> convert_dict_to_tup_list({'Comics R Us': [2], 'Smash Club': [1]})
    [('Comics R Us', 2), ('Smash Club', 1)]
    """
    list_of_tuple = []
    list_of_nums = []
    inverted = invert_and_sort(clubs)

    for key in inverted:
        list_of_nums.append((key))

    for num in list_of_nums:
        for key in inverted:
            if key == num:
                for club in inverted[key]:
                    list_of_tuple.append((club, key))

    return list_of_tuple


def add_clubs_not_repeating(
        person_to_clubs: Dict[str, List[str]],
        clubs: Dict[str, List[str]],
        member: str, person: str) -> Dict[str, List[str]]:

    """
    Returns clubs with each club of member with a 
    point added if person is not in the club already.
    The list of which clubs that person and member is
    in is called person_to_clubs

    >>> add_clubs_not_repeating(P2C, {'Comics R Us': [1]}, Danny R Tanner, Jesse Katsopolis)
    {'Comics R Us': [1]}
    """
    list_of_common_clubs = []
    if member not in list_of_common_clubs:
        for member_club in person_to_clubs[member]:
            if member_club not in person_to_clubs[person]:
                if member_club not in clubs:
                    clubs[member_club] = [0]
                clubs[member_club][0] += 1
    return clubs


if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()