puts "input a list of accessions"
gets.chomp.split.each do |accession|
    ent = getent("genbank:#{accession}")
    savefile "data/#{accession}.fasta", ent
end