#!/usr/bin/env ruby
# -*- coding: utf-8 -*
puts "Content-Language: ja, en"
puts "Content-type: text/html; charset=utf-8\n\n";

require 'cgi'
require 'pstore'

#デバッグ用
def error_cgi
  puts "Content-type: text/html; charset=utf-8\n\n";
  puts "<p>*** CGI Error List ***</p>"
  puts "<p>#{VERSION}</p>"
  puts "<p>#{CGI.escapeHTML($!.inspect)}</p>"
  $@.each {|x| puts "<p>", CGI.escapeHTML(x), "</p>"}
end

begin
  timestamp = Time.now.strftime("%Y%m%d%H%M%S").to_s

  cgi = CGI.new
  param         = cgi.params
  value         = cgi.params['upload'][0]
  filename      = value.original_filename
  filecontents  = value.read
  email         = cgi.params['email'].to_s
  reason        = cgi.params['reason'].to_s

  puts <<EOM
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>|採用| BPS株式会社</title>
  <link rel="stylesheet" media="screen" href="../sample.css">
  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>
  <![endif]-->
  <script type="text/javascript" src="../script/jquery-2.0.3.min.js"></script>
  <script type="text/javascript" src="../script/sample.js"></script>
    <script type="text/javascript" src="../script/samplejquery.js"></script>
</head>
<body>
  <div class="headpattern"></div>
  <div id="shell">
    <header>
      <div id="headline">
        <div id="logo" class="hover">
          <img src="../images/logo.png" height="80" width="250" alt="logo">
        </div>
        <div id="topmenu">
          <nav>
            <ul class="menu">
              <li class="button" id="list1"><a class="button" href="/">
                <div class="first">トップページ</div>
                <div class="second">Top page</div></a>
              </li>
              <li class="button" id="list2"><a class="button" href="/">
                <div class="first">実績</div>
                <div class="second">Works</div></a>
              </li>
              <li class="button" id="list3"><a class="button" href="/">
                <div class="first">サービス紹介</div>
                <div class="second">Service</div></a>
              </li>
              <li class="button" id="list4"><a class="button" href="/">
                <div class="first">会社案内</div>
                <div class="second">Company</div></a>
              </li>
              <li class="button" id="list5"><a class="button" href="/">
                <div class="first">お問い合わせ</div>
                <div class="second">Contact</div></a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <div class="clear"><hr /></div>
    </header>
EOM

  puts "<section>\n";
  puts "<div class='exterior'>\n";
  puts "<p>I am Ruby!!!! Version: #{VERSION}</p>\n";

  puts "<p>timestamp: #{timestamp}<p>"
  puts "<p>current directory: #{Dir::pwd}<p>"
  puts "<p>cgi_keys: #{cgi.keys}<p>"
  puts "<p>has_keys? #{cgi.has_key?('email')}</p>"
  puts "<p>include? #{cgi.include?('email')}</p>"
  puts "<p>param: #{param['email']}</p>"
  puts "<p>email: #{email}</p>"
  puts "<p>reason: #{reason}</p>"
  puts "<p>filename: #{filename}</p>"
  puts "<p>value: #{filecontents}</p>"

  puts "<p>I am Ruby!!!!</p>\n";

  # Dir::chdir("../received")
  # Dir::mkdir(timestamp)
  # theProfile = []
  # theProfile << email.to_s
  # theProfile << reason.to_s
  # path = timestamp + "/"
  # File.open(path + "profile.txt", "w") {|f| f.write theProfile}
  # File.open(path + filename, "wb") {|f| f.write filecontents.to_s}

  puts "</div>\n";
  puts "</section>\n";
  puts "</body>\n";
  puts "</html>\n";
puts <<EOM
<div class="footpattern">
  <div id="copyright" class="floatleft">
    COPYRIGHT (C) BEYOND PERSPECTIVE SOLUTIONS LTD. ALL RIGHTS RESERVED.
  </div>
  <div class="floatleft">
    <ul id="backtotop">
      <li class="button"><a href="">ページの先頭へ</a></li>
    </ul>
  </div>
</div>
<div class="clear"><hr /></div>
</body>
</html>
EOM
rescue
  error_cgi
end