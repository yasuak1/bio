require 'bio'

Bio::FlatFile.auto(ARGF) do |ff|
    ff.each_entry do |ent|
        p ent.definition
        p ent.seq.length
        puts "=== seq composition ==="
        ent.seq.composition.each do |key, val|
            puts "#{key} : #{val}"
        end
        #disp ent
    end
end