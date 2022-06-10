require 'bio'

puts "input a list of accession number."
gets.chomp.split("、").each do |accession_number|
    gb = getobj("genbank:#{accession_number}")
    puts "=== #{accession_number} ==="
    p gb.definition
    p gb.seq.length
    p gb.seq.composition
end
