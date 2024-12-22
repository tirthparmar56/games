def fizz_buzz(answer:int) -> str :
    """the number is ranging from 1 to 100,
        if the number is divisible by 3 , the returned result will be fizz , if the number is divisible by 5, the
        returned result will be buzz, if the retured result is divisible by both, the returned result will be fizz buzz
        else it will return the number itself"""
    print("{}: write fizz, buzz, fizz and buzz or number itself = ".format(answer),end='')
    while True:
        if answer%3==0:
            if answer%5==0:
                result="fizz buzz"
            else:
                result="fizz"
        elif answer%5==0:
            result="buzz"
        else:
            result=str(answer)
        if answer%2!=0:
            user_input=str(input())
            if user_input!=result:
                return "game over"
        else:
            print(result)

        return str(result)

for i in range(1,101):
    number=fizz_buzz(i)
    if number=="game over":
        break
print("game over")
