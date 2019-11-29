try:
    h=eval(input())
    print(10/h)
except EOFError as e:
    print('EOF end of file error')
except ValueError as e:
    print('value not valid error')
except(ZeroDivisionError,TypeError,AttributeError) as e:
    print('unknown error ',e)
finally:
    print('done')
