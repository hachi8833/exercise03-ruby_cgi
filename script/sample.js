function check() {
  var message = [];
  var regexp = new RegExp("^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$");

  if(document.form1.email.value == "") {
    message.push("・メールアドレスが入力されていません。\n");
  }
  else if(document.form1.email.value.match(regexp) == null) {
    message.push("・メールアドレスが正しくない可能性があります。\n");
  }
  if(document.form1.reason.value == ""){
    message.push("・志望動機が入力されていません。\n");
  }

  message =  message.join("");
  if(message != "") {
    alert("以下の項目を修正してください。\n\n" + message);
    return false;
  }
  else {
    return true;
  }
}