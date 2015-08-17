def ordered(word)
	for i in 0..word.length-2
		if(word[i]>word[i+1])
			return false
		end
	end
	puts(word + " IN ORDER")
	return true
end
def reverse(word)
	for i in 0..word.length-2
		if(word[i]<word[i+1])
			puts(word + " NOT IN ORDER")
			return false
		end
	end
	puts(word + " REVERSE ORDER")
	return true
end
File.open("input.txt") do |f|
	f.each_line do |word|
		if(!ordered(word.chomp))
			reverse(word.chomp)
		end
	end
end