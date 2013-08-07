function check() {
  var message = [];

  if(document.form1.email.value == "") {
    message.push("・メールアドレスが入力されていません。\n");
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