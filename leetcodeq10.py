from collections import Counter


def permuteUnique(nums):
    lst = []
    counter = Counter(nums)
    print("counter = ", counter)
    if len(nums) == 1:
        return nums

    def permute(templst):
        print("FUNCTION BEGIN %%%%%%%%%%%%%%%%%%%\n")
        print("if len(templst) == len(nums):")

        if len(templst) == len(nums):
            print("True \n")
            lst.append(templst)
            print("lst = ", lst)
            print("return xxxxxx")
            return
        else:

        print(">>>For loop begin @@")
        for key in counter:
            print("key = ", key)
            print("counter[key]", counter[key])
            print("\nif counter[key]:")
            if counter[key]:
                print("True \n")
                counter[key] -= 1
                print("decrement counter for key = ", counter[key], key)
                print("counter[key] = ", counter[key])
                print("\ncounter = ", counter)
                print("\nCall function again ---")
                print("templst = ", templst)
                print("key = ", key)
                print("templst + [key] = ", templst + [key])
                permute(templst + [key])
                print("\nIncrement counter[key]")
                counter[key] += 1
                print("counter[key] = ", counter[key])
            else:
                print("False \n")

    permute([])

    return lst


nums = [1, 1, 2]
print("Final = ", permuteUnique(nums))
