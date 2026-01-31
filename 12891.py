S, P = map(int, input().split())
char = input()
A, C, G, T = map(int, input().split())
dic = {'A':0, 'C':0, 'G':0, 'T':0}
start_index = 0
end_index = P-1
count = 0

slice = char[0:P]
dic['A'], dic['C'], dic['G'], dic['T'] = slice.count('A'), slice.count('C'), slice.count('G'), slice.count('T')

while end_index != S:
    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        count += 1
        dic[char[start_index]] -= 1
        start_index += 1
        end_index += 1
        if end_index < S:
            dic[char[end_index]] += 1
        else:
            break
    else:
        dic[char[start_index]] -= 1
        start_index += 1
        end_index += 1
        if end_index < S:
            dic[char[end_index]] += 1
        else:
            break

print(count)