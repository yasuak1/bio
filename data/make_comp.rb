require 'bio'

Bio::FlatFile.auto(ARGF) do |ff|
    str = 'ACDEFGHIKLMNPQRSTVWY'
    hash = Hash.new(0)
    str.chars.each do |c|
        hash[c] = 0
    end
    ff.each_entry do |entry|
        entry.seq.composition.each do |key, val|
            hash[key] += val
        end
    end
    hash.each do |key, val|
        puts "#{key} #{val}"
    end
end