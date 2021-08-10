# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen

def merge_the_tools(string, k):
    chunk_size = int(len(string) / (len(string) / k))
    chunks_list = [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]
    for i in range(len(chunks_list)):
        chunk = chunks_list[i]
        element_string = ""
        for element in range(len(chunk)):
            if chunk[element] not in element_string:
                element_string += chunk[element]
        print(element_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)