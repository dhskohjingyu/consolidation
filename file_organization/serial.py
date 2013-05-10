import datetime

def write_to_file(values):
    try:
        infile = open("sequential.DAT", "a")
        
        for value in values:
            infile.write(value + "\n")

        print("Successfully wrote values to sequential.DAT")

        infile.close
    except IOError:
        print("Error writing to sequential.DAT")

def get_value():
    value = input("Enter a value to write to file (enter nothing if you want to stop): ")

    now = datetime.datetime.now()
    time = now.strftime('%d-%m-%Y %H:%m:%S')
    
    if value:
        return time + ": " + value
    else:
        return None


values = []
value = get_value()

while value:
    values.append(value)
    value = get_value()

write_to_file(values)
