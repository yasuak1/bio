require 'bio'

Bio::FlatFile.auto(ARGF) do |ff|
    dpoint = Hash.new(0)
    ff.each_entry do |ent|
        # define amino vector
        arg = 0
        darg = 360 / ent.seq.chars.uniq.size
        ent.seq.chars.uniq.sort.each do |amino|
            x = Math.cos(arg / 180.0 * Math::PI)
            y = Math.sin(arg / 180.0 * Math::PI)
            dpoint[amino] = [x, y]
            arg += darg
        end

        # define amino weight
        cnt_amino = Hash.new(0)
        amino_weight = Hash.new(0)
        lseq = 0
        File.open("../data/composition.dat", mode = "rt") do |f|
            f.each_line do |line|
                amino, cnt = line.split
                cnt_amino[amino] = cnt
                lseq += cnt.to_i
            end
        end
        cnt_amino.each do |key, val|
            amino_weight[key] = val.to_f / lseq
        end
=begin
        lseq = ent.seq.length
        ent.seq.composition.each do |key, val|
            #amino_weight[key] = -Math.log(val.to_f / lseq, 2)
            amino_weight[key] = val.to_f / lseq
        end
        #p amino_weight
=end
        # plot data
        INF = (1 << 21)
        x_range = [INF, -INF]
        y_range = [INF, -INF]
        multiply_wight = true
        points = Array.new
        points << [0, 0]
        ent.seq.chars.each do |amino|
            point = points[-1].dup
            point.each_with_index do |val ,index|
                point[index] += multiply_wight ? dpoint[amino][index] * amino_weight[amino] : dpoint[amino][index] 
                x_range[0] = [x_range[0], point[0]].min
                x_range[-1] = [x_range[-1], point[0]].max
                y_range[0] = [y_range[0], point[-1]].min
                y_range[-1] = [y_range[-1], point[-1]].max
            end
            points << point
        end
        points.each do |point|
            puts "#{point[0]} #{point[-1]}"
        end

        puts "# set range"
        x_range.map!{|val| (val * 1.1).round(2)}
        y_range.map!{|val| (val * 1.1).round(2)}
        puts "# x [#{x_range[0]}, #{x_range[-1]}]"
        puts "# y [#{y_range[0]}, #{y_range[-1]}]"
    end
=begin
    amino_vec.each do |key, val|
        puts "#{val[0]} #{val[-1]}"
    end
=end
end