#!/usr/bin/env ruby
# -*- coding: utf-8 -*

require 'cgi'
input = ENV["QUERY_STRING"]
contentlength = ENV["CONTENT_LENGTH"]

parsed = input.split('&')

puts "Content-Language: ja, en"
puts "Content-type: text/html; charset=utf-8\n";
puts "\n";
puts "<html>\n";
puts "<body>\n";
puts "<p>I am Ruby!!!!</p>\n";
puts "<p>received: #{CGI.unescape(input)}</p>"
parsed.each do |i|
  field = i.slice!(/^.+?=/)
  puts "<p>#{field.chop}: #{CGI.unescape(i)}</p>"
end

puts "<p>contentlength: #{contentlength}</p>"
puts "</body>\n";
puts "</html>\n";