


ENCODE, DECODE = 0, 1

def EncodingManager(Func: callable, Op: int) -> str:
	assert Op in {
		0,
		1,
	}, f'This Operation is not NotImplemented or incorrect!, index [{Op}]'
	if Op == ENCODE:
		def Func_(s: str | bytes):
			assert isinstance(
				s, (str, bytes)
			), f"This function can not encode {str(type(s))} Object"
			if isinstance(s, str):
				s = s.encode()
			return Func(s).decode()

	elif Op == DECODE:
		def Func_(s: str | bytes):
			assert isinstance(
				s, str
			), f"This function can not encode {str(type(s))} Object"
			return Func(s).decode()

	return Func_
