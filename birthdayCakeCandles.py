def birthdayCakeCandles(q, candles: list):
    
    max_candle = max(candles)
    
    print(candles.count(max_candle))
    

birthdayCakeCandles(int(input()),[int(x) for x in input().split()])
    