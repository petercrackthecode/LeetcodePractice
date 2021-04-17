const removeDuplicates = (S, K) => {
	let SC = s.split(""), st = [0], i, j;
	for (i = 1, j = 1; j < S.length; SC[++i] = SC[++j])	{
		if (SC[i] !== SC[i-1])
			st.push(i);
		else if (i - st[st.length - 1] + 1 === K)
			i = st.pop() - 1;
	}

	return SC.slice(0, i + 1).join("");
}