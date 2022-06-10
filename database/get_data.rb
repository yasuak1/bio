require 'bio'

gets.chomp.split.each do |accession_number|
    ent =  getent("genbank:#{accession_number}") 
    savefile "#{accession_number}.gbk", ent
end
