def merge_the_tools(string, k):

    Substrings = int(len(string) / k)

    counter = 0

    for i in range(Substrings):
        Substring = string[counter : counter + k]
        counter += k

        check = []
        for char in Substring:
            if char not in check:
                check.append(char)

        print("".join(check))
        check = []


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
