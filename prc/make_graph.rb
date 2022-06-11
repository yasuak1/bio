require 'bio'

Bio::FlatFile.auto(ARGF) do |ff|
    dpoint = Hash.new(0)
    ff.each_entry do |ent|
        arg = 0
        darg = 360 / ent.seq.chars.uniq.size
        ent.seq.chars.uniq.sort.each do |amino|
            x = Math.cos(arg / 180.0 * Math::PI)
            y = Math.sin(arg / 180.0 * Math::PI)
            dpoint[amino] = [x, y]
            arg += darg
        end

        points = Array.new
        points << [0, 0]
        ent.seq.chars.each do |amino|
            point = points[-1].dup
            point.each_with_index do |val ,index|
                point[index] += dpoint[amino][index] 
            end
            points << point
        end
        points.each do |point|
            puts "#{point[0]} #{point[-1]}"
        end
    end
=begin
    amino_vec.each do |key, val|
        puts "#{val[0]} #{val[-1]}"
    end
=end
end