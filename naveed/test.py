# Complete the function below.

def alternate_operations(n):
    # your code
    a = []
    for i in range(n + 1):
        if i == 0:
            pass
        else:
            a.append(i)
    result = 0
    for i in a:
        try:
            if i:
                result = result + i
            try:
                if (i + 1):
                    result = result + (i + 1)
                    print result
                try:
                    if (i + 2):
                        result = result * (i + 2)

                    try:
                        if (i + 3):
                            result = result - (i + 3)

                    except:
                        break
                except:
                    break
            except:
                break

        except:
            break
        i = i + 4

    return result