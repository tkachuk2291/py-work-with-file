def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open("test.txt", "r") as file_read:
        lines = file_read.readlines()
    for line in lines:
        action, amount = line.strip().split(",")
        amount = int(amount)
        if action == "supply":
            supply += amount
        elif action == "buy":
            buy += amount
    result = supply - buy
    print(f"sup , {supply},buy, {buy} ,result, {result}")
    with open("test_name.txt", "w") as file_write:
        file_write.write(f"supply,{supply}\n")
        file_write.write(f"buy,{buy}\n")
        file_write.write(f"result,{result}\n")
