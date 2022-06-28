File.open('/home/yasu/data/COG-100-2892/dataset0/train.txt', 'r').each_line do |line|
    key, arry = line.chomp.split("\t")
end