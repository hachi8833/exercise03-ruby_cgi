#!/usr/bin/env ruby
# -*- coding: utf-8 -*

input = ENV["QUERY_STRING"]
contentlength = ENV["CONTENT_LENGTH"]

username, gender, description, profile = input.split('&').map {|i| i.gsub(/^.*?=/, "")}

puts "Content-Language: ja, en"
puts "Content-type: text/html; charset=utf-8\n";
puts "\n";
puts "<html>\n";
puts "<body>\n";
puts "<p>I am Ruby!!!!</p>\n";
puts "<p>received: #{input}</p>"
puts "<p>username: #{username}</p>"
puts "<p>gender: #{gender}</p>"
puts "<p>description: #{description}</p>"
puts "<p>profile: #{profile}</p>"
puts "<p>contentlength: #{contentlength}</p>"
puts "</body>\n";
puts "</html>\n";
