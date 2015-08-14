def find(x,y,point,condition)
	num,change,direction,move,location = 1,1,0,0,[point]
	while((point != [x,y] && condition) || (num<x && !condition))
		move,num,location = move+1, num+1, location << point = direction==0 ? [point[0]+1,point[1]] : direction==1 ? [point[0],point[1]-1] : direction==2 ? [point[0]-1,point[1]] : [point[0],point[1]+1]
		if(move==change)
			change, direction, move = (direction==1 || direction == 3) ? change+1 : change, (direction==3) ? 0 : direction+1, 0
		end
	end
	return val = condition ? num.to_s : location[num-1].to_s
end
midPoint = ((size = ((((file = File.open("spiral input.txt")).gets).to_i)))/2) + 1
puts val = (line = file.gets.split(' ')).length>1 ? find(line[0].to_i, line[1].to_i, [midPoint,midPoint], true) : find(line[0].to_i, line[1].to_i, [midPoint,midPoint], false)