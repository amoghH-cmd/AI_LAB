

rooms = {
    'A': 'Dirty',
    'B': 'Dirty',
    'C': 'Dirty',
    'D': 'Dirty'
}

def vacuum_cleaner():
    current_room = 'A'

    print("Initial Room Status:", rooms)

    for room in rooms:
        current_room = room

        print("\nVacuum Cleaner is in Room:", current_room)

        if rooms[current_room] == 'Dirty':
            print("Room is Dirty. Cleaning...")
            rooms[current_room] = 'Clean'
        else:
            print("Room is already Clean.")

        print("Room Status:", rooms)

    print("\nAll Rooms Cleaned!")
    print("Final Room Status:", rooms)


vacuum_cleaner()