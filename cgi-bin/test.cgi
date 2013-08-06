#!/usr/bin/ruby
# -*- coding: utf-8 -*

input = ENV["QUERY_STRING"]
querylength = ENV["CONTENT_LENGTH"]

username, gender, description, profile = input.split('&')

puts "Content-Language: ja, en"
puts "Content-type: text/html; charset=utf-8\n";
puts "\n";
puts "<html>\n";
puts "<body>\n";
puts "<p>I am Ruby!!!!</p>\n";
puts "<p>received: #{input}</p>"
puts "<p>#{username}</p>"
puts "<p>#{gender}</p>"
puts "<p>#{description}</p>"
puts "<p>#{profile}</p>"
puts "<p>querylength: #{querylength}</p>"
puts "</body>\n";
puts "</html>\n";
