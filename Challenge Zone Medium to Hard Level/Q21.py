"""
Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.
Range - Number of notes(n) : n (1 = n = 1000000).
"""

def count_notes(amount):
    notes=[500,200,100,50,20,10]
    note_count={}

    for note in notes:
        count=amount//note
        if count>0:
            note_count[note]=count
            amount%=note

    return note_count

print(count_notes(1700))