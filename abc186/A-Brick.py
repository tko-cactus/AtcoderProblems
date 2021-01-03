def main(cap, kg):
	return cap // kg

if __name__ == '__main__':
	n, w = map((lambda x: int(x)), input().split())
	print(main(n, w))