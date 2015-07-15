def garland(word)
	repeat = ""
	count = word.count(word[0])
	if(count > 1)
		second = 1 
		while(second<word.length && count>1)
		    count -= 1
		    second = word.index(word[0],second)+1
		    first = 1
		    repeat = word[0]
		    while(second<word.length)
			    if(word[first] == word[second])
				    repeat += word[first]
				    first += 1
				    second += 1
			    else
				    repeat = ""
				    break
			    end
		    end
	    end
	end
	return repeat.length
end

word = "abracadabra"
puts garland(word)