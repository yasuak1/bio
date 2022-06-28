require 'bio'

Bio::FlatFile.auto(ARGF) do |ff|
    cnt = 0
    hash = Hash.new(0)
    ff.each_entry do |entry|
        entry.seq.composition.each do |key, val|
            key = Bio::Sequence::AA.new(key)
            hash[key] += val
            cnt += val
        end
    end
    hash = hash.sort_by{|_, v| -v}.to_h
    p cnt
    p hash
    puts "================================"
    puts "amino\t acid\t cnt\t %"
    hash.each do |key, val|
        puts "#{key.codes}\t #{key}\t #{val}\t #{(val.to_f/cnt*100).to_i}"
    end
    puts "================================"
end