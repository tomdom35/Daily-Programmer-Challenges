def create_num_word(word)
	scale = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	num_word = []
	word.each_char {|c| num_word << scale.index(c)+1}
	return num_word
end
def is_balanced(word, num_word)
	for i in 1..num_word.length-2
		left_weight = 0
		right_weight = 0
		left_set = ""
		right_set = ""
		for j in 0..i-1
			left_set += word[j]
			left_weight += (i-j)*num_word[j]
		end
		for k in i+1..word.length-1
			right_set += word[k]
			right_weight += (k-i)*num_word[k]
		end
		if(left_weight == right_weight)
			print left_set, " ", word[i], " ", right_set, " - #{left_weight}"
			return true
		end
	end
	return false
end
word = "UNINTELLIGIBILITY"
num_word = create_num_word(word)
if(!is_balanced(word,num_word))
    print word, " DOES NOT BALANCE"
end