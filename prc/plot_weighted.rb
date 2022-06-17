require 'bio'

Bio::FlatFile.auto(ARGF) do |ff|
    dpoints = Hash.new(0)
    ff.each_entry do |ent|
        # define amino vector
        arg = 0
        darg = 360 / ent.seq.chars.uniq.size
        ent.seq.chars.uniq.sort.each do |amino|
            x = Math.cos(arg / 180.0 * Math::PI)
            y = Math.sin(arg / 180.0 * Math::PI)
            dpoints[amino] = [x, y]
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
            amino_weight[key] = - Math.log( val.to_f / lseq )
        end

        # plot data and disp
        latest_point = [0, 0]
        ent.seq.chars.each do |amino|
            latest_point[0] += amino_weight[amino] * dpoints[amino][0]
            latest_point[1] += amino_weight[amino] * dpoints[amino][1]
            puts "#{latest_point[0]} #{latest_point[1]}"
        end
    end
end