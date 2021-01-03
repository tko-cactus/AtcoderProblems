# def main(h, w, matrix):
# 	print(h, w, matrix)

if __name__ == '__main__':
	h, w = map((lambda x: int(x)), input().split(" "))
	matrix = [list(map(int, input().split(" "))) for i in range(w)]
	print(matrix)
