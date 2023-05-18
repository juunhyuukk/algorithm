T = int(input())

for t in range(1, T + 1):
    memory = input().strip()
    length = len(memory)

    count = 0
    prev_bit = '0'

    for bit in memory:
        if bit != prev_bit:
            count += 1
        prev_bit = bit

    print(f"#{t} {count}")