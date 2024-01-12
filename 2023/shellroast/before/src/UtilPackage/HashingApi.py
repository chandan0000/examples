def Hasher(HashingFunc: callable, s: str | bytes) -> str:
	assert isinstance(
		s, (str, bytes)
	), f"This function can not hash a {str(type(s))} object"	

	if isinstance(s, str):
		s = s.encode()

	return HashingFunc(s).hexdigest()

