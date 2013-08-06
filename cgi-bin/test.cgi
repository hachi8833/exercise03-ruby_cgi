#!/usr/bin/env ruby
# -*- coding: utf-8 -*

require 'cgi'
input = ENV["QUERY_STRING"]
contentlength = ENV["CONTENT_LENGTH"]

email, reason, x, y, profile = input.split('&').map {|i| i.gsub(/^.*?=/, "")}

puts "Content-Language: ja, en"
puts "Content-type: text/html; charset=utf-8\n";
puts "\n";
puts "<html>\n";
puts "<body>\n";
puts "<p>I am Ruby!!!!</p>\n";
puts "<p>received: #{CGI.unescape(input)}</p>"
puts "<p>email: #{CGI.unescape(email)}</p>"
puts "<p>reason: #{CGI.unescape(reason)}</p>"
puts "<p>x-y coordinate: #{CGI.unescape(x)}, #{CGI.unescape(y)}</p>"
puts "<p>profile: #{CGI.unescape(profile)}</p>"
puts "<p>contentlength: #{contentlength}</p>"
puts "</body>\n";
puts "</html>\n";