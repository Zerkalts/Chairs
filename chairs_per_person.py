f = open("reservations")

List = []
for reservation in f:
    name, number = reservation.split(",")
    try :
        chairs_per_person = 50 / int(number)
    except ValueError:
        if number.strip("\n") not in List:
            List.append(number.strip("\n"))
        pass
    except ZeroDivisionError:
        if number.strip("\n") not in List:
            List.append(number.strip("\n"))
        pass

    print("{} will get {} chairs per person".format(name, chairs_per_person))
print(List)
