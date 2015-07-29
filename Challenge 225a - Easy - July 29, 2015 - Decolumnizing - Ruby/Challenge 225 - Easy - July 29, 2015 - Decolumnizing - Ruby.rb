lines = []
input = File.open("input.txt", "r")
input.each_line do |line|
  lines << line
end
input.close
newString = ""
lines.each{|line|
    tempString = line
    addSpace = true
    if(tempString[tempString.length-3] == "-")
        tempString = tempString[0..tempString.length-4]
        addSpace = false
    end
    if(tempString.include? "- +")
        tempString = tempString[0..tempString.index("- +")-1]
        addSpace = false
    end
    if(tempString.include? "- |")
        tempString = tempString[0..tempString.index("- |")-1]
        addSpace = false
    end
    if(tempString.include? "+")
        if tempString.index("+") == 0
            tempString = tempString[tempString.index("-+")+3..tempString.length-1]
            addSpace = false
        else
            tempString= tempString[0..tempString.index("+-")-1]
            addSpace = false
        end
    end
    if(tempString.include? "|")
        if(tempString[0]=="|")
            tempString = tempString[tempString.index(" |")+3..tempString.length-1]
        else
            tempString = tempString[0..tempString.index(" |")-1]
        end
    end
    if(tempString[0] == " ")
        tempString = tempString.lstrip
    end
    if(tempString == "\n" or line == "\n")
        newString += "\n\n"
        addSpace = false
    end
    newString += tempString.chomp
    newString = newString.strip()
    if(addSpace)
        newString += " "
    end
}

puts newString