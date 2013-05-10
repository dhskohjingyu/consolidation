import datetime

def quick_sort(a):
    if a == []:
        return []
    else:
        p = a[0]
        l, g = [], []

        for value in a[1::]:
            if value < p:
                l.append(value)
            else:
                g.append(value)

        return quick_sort(l) + [p] + quick_sort(g)

def write_to_file(values):
    try:
        infile = open("serial.DAT", "w")

        # sort values and write sorted values
        values = quick_sort(values)

        for i in range(0, len(values)):
            infile.write(values[i] + "\n")

        print("Successfully wrote to serial.DAT")
        
        infile.close
    except IOError:
        print("Error writing to serial.DAT")

def get_value():
    value = input("Enter a value to write to file (enter nothing if you want to stop): ")

    if value:
        return value
    else:
        return None


values = []
value = get_value()

while value:
    values.append(value)
    value = get_value()

write_to_file(values)
