# counters
boxes = 0
remaining_candles = 0

candles = 24

for age in range(1, 101):  # loop through age
    candles_need = age  # how many candles for birthday
    if remaining_candles >= candles_need:  # chech remaining candles
        remaining_candles -= candles_need
    else:  # buy new boxes
        boxes_to_buy = (candles_need - remaining_candles + candles - 1) // candles  # dont know how to break lines without breaking code
        boxes += boxes_to_buy
        remaining_candles = boxes_to_buy * candles - (candles_need - remaining_candles)
    # programe start
    print(f"Before birthday {age}, buy {boxes_to_buy} box(es)")
# total number of boxes and remaining candles print
print(f"\nTotal number of boxes: {boxes}, Remaining candles: {remaining_candles}")