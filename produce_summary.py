def get_delivery_log(day_number, path):

    print("Day", day_number)
    delivery_log = open(path)

    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print(f"Delivered {count} {melon}s for total of ${amount}")

    delivery_log.close()

get_delivery_log(1, "um-deliveries-20140519.txt")
get_delivery_log(2, "um-deliveries-20140520.txt")
get_delivery_log(3, "um-deliveries-20140521.txt")
