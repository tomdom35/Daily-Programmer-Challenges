def is_palindrome(item)
	new_item = item.to_s
	for index in (0..new_item.length/2)
		if(new_item[index] != new_item[(new_item.length-1)-index])
			return false
		end
	end
	return true
end

def get_reverse(item)
	reverse_num = item.to_s.reverse
	return reverse_num.to_i
end

loop do
    print "Enter a number (or hit space to quit) :"
    original_num = gets.chomp
    if original_num == " "
        break
    end
    original_num = original_num.to_i
    num = original_num
    count = 0
    too_long = false
    while !is_palindrome(num) && !too_long
    	reverse_num = get_reverse(num)
    	puts "#{num} is not palindromic"
        puts "#{num} + #{reverse_num} = #{num + reverse_num}"
    	num = num + reverse_num
    	count+=1
    	if count == 1000
    	    too_long = true
    	end
    end
    if too_long
        puts "#{original_num} could not become palindromic after #{count} steps"
    else
        puts "#{original_num} gets palindromic after #{count} steps"
    end
end