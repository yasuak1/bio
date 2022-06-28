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

        # plot data
        points = Array.new
        latest_point = [0, 0]
        ent.seq.chars.each do |amino|
            latest_point[0] += dpoints[amino][0]
            latest_point[1] += dpoints[amino][1]
            points << latest_point.dup
        end

        # disp
        points.each do |point|
            puts "#{point[0]} #{point[1]}"
        end
    end
end